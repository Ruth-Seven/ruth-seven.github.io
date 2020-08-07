---
title: Linux笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Linux
date: 2020-08-07 12:52:29
tags:
---



# 基础命令

`uname -r` 查看内核版本

<!-- more -->

`sudo lsb_release -a` 查看系统系统版本

`cp` 复制

`sudo -i` 提权， 使用 root 权限登录

`su user` 切换为user用户， 如果验证失败，可能原因是root密码未设置，（好像ubuntu的root密码每次开机都会变化，需要重新设置。系统不希望大家一直变身root）

`sudo passwd user` 更改user密码



# Ubuntu /debian 系操作

Ubuntu /debian 系最大的好处就是可以使用「软件源」进行软件安装，使用 Ubuntu 自带的 deb 包管理系统APT安装软件可以减少直接下载源码编译的麻烦，所以这里就要用到「apt-get」系列命令了。

注意APT与命令apt、apt-get是不同的，apt-get和apt是高层的APT的命令API。

## 更换 Linux 子系统的软件源并更新软件

因为默认的软件源是 Ubuntu 的官方源，我们可以选择替换为国内的软件源，比如说阿里云镜像的软件源。

`sudo -i` 提权， 使用 root 权限登录

```
cp /etc/apt/sources.list /etc/apt/sources.list.old
```

不难看出管理源的文件就是 sources.list。所以命令是：

```
vim /etc/apt/sources.list
```

阿里云源

```
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```

输入`apt-get update` Ubuntu 的软件源切换到阿里云的源了。`apt-get upgrade` 对当前系统的软件和类库进行来更新。

`update` 是同步 /etc/apt/sources.list 和 /etc/apt/sources.list.d 中列出的源的索引，这样才能获取到最新的软件包。

`upgrade`是升级已安装的所有软件包，升级之后的版本就是本地索引里的，因此，在执行 upgrade 之前一定要执行 update, 这样才能是最新的。

## APT

APT - Ubuntu’s Advanced Packaging Tool 是 Ubuntu 默认包管理工具。使用 Ubuntu 等 Linux 发行版时，我们往往都会使用 APT 等相似的包管理工具来安装、更新我们的软件包。命令 `apt` 和 `apt-get` 与 APT 不同，它们是用来和 APT 进行交互的高层命令执行工具。请大家清楚二者的区别。

其中，在 Ubuntu 16.04 中 Ubuntu 引入了 `apt` 命令来代替曾经老用户熟悉的 `apt-get`，提供了更用户友好的操作和命令行界面，对软件包 cache 缓存的处理也更为优雅。这里我推荐大家使用 `apt` 命令来与 APT 包管理工具交互，安装、管理和更新软件和依赖，接下来的文档中，我也都会使用 `apt` 命令进行介绍。

**推荐阅读：**[Difference Between apt and apt-get Explained - It’s FOSS](https://itsfoss.com/apt-vs-apt-get-difference/)

## bash

下载安装的 Windows Subsystem for Linux 默认就是 `bash` 的 Shell 环境。`bash` 是 Unix shell 的一种，是我们开发环境的基础。不过 `bash` 本身仅提供一个非常基础的命令行交互功能，没有类似 `zsh` 或 `fish` 等 Shell 的自动补全、命令提示等高阶功能。因此，这里推荐大家继续阅读，安装 `zsh` 或 `fish` 来替代 `bash`。

`zsh` 和 `fish`，都是 Unix-like 系统中不可或缺的好 Shell，它们都极大的拓展了我们命令行界面的交互体验。在命令行的世界中：

- `fish` 更加注重「开箱即用」的体验，让我们安装完成即拥有一个包含了命令高亮、自动补全等强大功能的 Shell 环境
- `zsh` 则更加重视拓展性，借助于社区中优秀的 `zsh` 插件系统 oh-my-zsh 以及无数优秀的插件，`zsh` 同样能有比肩 `fish` 甚至比 `fish` 更高阶的功能和体验

## zsh

### 安装、配置

安装 `zsh` 并将之设置为默认 Shell：

- 利用 apt 安装 `zsh`

```
sudo apt install zsh
```

下载安装 [oh-my-zsh](https://ohmyz.sh/)，可能是市面上最好的 `zsh` 配置管理工具：

- 运行命令下载安装

```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

- 将 `zsh` 作为默认的 Shell 环境（如果刚刚安装脚本没有这样做的话）：

```
chsh -s $(which zsh)
```

## fish

开箱即用的 `fish` 无需安装以上 `zsh` 中繁琐的插件就能拥有几乎全部上面提到的功能。如果你觉得 `zsh` 的配置繁琐无趣，那么 `fish` 可能更符合你的口味。

同样使用 Ubuntu 包管理工具安装 `fish`：

```
sudo apt install fish
```

将 `fish` 作为默认 Shell：

```
chsh -s $(which fish)
```

### 配置

未经任何配置的 `fish` 即直接支持了诸多优秀的命令行交互特性。上图的例子中，我们可以看到 `fish` 开箱自带的几个功能：

- 输入命令的实时高亮，错误命令标红
- 历史命令的记忆，对输入命令的实时补全
- 对 `*.png` 等通配符（Wildcard character）的支持
- 相对 decent 的命令提示符（Prompt）

`fish` 的配置文件位于 `~/.config/fish/config.fish`，这一文件之于 `fish` 就像 `.zshrc` 之于 `zsh`、`.bashrc` 之于 `bash` 一样。

有关 `fish` 的配置方法推荐大家查看其官方文档：[fish tutorial - fish shell](https://fishshell.com/docs/current/tutorial.html)

### 安装`Pip`

Ubuntu16.04系统默认Python3，安装Pip如下。

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本
sudo python3 get-pip.py    # 运行安装脚本。
```

判断是否安装

```
pip --version
```

升级 pip

```
pip install -U pip

```