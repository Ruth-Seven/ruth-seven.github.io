---
title: ssh笔记
thumbnail: 'http://static.come2rss.xyz/image-20200504091052190.png'
toc: true
top: 10
categories:
  - Code tools
  - Linux
date: 2020-08-07 12:51:22
tags:
---



[这内容是真的丰富](https://missing.csail.mit.edu/2020/command-line/)

Secure Shell(SSH) 是由 IETF(The Internet Engineering Task Force) 制定的建立在应用层基础上的安全网络协议。它是专为远程登录会话(甚至可以用Windows远程登录Linux服务器进行文件互传)和其他网络服务提供安全性的协议，可有效弥补网络中的漏洞。通过SSH，可以把所有传输的数据进行加密，也能够防止DNS欺骗和IP欺骗。还有一个额外的好处就是传输的数据是经过压缩的，所以可以加快传输的速度。目前已经成为Linux系统的标准配置。

<!-- more -->

## ssh安全机制

SSH之所以能够保证安全，原因在于它采用了非对称加密技术(RSA)加密了所有传输的数据。传统的网络服务程序，如FTP、Pop和Telnet其本质上都是不安全的；因为它们在网络上用明文传送数据、用户帐号和用户口令，很容易受到中间人（man-in-the-middle）攻击方式的攻击。就是存在另一个人或者一台机器冒充真正的服务器接收用户传给服务器的数据，然后再冒充用户把数据传给真正的服务器。

但并不是说SSH就是绝对安全的，因为它本身提供两种级别的验证方法：

第一种级别（基于口令的安全验证）：只要你知道自己帐号和口令，就可以登录到远程主机。所有传输的数据都会被加密，但是不能保证你正在连接的服务器就是你想连接的服务器。可能会有别的服务器在冒充真正的服务器，也就是受到“中间人攻击”这种方式的攻击。

第二种级别（基于密钥的安全验证）：你必须为自己创建一对密钥，并把公钥放在需要访问的服务器上。如果你要连接到SSH服务器上，客户端软件就会向服务器发出请求，请求用你的密钥进行安全验证。服务器收到请求之后，先在该服务器上你的主目录下寻找你的公钥，然后把它和你发送过来的公钥进行比较。如果两个密钥一致，服务器就用公钥加密“质询”(challenge)并把它发送给客户端软件。客户端软件收到“质询”之后就可以用你的私钥在本地解密再把它发送给服务器完成登录。与第一种级别相比，第二种级别不仅加密所有传输的数据，也不需要在网络上传送口令，因此安全性更高，可以有效防止中间人攻击。

[原文链接](https://blog.csdn.net/li528405176/article/details/82810342)

## ssh基本操作

### 安装

查看安装包

```
dpkg -l | grep ssh
```

安装本地的ssh的服务器和客户端

```
sudo apt-get install openssh-client #连其他人
sudo apt-get install openssh-server #让别人连
```

### 启动

启动ssh服务

```
# -e identail to -A select all processe
ps -e | grep ssh #如果有sshd 表示ssh已经启动
#没有则启动ssh
sudo /etc/init.d/ssh start
```

停止和重启ssh服务

```
sudo /etc/init.d/ssh stop  #server停止ssh服务 
sudo /etc/init.d/ssh restart  #server重启ssh服务
```

登陆

### **口令登陆**

**单个私钥登陆**

```
ssh name@ip

#调用图形界面
ssh -X name@ip

#如何客户机和服务器的登陆用户名相同可以省略用户名
ssh ip

#设置端口, 默认22	
ssh -p port name@ip
```

如果是第一次登陆还需要把服务器的IP加入可信列表。之后输入密码即可登陆。

**多个私钥配置**

修改：~/.ssh/config

```
Host name
	HostName xxx.xxx.xxx.xxx
	Port 22
	User root
	IdentityFile ~\\.ssh\\id_rsa
	PreferredAuthentications publickey
```

简化登录： ssh name

### 公钥配置

本机生成密钥对

```
ssh-keygen -t rsa # -t 表示密钥类型
#密钥生成后存在放 /home/用户名/.ssh,其中私钥为id_rsa, 公钥为 id_rsa.pub
```

Linux上传密钥到远程linux主机

```shell
ssh-copy-id name@ip
#或者
ssh-copy-id -i .ssh/id_ed25519.pub foobar@remote
#再或者
cat .ssh/id_ed25519.pub | ssh foobar@remote 'cat >> ~/.ssh/authorized_keys'
```

也可以手动创建对应文件：

```shell
cd ~/.ssh && touch authorized_keys //没有这个文件则创建
cat id_ras.pub >>  authorized_keys   //追加公钥，可以是多个 手动拷贝也可以，可以不用要后面的用户名，一行一个
chmod 600 authorized_keys
cd .. && chmod 700 .ssh
```



之后就可以直接使用ssh登陆而无需输入密码了

Window主机上传到Linux主机可以使用如下命令：

```shell
scp id_rsa.pub root@xxx:/root/.ssh/ 或者手动ftp等方式拷贝也可以
```

修改ssh配置

```
#: vim /etc/ssh/sshd_config
RSAAuthentication yes
PubkeyAuthentication yes
PermitRootLogin yes
#: service sshd restart
```

### 退出

```
exit
#或者按 Ctrl + D
```



### 运行程序

当我们利用ssh在远程主机上跑程序的时候，只要关闭了终端就会中断ssh连接，然后远程主机上正在跑的程序或者服务就会自动停止运行。我们可以利用 nohup + 需要运行的程序 使运行的程序在切断ssh连接的时候仍然能够继续在远程主机中运行。nohup即no hang up(不挂起)。

### Executing commands

An often overlooked feature of ssh is the ability to run commands directly. ssh foobar@server ls will execute ls in the home folder of foobar. It works with pipes, so ssh foobar@server ls | grep PATTERN will grep locally the remote output of ls and ls | ssh foobar@server grep PATTERN will grep remotely the local output of ls

> 注意两个命令的区别

*参考文章： (基本内容)[https://blog.csdn.net/li528405176/article/details/82810342], (进阶)[https://blog.csdn.net/pipisorry/article/details/52269785]*





## ssh其他

### 强制使用密码登陆

面对需要测试密码正确性，但秘钥配置完成的情况，需要强制密码登陆。

```shell
ssh -o PreferredAuthentications=password -o PubkeyAuthentication=no user@host
```

