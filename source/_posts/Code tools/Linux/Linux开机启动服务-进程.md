---
title: Linux开机启动服务/进程
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-09-02 08:15:54
tags:
---

简记一下。

## [开机以root用户启动脚本](https://askubuntu.com/questions/290099/how-to-run-a-script-during-boot-as-root)

Place the script you want to run in the /etc/init.d directory and make the script executable.

<!-- more -->

```bsh
chmod 755 myscript
```

Once that is done create a symbolic link in the run level directory you would like to use, for example if you wanted to run a program in the graphical runlevel 2, the default runlevel for Ubuntu, you would place it in the `/etc/rc2.d` directory. You just cannot place it the directory, you must signify when it will run by indicating the startup with an “S” and the execution order is important. Place it after everything else that is in the directory by giving it a higher number.

If the last script to be run is `rc.local` and it is named `S99rc.local` then you need to add your script as `S99myscript`.

```bsh
ln -s /etc/init.d/myscript /etc/rc3.d/S99myscript
```

Each backward compatible `/etc/rc*.d` directory has symbolic links to the `/etc/init.d/` directory.





## [WSL开机启动服务配置方法](https://zhuanlan.zhihu.com/p/47733615)

创建启动脚本：

进入任意 WSL 发行版中，创建并编辑文件：/etc/init.wsl

```bash
#! /bin/sh
/etc/init.d/cron $1
/etc/init.d/ssh $1
/etc/init.d/supervisor $1
```

里面调用了我们希望启动的三个服务的启动脚本，设置权限为可执行，所有者为 root，这时候可以通过：

```bash
sudo /etc/init.wsl [start|stop|restart]
```

来启停我们需要的服务，在 Windows 中，开始-运行，输入：

```bat
shell:startup
```

按照你 WSL 使用的 Linux 发行版创建启动脚本，比如我创建的 Debian.vbs 文件：

```vb.net
Set ws = CreateObject("Wscript.Shell")
ws.run "wsl -d debian -u root /etc/init.wsl start", vbhide
```

这个脚本就会在你登陆的时候自动在名字为 "debian" 的 wsl 发行版中执行 /etc/init.wsl 启动我们的服务了，如果你用的是 ubuntu18.04 的发行版，那么修改上面脚本里的 debian 为 ubuntu1804.vbs：

```vb.net
Set ws = CreateObject("Wscript.Shell")
ws.run "wsl -d Ubuntu-18.04 -u root /etc/init.wsl start", vbhide
```

而如果你不知道自己的 WSL 发行版叫做什么名字，可以用 “wsl -l" 来查看。不管你用最初的 bash (ubuntu 16.04) 还是商店里下载的 debian/ubuntu1804 都能顺利启动服务了。

WSL 中有很多有用的服务，你可以按需删改 /etc/init.wsl ，但没必要塞很多东西进去影响你的启动速度，比如 mysql/mongodb 这些重度服务，可以需要的时候再启动，用完就停了。



## 其他参考博客

[linux开机自启动脚本](https://www.cnblogs.com/downey-blog/p/10473939.html)

[Linux 设置开机启动项的几种方法](https://blog.csdn.net/autoliuweijie/article/details/73279136)