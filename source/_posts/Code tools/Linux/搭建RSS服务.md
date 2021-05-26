---
title: 搭建RSS服务
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
  - 折腾
categories:
date: 2020-09-09 17:01:58
---

好怀念神奇又快捷的RSS功能啊。经过不懈的尝试和努力，终于在VPS-Ubuntuuh建了一个。

<!-- more -->

## 安装

首先安装docker:

```shell
sudo apt install docker.io

```

安装docker-compose。详细请见[官网](https://docs.docker.com/compose/install/)

接下来安装[Awesonme-TTRSS](http://ttrss.henry.wang/#deployment-via-docker)。经过本人的多次试错，安装在Ubuntu，采取Docker-Compose的方法安装，并不修改除了`SELF_URL_PATH`之外的所有配置是成功的唯一方法。

把`SELF_URL_PATH`修改为浏览器访问的网址，并且网址最好换成域名，做好DNS解析。

```shell
docker-compose up -d #后台启动即可
```

如果修改了`.yml`配置文件，删除container然后重启即可。

````shell
docker-compose donw #删除contianer
docker-compose up -d 
````



最后安装[RSSHUB](https://github.com/DIYgod/RSSHub)，配合在浏览器上安装[RSSHUB-Radar](https://github.com/DIYgod/RSSHub-Radar)。前者可以神奇地解析不可RSS获取的内容，后者可以搜寻RSS源，查找RSSible的内容，并与RSSHUB联动获取内容，最后可方便地订阅到RSS。



## 后记

但由于现在RSSHUB的官方文档挂掉了，好多功能有点难用了~~~