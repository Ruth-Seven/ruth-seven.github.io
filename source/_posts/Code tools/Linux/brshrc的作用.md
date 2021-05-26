---
title: .brshrc的作用
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
date: 2020-08-26 12:43:15
tags:
---

Linux的Ubunut的用户目录下，`.bashrc`常被用于存储环境变量和别名语句，该文件会在Shell启动的时候自动被导入。

<!-- more -->

常见的手动导入`.bashrc`文件方式有`source ~/.bashrc`和`exce bash`。两者存在略微的不同，前者可能将`.bashrc`文件中的路径变量也导入，后者用一个新的bash替换旧的bash，可能导致bash的变量和历史命令丢失。
常见的别名：

```shell

alias ls='ls --color=auto'
#alias dir='dir --color=auto'
#alias vdir='vdir --color=auto'
```
`.bash_aliases`文件默认不存在，一般用于存放别名命令，如需使用需要用户手动创建。`.bashrc`文件中有一段：
```shell
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```
会检查该文件是否存在，如果存在就执行


