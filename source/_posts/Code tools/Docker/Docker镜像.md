---
title: Docker镜像
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Docker
date: 2020-08-07 12:39:04
tags:
---





Dockerfile是镜像的描述文件，定义了如何构建镜像。

镜像中最基础的镜像是base镜像，不依赖于其他镜像，同时可以提供给其他镜像作为基础来扩展。那对应的Base镜像从Scratch构建。通常来说Base镜像是那些提供操作系统平台的镜像。

<!-- more -->

Linux的空间由内核空间（kernel）和用户空间（/dev,/proc等文件）组成。Linux启动时会加载bootfs文件系统，之后卸载掉bootfs，载入rootfs。对于base镜像而言，他底层使用的是Host的kernel，自身提供rootfs，比如基本命令、工具和程序库。也就是说对于镜像而言，内部他的kernel和host的kernel一致，而且无法修改。如果镜像对kernel有要求，可能使用虚拟机会更好一点。



[![img](http://static.come2rss.xyz/image-20200509141013201.png)](http://static.come2rss.xyz/image-20200509141013201.png)

如下图，两个不同Base镜像可以在同一个host共用底层kernel。

[![img](http://static.come2rss.xyz/image-20200509141349614.png)](http://static.come2rss.xyz/image-20200509141349614.png)

### 容器的分层结构

构建一个新容器如下图dockfile所示，docker按照命令构建了多层级的叠加起来的容器。

[![img](http://static.come2rss.xyz/image-20200509141824955.png)](http://static.come2rss.xyz/image-20200509141824955.png)

[![img](http://static.come2rss.xyz/image-20200509141836171.png)](http://static.come2rss.xyz/image-20200509141836171.png)

一个重要的原因就是共享资源，也就是说Docker会共享不同镜像中的相同层的资源，避免重复载入。同时Docker最后添加一个可写层（称为容器层，其之下都称为镜像层）到每一个镜像的顶部，所有镜像的修改都会记录到Writable Container。

[![img](http://static.come2rss.xyz/image-20200509142359240.png)](http://static.come2rss.xyz/image-20200509142359240.png)

其操作如下：

1. 添加文件：直接添加到容器层。
2. 读取文件：从上到下依次到各个镜像寻找此文件
3. 修改文件：同上查找文件并复制到容器层，然后修改（这称之为Copy-on-write）
4. 删除文件：同上查找文件并在容器层中记录下删除记录

### 构建镜像

有两种方式创建新镜像。一种是docker commit命令，另一种是写Dockerfile。

#### docker commit

这种方法不推荐使用，对其他人不知晓其构建方法，不透明，不安全，重现性差。

具体步骤：

1. 运行容器

2. 安装软件

3. 保存为新镜像并重命名

   ```
   docker ps #查看docker名字old_name
   docker commit old_name new_name
   ```

#### Dockerfile

##### 编写

可以在`/root`目录下构建一个Dockerfile文件，内容如下：

```
FROM ubuntu
RUN apt-get update && apt-get install -y vim
```

##### 构建

在Dockerfile文件夹下运行以下命令即可完成构建。

```
docker build -t ubuntu-with-vi-dockerfile .
```

> 在`.`构建imagename为名的docker镜像， `-t`为命名参数，`-f`可指定Dockerfile位置。其中`.`表示build context为当前目录。Docker默认从bulid context中查找Dockerfile文件，并通过`ADD`，`COPY`命令将Build context中的文件添加到镜像。

`--->20983rfjehwuh0e`就是表示docker构建了一个新的镜像，其iD为那串数字。

`--->Running in s132fj1142dSf`就是表示docker临时构建了一个镜像。

##### 缓存

Docker会缓存已有的镜像的镜像层，比如包含`RUN apt-get update && apt-get install -y vim`的新Dockerfile文件在构建时会直接利用已经存在的镜像，可以通过`--no-cache`禁用cache。

同时Dockfile的镜像层都是上层**依赖**下层的，所以只有之前一层的发生变化，镜像层的缓存就会失效。

在Docker**下载上传镜像**之时也会检查之前相同的docker镜像层来减少下载量。

##### 调试

进入在构建镜像失败之前的**成功的镜像**进行调试。

##### Run vs CMD vs ENTRYPOINT

三种命令有两种编写格式：`Shell`和`Exec`。

`Shell`格式比较简单。他会调用底层`shell`来执行命令，同时解析掉**环境变量**。其形如：

```
<instruction> <command>
ENV name Cloun Man ENTRYPOINT echo "Hello ,$name" #输出 Hello, Cloud man
```

`Exec`更易读。默认不解析而是直接调用命令, 当然也可以通过调用`sh`来解析环境变量，形如：

```
<instruction> ["executable", "param1", "param2",...]
ENV name Cloud Man ENTRYPOINT ["/bin/echo", "Hello, $name"] #输出：Hello, $name
ENV name Cloud Man ENTRYPOINT ["/bin/sh","-c" "Hello, $name"] #输出：Hello, Cloud man
```

`RUN`命令会执行命令并创建新的镜像层，常常用于安装软件包。注意要把`sudo apt-get update && apt-get insatll -y\package`放在一起，不然分层的特性可能导致更新的那层是很久之前构建的。

`CMD`命令将在容器运行初（docker run）执行命令，有三种格式：

1. 推荐的`Exec`：`CMD ["executable", "param1", "param2"]`
2. 为`ENRTYPOINT`提供参数，此时必须使用`Exec`：`CMD ["param1", "param2"]`
3. `Shell`格式：`CMD command param1 param2`

注意`CMD`命令会被`docker run`指定的命令所**代替**，且只有**最后**一个CMD命令会生效

`ENTRYPOINT`类似于`CMD`的执行命令格式，但是他不会被`docker run`指定的命令代替。同样的`ENTRYPOINT`有两种命令格式，但是不同的上面也讲了。`ENTRYPOINT`的参数一定都会被使用，同时可以由`CMD`提供参数，当然`CMD`参数也可以在容器启动是被动态替换掉。

> `RUN`安装应用和服务；`CMD`设置默认启动命令；``ENTRYPOINT`运行服务和应用，同时用`CMD`提供动态可变参数。

#### 其他Dockefile参数

（待学习）

### 分发镜像

特定镜像名字格式：`[image name] = [registry]:[port]/[username]/[repository]:[tag]`

默认tag值为`latest`，如果`build -t imagename:tag`中tag没有指明就会默认使用`latest`。registry默认为`hub.docker.com`，port默认为`5000`。

Docker Hub的repository的**Tag命令方式**如下：

1. `imagename:1`指向1这个分支中最新版本；
2. `imagename:1.2`指向1.2这个分支中最新版本；
3. `imagename:1.2.3`指向1.2.3这个分支中的版本；
4. `imagename:latest`指向最新版本；

用户上传的镜像的完整命名需要包含用户名字，形如`username/imagename:tag`。（官方维护的image没有名字）。而当用户上传到自己的registry是**记得加registry:post**。

#### 构建自己的Registry

官网上已经开源了repository的docker，可以直接安装。

注意对自己建立的registry上传的image**上传、下载**时，需要写成完整正确的image名字

