---
title: Docker网络
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Docker
date: 2020-08-07 12:40:59
tags:
---



> 这部分涉及了具体的Linux网络部分，理解的不是特别透彻

Docker网络分为单host网络和多host网络，单host网络又分为无网络、host网络、 bridge网络和user-definer网络。

<!-- more -->

## 单host网络

单host网络实际上就是仅在一个主机上的多容器的网络，相反的多host网络定义就呼之欲出了。

### 无网络

无网络即没有任何网络可以连接，适用于安全要求高无网络连接需要的容器，可以通过`docker run --network=none`中指定。

### host网络

host网络即直接使用host主机上的网络配置，与主机配置一样，但是容易出现端口占用而冲突。通过`--network=host`指定。

### bridge网络

docker安装时会创建一个名为docker0的Linux bridge。不指定`--network`默认创建的容器都会连接到docker0上。

新建的容器连接到网桥上会建立一个`interfaces`，容器自身会建立一个网卡`eho@xxx`，容器的网卡会连接到docker0网桥上的`interfaces`。其拓扑结构如下：

[![image-20200511125601000](http://static.come2rss.xyz/image-20200511125601000.png)](http://static.come2rss.xyz/image-20200511125601000.png)

[image-20200511125601000](http://static.come2rss.xyz/image-20200511125601000.png)



（接下来的内容就非常的计算机网络了！，不同的网桥为啥不能通信？如果加上路由器（网管）就能通信了吗？希望以后读过TCP/IP之后再去学习）