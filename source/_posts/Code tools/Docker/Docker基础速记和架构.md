---
title: Docker基础速记和架构
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Docker
date: 2020-08-07 12:38:24
tags:
---



Docker是现代软件开发微服务的一个重要支柱，他让复杂多变的服务和系统能在仅一次调试和配置之后稳定运行——Build once, Vonfigure Once, and Run Auywhere.
Docker具有轻量、隔离的特性。Docker相比于虚拟化技术所需要的部署虚拟系统所要承担的巨大代价不同，Docker只需要将软件和依赖打包在一个镜像中，并与系统相隔离。Docker的图标的集装箱暗示了Container的作用——将软件打包起来，更快更方便的部署环境，消除了开发测试和生产环境的不一致性。

<!-- more -->



## 入门

### 安装

(官方在Ubuntu下的[安装和升级教程](https://docs.docker.com/engine/install/ubuntu/)，当然我更喜欢的是WIn10下WLS2中的[Docker官方安装](https://docs.docker.com/docker-for-windows/wsl-tech-preview/#download)（可见WSL2折腾笔记）和[VSCode的教程](https://code.visualstudio.com/blogs/2020/03/02/docker-in-wsl2)。

这里我配合WSL2和Window下的Docker安装，成功在PS中开启了Docker命令，同时在WSL2的Linux dis开启了Docker进程，并且可以通过Localhost访问~按照VsCode教程来说这样已经可以通过VSCode直接访问（access）WLS中的容器了。

### 测试

PS运行，可以访问localhost查看服务器，里面有docker更多教程。

```
docker run -dp 80:80 docker/getting-started
```

Linux Dis 运行：

```
docker ps # 如果成功，可以看到getting-started的容器正在运行！
```

> **Windows10下的配合WLS2的Docker使用建议：**
>
> - docker文题最好运行在Linux目录下，而非挂载在`/mnt`下的Win文件
> - VHDX文件的大小限制[WSL tooling built into Windows](https://docs.microsoft.com/en-us/windows/wsl/wsl2-ux-changes#understanding-wsl-2-uses-a-vhd-and-what-to-do-if-you-reach-its-max-size).
>
> - CPU和内存限制[WSL 2 utility VM](https://docs.microsoft.com/en-us/windows/wsl/release-notes#build-18945)
> - 安装桌面版Docker之前最好删除Linux Dis下的Docker版本

### 加速

为了提升镜像的安装速度，可以在`daocloud.io`中注册账户并点击顶部菜单的**加速器**，获取加速器命令，长得像这个样子`culr -sSl httpxxxxx | sh -s``。**执行**后，重启docker deamon即可获取飞一般的感觉。

```
systemctl restart docker.service #WSL2环境不支持此命令
```

## Docker架构

Docke以C/S为架构，组成部分为：Docker Clinet（docker命令启动）、Docker Server（Docker daemon）、Docker image、Registry和Docker Container。

[![img](http://static.come2rss.xyz/image-20200509133957253.png)](http://static.come2rss.xyz/image-20200509133957253.png)

用户通过Docker Clinet启动Docker，用命令来制作下载Docker镜像并运行。Docker daemon是服务器组建，以Linux后台服务的方式运行，负责创建、运行、监控容器、构建和存储镜像。

默认情况下Docker deamon**只能监听本地**host的客户端请求，如果需要远程客户端请求，可以添加配置（具体Google）。

Docker images和Docker container的关系就像模子和陶瓷，可以通过Docker images创建Docker containers。镜像的制作方法有三种：（1）从头创建；（2）下载并使用其他人的现成镜像；（3）在一个镜像基础上创建一个新的镜像。

Docker container作为Docker images的运行实例，可以通过CLI（命令行接口）和API启动。

Registry是存放Docker镜像的仓库，分为公有和默认的，其中Docker Hub( https://hub.docker.com/)就是Docker公司维护的公有镜像库。

### 例子

如果第一次安装Docker，运行这条命令

```
docker run -dp 80:80 httpd
```

实际上Docker是这么处理的：

[![img](http://static.come2rss.xyz/image-20200509135238794.png)](http://static.come2rss.xyz/image-20200509135238794.png)

## 常用命令

> ID一般都是指容器的ID，当然ID也可用其他值代替，比如系统取的随机名称。

### 镜像

> 

`docker build -t imagename .` 在`.`构建imagename为名的docker镜像， `-t`为命名参数，`-f`可指定Dockerfile位置。

`docker images imagename` 查看docker images 信息

`docker history imagename`可以获取镜像的构建历史

`docker tag imagename username/image:tag`实际上tag更像是一个改镜像名命令（原来image还保持原样）

`docker rmi imagename` 仅仅删除Docker host中的镜像。或者说删除某一个tag的镜像，当然如果一个镜像有多个tag，直到删除最后一个tag，这个镜像才被删干净。

### 容器

`docker run imagename` 运行docker images ，并输出容器的lID（长ID）

> `-it` 交互模式进入容器
>
> `-d` 后台运行
>
> `-p` 端口映射
>
> `--name`显式命名镜像，不加就会自动为镜像命名
>
> `--restart=always`容器“停止运行”（包括正常退出）时，总是重启容器
>
>  也可以`--restart=on-failure:3`最多重启三次

> 长期运行容器示例：`docker run imagename /bin/bash -c "while true; do sleep 1; done"`
>
> **资源限制**
>
> `-m`或者`--memory` 设置内存使用额度，如 `-m 200M --memory-swap=300M`设置了20M内存和300MSWAP磁盘额度。若参数为`-1`表示没有限制。
>
> `--vm n`开启n个内存工作线程
>
> `--vm-bytes 280M` 每个线程分配280M
>
> `-c 2048` 设置单个容器分配CPU权重（CPU share），其CPU share决定了该容器CPU分配时间占所有容器的权重，也就是算比例。默认参数为1024。
>
> 限制读写 可以查询block IO。

`docker create imagename`创建容器

`docker start id`启动容器

`docker pause id` \`docker unpause id` 停止\恢复容器

`docker stop id` 停止容器

`docker kill id` 杀死容器

`docker attach id` attach到容器启动进程的终端

`docker exec id` 进入容器中并启动新进程

```
docker ps` 显示运行中的容器。等价于`docker container ls
```

> `-a` 显示所有状态的容器，包括运行结束的镜像

`docker logs -f id` 持续打印输出

> `-f`持续打印

### 系统

`docker login -u username` 登陆Docker

`docker push imagename` 上传镜像到Docker hub。其镜像不用加tag就是上传统一repository中的所有镜像。

`docker pull imagename`下载对应镜像

`docker search imagename` 搜索镜像