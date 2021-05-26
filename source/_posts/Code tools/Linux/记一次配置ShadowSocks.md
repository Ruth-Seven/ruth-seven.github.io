---
title: 记一次配置ShadowSocks
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
  - bugs
  - 折腾
categories:
date: 2020-09-06 19:18:39
---

用香港服务器做一个代理。网上的教程很多，只需要5分钟就可以配置好。
<!-- more -->

## 安装

在VPS建议直接用python的pip3下载安装shadowsocks。

```shell
sudo apt install python-pip3 #ubuntu上是python3-pip
pip3 install shadowsocks
```

> [Win桌面下载地址](https://ifun.cool/go/?url=aHR0cHM6Ly9naXRodWIuY29tL3NoYWRvd3NvY2tzL3NoYWRvd3NvY2tzLXdpbmRvd3MvcmVsZWFzZXM/YWZ0ZXI9Mi41LjE=)
>
> [Andriod下载地址](https://ifun.cool/go/?url=aHR0cHM6Ly9naXRodWIuY29tL3NoYWRvd3NvY2tzL3NoYWRvd3NvY2tzLWFuZHJvaWQvcmVsZWFzZXM=)
>
> [更多下载地址](https://ifun.cool/app/648.html)

## 配置并启动

VPS上新建 `/etc/shadowsocks.json` 文件, 并写入以下内容

```
{
	"server":"0.0.0.0", #服务器上这部分必须为0.0.0.0
	"server_port":443, #通信端口
	"local_address":"127.0.0.1",
	"local_port":1080,
	"password":"your-passwd", #your password
	"timeout":300,
	"method":"aes-256-cfb",
	"fast_open":false,
	"workers":5
}
```

注意修改 `server` 和 `password`, `workers` 表示启动的进程数量。

然后使用以下命令启动: `ssserver -c /etc/shadowsocks.json -d start`

另外

```shell
#命令可以快捷启动，停止和重启服务
ssserver -c /etc/shadowsocks.json -d [start]|[stop]|[restart]
```



按照上面设置的参数配置，可以在本地的ShadowSocks客户端添加服务器和相关参数，即可连接成功。

## 错误



### 报错`undefined symbol EVP_CIPHER_CTX_cleanup`

[原文参考](https://kionf.com/2016/12/15/errornote-ss/)

错误原因是openssl1.1.0目前兼容性很不好，大部分的软件都不支持。

> 所以如果决定使用openssl1.1.0需要考虑很多兼容问题，必须保留1.0.2或1.0.1(不推荐，存在一些已知漏洞，最重要的是如果服务器要开http2，由于新版chrome必须使用ALPN的限制，只有1.0.2版本支持ALPN，所以必须升级到1.0.2)版本以便编译其他程序。

解决方法 ：

1. vim打开文件openssl.py

```
find / -name openssl.py
vim /yourpath/openssl.py
```

> 路径不同根据报错路径而定

2. 修改libcrypto.EVP_CIPHER_CTX_cleanup.argtypes

```vim
:%s/cleanup/reset/
:x
```

3. 重新运行ss即可

### 报错` Cannot assign requested address`

检查一下配置的服务器地址是不是`0.0.0.0`。



## 检查日志

检查日志`more /var/log/shadowsocks.log` 

最后一次的记录 `tail -n 30 /var/log/shadowsocks.log`

## [启动为服务](https://www.cnblogs.com/xiangyangcao/p/10099277.html)