---
title: 记一次DNS分流
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
  - 折腾
categories:
date: 2020-08-31 20:21:44
---

最近因为下载Github文件却总是无法获取到真实IP，经过搜索发现是DNS被污染了。于是开始快乐的自建一个DNS服务器！
> 可以通过win自带的`nslookup`工具判断正在使用的DNS服务是否被污染。“正常”的DNS服务器可以解析出地址，如果无法解析肯定可以说明DNS被污染了。

<!-- more -->

## 安装

[Adgurd](https://github.com/AdguardTeam/AdGuardHome)是一款开源，能够强有力拦截广告的DNS服务器软件。Docker提供了快捷的[安装方式](https://hub.docker.com/r/adguard/adguardhome)。一键安装，网页管理，可视化数据显示，Nice~

## DNS-over-HTTPS

为了进一步保护隐私，防止中间人窃听DNS请求来获知我的访问网站，我推荐加上TLS加密保护我自己~

官网给出了详细[安装教程](https://github.com/AdguardTeam/AdGuardHome/wiki/Encryption)。

### Certbot

Certbot是一款自动化，自动修改服务器配置，可获取`Let's Encryption`的证书，并在过期前自动更新的强大工具包。

安装过程不再赘述，但是其中有一条：Certbot要求添加一条DNS TXT记录来验证安全性？（验证啥？没再看了）可以在域名解析的DNS解析商那边添加。

最后把获取的证书的两个PEM文件内容写到管理页面的加密设置那就OK了。

## 使用

按照管理页面的`设置指导`提示，可以在各个终端上使用该服务器作为DNS服务器。