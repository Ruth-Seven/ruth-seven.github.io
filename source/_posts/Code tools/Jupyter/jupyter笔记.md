---
title: jupyter笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Jupyter
date: 2020-08-07 12:48:55
tags:
---



## 设置默认工作目录

Jupyter notebook 只能在打开的工作目录下工作（创建文件，运行代码），所以十分有必要修改默认代码目录。

<!-- more -->

##### 在Anaconda Prompt中生成配置文件

打开Anaconda Prompt，输入如下命令：

```
jupyter notebook --generate-config1
```



##### 打开配置文件

根据显示的路径，打开配置文件jupyter_notebook_config.py，全文搜索【notebook_dir】，找到后填入自己的工作路径并保存。（注意：工作路径不能出现中文，否则无法打开Jupyter Notebook）

[![image-20200503125317705](http://static.come2rss.xyz/image-20200503125317705.png)](http://static.come2rss.xyz/image-20200503125317705.png)

[image-20200503125317705](http://static.come2rss.xyz/image-20200503125317705.png)



##### 修改JupyterNotebook快捷方式的目标属性(如果用Prompt也许就不用了)

右击JupyterNotebook快捷方式，选择【属性】，删除【目标】属性中的【%USERPROFILE%】，点击【应用】–【确定】。