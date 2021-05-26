---
title: CNAME和A记录
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-07 12:15:24
tags:
---

## 域名解析中A记录、CNAME记录的区别和联系

**域名解析**就是域名申请后做的到IP地址的转换过程。域名的解析工作由DNS服务器完成。

**A (Address) 记录**是用来指定主机名（或域名）对应的IP地址记录。用户可以将该域名下的网站服务器指向到自己的web server上。同时也可以设置您域名的二级域名。

**CNAME记录**即：别名记录。这种记录允许您将多个名字映射到另外一个域名。通常用于同时提供WWW和MAIL服务的计算机。例如，有一台计算机名为“host.mydomain.com”（A记录）。它同时提供WWW和MAIL服务，为了便于用户访问服务。可以为该计算机设置两个别名（CNAME）：WWW和MAIL。这两个别名的全称就 “[www.mydomain.com"](http://www.mydomain.com"/) 和“mail.mydomain.com”。实际上他们都指向“host.mydomain.com”。

**两者的区别在于**A记录就是把一个域名解析到一个IP地址（Address，特制数字IP地址），而CNAME记录就是把域名解析到另外一个域名。其功能是差不多，CNAME将几个主机名指向一个别名，其实跟指向IP地址是一样的，因为这个别名也要做一个A记录的。但是使用CNAME记录可以很方便地变更IP地址。如果一台服务器有100个网站，他们都做了别名，该台服务器变更IP时，只需要变更别名的A记录就可以了。

域名解析CNAME记录A记录对网站的影响不大。但是：CNAME有一个好处就是稳定，就好像一个IP与一个域名的区别