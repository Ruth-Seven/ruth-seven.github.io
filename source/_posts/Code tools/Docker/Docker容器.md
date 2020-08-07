---
title: Docker容器
thumbnail: 'http://static.come2rss.xyz/th-1589169613559.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Docker
date: 2020-08-07 12:39:54
tags:
---



> 值得注意的是，命令中指定容器不同于镜像，需要指出名字。指定容器可以使用ps中显示的名称
>
> 和sID和`docker run`返回的lID（长ID）。
>
> ID一般都是指容器的ID，当然ID也可用其他值代替，比如系统取的随机名称。

<!-- more -->

## 进入容器

（看吐了Orz）



有两种方法可以进入容器，一种是`docker attch ID`，另一种是`docker exec -it id bash|sh`。

前者直径进入容器启动命令的终端，只适用于查看输出，适用性一般，而且可以使用`docker logs -f id`代替；后者会在容器中开启一个新进程并可以启动其他进程，除了查看输出优先推荐使用。

前者使用`ctrl+p` + `ctrl+q`组合推出终端，后者使用`exit`推出终端。

## 容器操作

容器其实是docker host上的一个进程。

`docker stop id` 停止容器——向该进程发送`SIGTERM`信号。

`docker kill id` 杀死容器——向该进程发送`SIGKILL`信号。

`docker start id` 重启容器，当然会保留第一次启动时运行的参数。

`docker restart id`重启容器，就是`stop`和`start`的组合。

`docker pasuse id` 暂时停止工作，容器不再占据CPU资源；`docker unpasuse id` 恢复工作；

`docker rm id` 删除容器；

> **批量删除：**
>
> ```
> docker rm -v $(docker ps -aq -f status=exited)
> ```

## 容器声明周期

[![docker-life-machine](http://static.come2rss.xyz/docker-life-machine.png)](http://static.come2rss.xyz/docker-life-machine.png)

[docker-life-machine](http://static.come2rss.xyz/docker-life-machine.png)



注意两个点：

1. 容器可以先`creat`再`start`，也可指直接`run`。
2. 从这张图看`kill`和`stop`命令效果相同。
3. 只有当容器正常退出和非正常退出，除了`kill`和`stop`之外都会依据`--restart`判断是否要重启

## Docker底层

Docker技术采用了cgroup来配置容器的各个性能限制的额度，用namespace来实现各个容器的共享和相互隔离同一个或多个设备、网络、文件和用户。

