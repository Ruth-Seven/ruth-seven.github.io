---
title: wls2折腾笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-07 12:56:47
tags:
  - 折腾
---

[推荐阅读官方博客](https://docs.microsoft.com/en-us/windows/wsl/about) 其中对[WSL2介绍](https://docs.microsoft.com/en-us/windows/wsl/wsl2-index)。
基于 Hyper-V 结构，WSL2大幅改进了上一代WSL在系统层面的的I/O效率，增加了系统调用的全面性，甚至还能支持Docker,唯一遗憾的是网关上做了隔离（？）。

<!-- more -->

## 命令

安装官网博客的配置后，应该已经能够使用WLS2了。快速摘录几条命令。
更改Linux distro的WLS的运行版本：

```
wsl --set-version <Distro> 2 #设置为启动WSL2
wsl --set-version <Distro> 1 #设置为启动WSL1
```

设置默认安装distr的WSL2版本：

```
wsl --set-default-version 2
```

检查各个distr的WSL版本：

```
wsl --list --verbose #or wsl -l -v
```

## 网络连接问题

### Linux连PC

（In the initial builds of WSL2 preview）从Linux访问Windows中软件需要Linux连接主机的host ip。

获取主机LAN IP方法如下：

```
cat /etc/resolv.comf
```

之后就可以使用该IP地址连接到PC的服务器上了。

### PC连Linux

在高于18945版本的WIN10系统可以直接访问Localhost来访问Linux Dis的服务器。对应的低于此版本的WIN10需要获取Linux虚拟机的IP地址。即可由以下命令获取：

```
ip addr | grep  eth0
```

## 迁移WSL
如果你更换了电脑，如何将WSL迁移至新的电脑或windows系统中呢？

在旧电脑或系统中输入：

```shelll
wsl --export distro_name file_name.tar
```

此时wsl系统已经被打包成tar文件，在新的电脑或系统中输入：
```shelll
wsl --import distro_name install_location file_name.tar
```

此时就完成了wsl迁移。如果想删除wsl则执行：
```shelll
wsl --unregister distro_name
```

查询wsl安装情况执行：

```shelll
wsl --list
```
上述命令在windows powershell里执行。