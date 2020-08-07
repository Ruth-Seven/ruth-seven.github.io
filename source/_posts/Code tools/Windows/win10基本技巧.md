---
title: win10基本技巧
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Windows
date: 2020-08-07 12:57:20
tags:
---


<!-- more -->

# WIN10基本技巧

## 运行指令

`cmd` 运行cmd Terminal

`services.msc` 打开服务窗口（也可以通过任务管理器的服务页打开，或者计算机管理的 “服务和应用程序/服务”打开）。

`shell:startup`打开开机自启动软件的文件夹。



`msinfo32`显示系统详细信息

## CMD指令

### Tree

TREE [drive:][path] [/F] [/A]

/F 显示每个文件夹中文件的名称。（带扩展名）

/A 使用 ASCII 字符，而不使用扩展字符。

```
tree -f > list.txt  -- 将带扩展名的文件目录输出到list.txt文件中
卷 资料 的文件夹 PATH 列表
卷序列号为 70BA-EEC3
H:.
│  README.md
│  README.txt
│  
├─grangerData
│  ├─Airdata1
│  │      1226A_filled.csv
│  │      1239A_filled.csv
│  │      1241A_filled.csv
│  │      1243A_filled.csv
│  │      1247A_filled.csv
│  │      1260A_filled.csv
│  │      
│  ├─matched
│  │      1226A_58457_filled.csv
│  │      1239A_58569_filled.csv
│  │      1241A_58239_filled.csv
│  │      1243A_58752_filled.csv
│
```

### Ver

显示系统版本信息。

## 其他

### 进入安全模式

在锁屏界面点击电源，按下shift键，再点击重启。在弹出的蓝色界面中依次选择“疑难解惑”-“高级方案”-“重启”-“安全模式”（有点记不清了）

