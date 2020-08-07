---
title: 安装java
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - Java
date: 2020-08-07 13:06:33
tags:
---



## Install Oracle Java in WSL

<!-- more -->

Oracle Java至此已经发布到了14.01版本，已知的安装方法有两种。一种直接下载JKD，另一种采用包管理工具来管理JAVA的安装和升级。但是由于版权问题，后者对JAVA的版本支持只能到10。



## 直接下载JKD

可以直接去[官网](https://www.oracle.com/java/technologies/javase-downloads.html)，下载对应版本的JDK。需要注册Oracle账号，值得注意的是，我在初次注册的时候发现原有密码必须改变一次才能登陆。

> 黑人问号？.jpg

下载对应版本后解压到`/opt`文件夹下，并把JKD文件下的bin文件路径加入PATH。

```
tar -xzvf JKDFILE.tar.gz -C /opt
export PATH=/opt/JKDFILE/bin:$PATH
```

测试运行，结果正确即可。

```
java --version
javac --verison
```

## 包管理方法

具体操作参考[博文](https://thishosting.rocks/install-java-ubuntu/)。

## OpenJava

其实也可以直接下载开源的JAVA版本。