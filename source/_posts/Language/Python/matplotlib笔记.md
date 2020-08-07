---
title: matplotlib笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - Python
date: 2020-08-07 13:07:42
tags:
---



## 基本库

## pyplot

<!-- more -->

[`matplotlib.pyplot`](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot) is a state-based interface to matplotlib. It provides a MATLAB-like way of plotting.

pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation:

```
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
```



### 常用函数

引入`import matplotlib as plt`

`plt.scatter(x, y, [s=None, c=None,...] )` A scatter plot of *y* vs *x* with varying marker size and/or color.

`plt.semilogy(x, y,)` 画出y轴取log的图像。

# 画图设置

## 嵌入项目

%matplotlib inline

## 设置图画大小

```
def set_figsize(figsize=(3.5, 2.5)):
    plt.rcParams['figure.figsize'] = figsize

set_figsize()
```

## 矢量图表示

```
def use_svg_display():
    # 用矢量图显示
    %config InlineBackend.figure_format = 'svg'
#输入为ts
def xyplot(x_vals, y_vals, name):
    set_figsize(figsize=(5, 2.5))
    plt.plot(x_vals.numpy(), y_vals.numpy())
    plt.xlabel('x')
    plt.ylabel(name + '(x)')
```

## 一行画多张图

```
#images is a list of matrixes of pictures, and label is the text about the pictures.
def show_fashion_mnist(images, labels):
    _, figs = plt.subplots(1, len(images), figsize=(12, 12))
    for f, img, lbl in zip(figs, images, labels):
        f.imshow(img.reshape((28, 28)))
        f.set_title(lbl)
        f.axes.get_xaxis().set_visible(False)
        f.axes.get_yaxis().set_visible(False)
    plt.show()
```

## 多子图

`121`表示1 * 2 的图像中占据第1个图像位置

```
iters = range(len(hist.history['loss']))    
 
# train
plt.subplot(121)
plt.plot(iters, hist.history['mae'], 'r', label='train mae')
plt.legend()
plt.plot(iters, hist.history['val_mae'], 'b', label='val mae')
plt.legend()
# val
plt.subplot(122)
plt.plot(iters, hist.history['loss'], 'g', label='train loss')
plt.legend()
plt.plot(iters, hist.history['val_loss'], 'k', label='val loss')
plt.legend()
plt.show()
```