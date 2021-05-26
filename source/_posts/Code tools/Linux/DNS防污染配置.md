---
title: DNS防污染配置
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-09-02 08:28:59
tags:
- 折腾
---






由于我国正处于发展不充分，不完全的阶段，DNS总是会出现一些莫名其妙的错误。twitter上不去，github下不了，非常尴尬。为了增进电脑使用体验，决定自己建一个DNS服务器避免DNS劫持和DNS毒化。

<!-- more -->

## 为啥要设置DNS

为了防止毒化，设置一个优秀正确而稳定的DNS服务器是必须的。如果有梯子的同学直接连接谷歌的`8.8.8.8`DNS服务器，当然也可以购买一台香港的服务器当做DNS服务器也OK。

> [Dns jump](https://www.sordum.org/7952/dns-jumper-v2-2/)一款的window下测量DNS使用速度的软件。随便测量了哪个世界知名的DNS服务器响应都不超过100ms，对上网影响太小了。直接推，随便选。

但是采用境外DNS服务器导致一个严重的使用体验不佳问题。访问本地网站尤其是淘宝等需要大量CDN静态内容的网站，出现长时间的卡顿以至于3分钟都无法加载。原因在于境外DNS把DNS请求转发给国内的DNS服务器，他会把离境外最近的CDN内容分发给我，这反而造成了访问速度下降。加之，三大运营商的网络之间主干道网速慢，平时的愉快的上网体验都是多运营商多服务器的多路配置提高了分发速度。DNS一出国，他就没有分配对应的运营商的服务器，进而又降低了网速。

## 解决思路

所以就有了以下广为传播的共识：国内的网站DNS请求转给国内DNS`114.114.114.114`，国外的DNS请求转给`8.8.8.8`。如此便可以保持国内上网体验的同时，保持国外网站不会被毒化。

这就要求本地设置一个DNS软件，而且要求能够分流DNS请求。上网查阅了一番，发现不少人已经鼓捣出来了。其次分流的前提是能够分清哪些域名去国外，哪些留在国内，这就需要一个白名单，当然

[GFWList](https://github.com/gfwlist/gfwlist)也可以抽出对应域名。

> 不过要写脚本~用Py和正则应该挺好写~

[更多内容](https://wzyboy.im/post/874.html)

### Daul DHCP DNS Server

[Daul DUCP DNS Server](https://sourceforge.net/projects/dhcp-dns-server/) Win环境下的[方案](https://zww.me/archives/25714)，但是存在白名单需要手动更新~~无力维护。折腾了半天，也算失败。

#### 安装

这节内容主要摘自[大佬](https://zww.me/archives/25714)：

1. 下载安装好（假定在 D:\DualServer）

2. 进入 D:\DualServer 目录，用文本编辑器打开 DualServer.ini

3. 找到 [SERVICES] 项部分，默认是开启 DHCP 和 DNS 服务的，因为我只要 DNS 功能，所以只开启 DNS 功能只要去掉 ;DNS 前面的英文分号 ;

4. 继续找到 [FORWARDING_SERVERS] 项，这里是指定默认的 DNS 服务器，这里我用 Google 的，所以加上

   ```
   8.8.8.8
   8.8.4.4
   ```

5. 然后就是重点了，找到 [CHILD_ZONES]（

   注：6.95RC后改名为

    

   [CONDITIONAL_FORWARDERS]

   ），这里是针对关键字自定义 DNS 服务器的地方，下面说说格式

   \- 拿淘宝网站来说明吧，淘宝一般的域名有：taobaocdn.com、taobao.com、tbcache.com、tdimg.com

   . 我们要设置这几个域名走电信的 DNS（这里我用路由器DNS代理地址——即路由器本身IP），那么格式如下

   

   ```
   taobaocdn.com=192.168.1.1
   taobao.com=192.168.1.1
   tbcache.com=192.168.1.1
   tdimg.com=192.168.1.1
   ```

   . 如果有多个 DNS 就这样（例如广东这边电信的 DNS 一般是 202.96.134.133 和 202.96.128.166）

   ```
   taobaocdn.com=202.96.134.133,202.96.128.166
   ```

6. 查看自己网卡的 IP 地址，因为 DualServer 默认会获取网卡的 IP 地址作为本地 DNS 服务器地址，不知道的可以在命令窗口敲 ipconfig 得到，这里假定是 192.168.1.100

7. 修改连接路由器的那个网卡的 DNS 服务器地址为 192.168.1.100（自淫？网卡自己的IP……）

8. 运行 RunStandAlone.bat，运行后会出现命令窗口显示 log，这样就OK了

**PS1：**如果你不想每次都要运行 RunStandAlone.bat 和看到那碍眼的命令窗口，那么你可以注册为系统服务，只要运行 DualServer.exe，然后去系统服务（命令行敲 services.msc）那里启动此服务，以后就会自动运行了，不过注意，如果你修改了 DualServer.ini 参数，需要停止再启动此服务——嫌麻烦就重新启动计算机

#### 配置白名单

在[大佬文章](https://wzyboy.im/post/874.html)中，我找到了一个为维护白名单的Coder。在Github上下载了他的名单后，用Python写了了脚本修改了一下地址格式，然后加到这个程序的`.ini`里面。

```python
# 参考

import os
import re
filepath = "./DualServer.ini"
filepath_w = filepath + "_w"
def replace(line):
    restring1 = r"^([a-zA-Z0-9\.\-]*?)/([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})$"
    restring2 = r"^server=/([a-zA-Z0-9\.\-]*?)/([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})$"
    reobj1 = re.match(restring1, line)
    reobj2 = re.match(restring2, line)
    if reobj1:
        return reobj1.group(1)+ '=' + reobj1.group(2) + '\n'
    elif reobj2:
        return reobj2.group(1) + '=' + reobj2.group(2)+ '\n'
    else:
        # print("Sorry! There isn't string for match\n", line)
        return line
    
with open(filepath, 'r+') as f:
    with open(filepath_w, 'w') as f_w:
        for line in f.readlines(): 
            newLine = replace(line)
            f_w.write(newLine)        
print(replace("sdkjf/114.223.432.11"))
```

使用一下发现还是挺不错的，偏偏淘宝相关的网站怎么也快不起来，结果一查DNS Log果然还是发给了国外的DNS服务器。诶毕竟了3年前的IP地址了。一个个加新域名完全加不完~~所以这也是一条死路。

### DNSforwarder

作为win和linux都有的DNS转发代理，做的功能已经相当齐全了, 但是同样缺少IP或者域名维护功能。详情请见[DNSforwarder Github](https://github.com/holmium/dnsforwarder)。

### DNSMASQ

[freeDNS](https://github.com/tuna/freedns-go)



### FreeDNS

该软件可以直接在Linux上[配置](https://github.com/tuna/freedns-go)。集成了DNS分流和DNS请求的功能，算是一个比较好的实现。

### ChinaDNS

貌似问题比较多的，[具体看](https://github.com/shadowsocks/ChinaDNS)

