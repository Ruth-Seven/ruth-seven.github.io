---
title: opencv-python 之路径问题
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
  - bugs
categories:
date: 2020-10-22 16:27:49
---

今天被OPEPCV-PYTHON整了，用`cv2.imread(path)`导入图片，结果啥都没有。查了半天发现是WINDOW下`opencv`在绝对路径下只支持`\`作为分隔符，在相对路径上只支持`/`！！

<!-- more -->

真的是气死我了，找了1个小时的bug！ 
2020.10.22.16.30 