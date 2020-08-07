---
title: python系统操作
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - Python
date: 2020-08-07 13:13:52
tags:
---

<!-- more -->



# 安装库

## 镜像库

```
 #华中科技的很快
https://pypi.mirrors.ustc.edu.cn/simple/
 #清华的一般
 https://pypi.tuna.tsinghua.edu.cn/simple some-package
 #豆瓣也OK
 https://pypi.douban.com/simple/
```



## 临时使用

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

#有些模块只能在官方的站点下？
pip install  tensorflow -i https://pypi.org/simple
```

注意，`simple` 不能少, 是 `https` 而不是 `http`

## 设为默认

升级 pip 到最新的版本 (>=10.0.0) 后进行配置（如果是WIN，记得用管理员身份运行CMD）：

```
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```

## 连接超时

```
pip --default-timeout=100 install -U tensorflow-gpu # 设置超时时间
```

## PYTHON 包安装更新

在PYcharm中，双击pip后面的蓝色升级箭头按钮。

[![image-20200503125713771](http://static.come2rss.xyz/image-20200503125713771.png)](http://static.come2rss.xyz/image-20200503125713771.png)

[image-20200503125713771](http://static.come2rss.xyz/image-20200503125713771.png)



会出现如图所示，Specify version要打对勾。然后install package即可。

或者使用命令操作：`--upgrade`

```
pip install --upgrade tensorflow -i https://pypi.org/simple
```

有时候由于一些环境上的问题，导致`pip`无法及时更新，所以采取另一种更新方法更有效

```
#强制更新
python3 -m pip install -U --force-reinstall pip
```

# PIP使用

pip 当前内建命令并不支持升级所有已安装的Python模块。

列出当前安装的包：

```
pip list
```

列出可升级的包：

```
pip list --outdate
```

升级一个包：

```
pip install --upgrade requests  // mac,linux,unix 在命令前加 sudo -H
```

升级所有可升级的包：

```
$ pip freeze --local | grep -v '^-e' | cut -d = -f 1  | xargs -n1 pip install -U
pip list -o --format legacy|awk '{print $1}'` ; do pip install --upgrade $i; done
```

显示包的信息

```
pip show numpy
```

删除包

```
pip uninstall numpy
```

pip默认源由于墙，所以速度很慢，可使用第三源提高速度：

```
vim ~/.pip/pip.conf
[global]



trusted-host = mirrors.aliyun.com



index-url = http://mirrors.aliyun.com/pypi/simple
```