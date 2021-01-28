---
title: WSL杀死进程
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-07 12:50:25
tags:
---

WLS2的Ubuntu18.04下没有办法直接使用`kill -s 9 PID`杀死进程，可是神奇的用`kill -9 PID`代替。