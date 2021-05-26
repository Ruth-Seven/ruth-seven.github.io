---
title: md文件cdn加速
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
tags:
  - 折腾 
categories:
date: 2020-08-07 11:57:43
---

# ypore+七牛OSS\CDN图片快速上传

需要提前准备：一个备案好的主域名A，七牛认证过的bucket。

<!-- more -->

## 配置七牛CDN加速

上传七牛的图片需要在CDN加速的域名处下载，为此需要在七牛的域名管理中添加自定义二级域名，比如`static.A` 。获取了七牛提供的解析域名值后在服务商出添加CNAME解析。

> CNAME解析中主机值就是`static.A`的`static`，可能服务商在等等添加CNAME过程时间比较长，be patient.

## 配置Typore上传七牛

Typore整合了图片上传工具ipicgo的功能，提供了ipic-core直接上传功能，只需要配置即可.

[官方文档](https://support.typora.io/Upload-Image/#picgo-core-command-line-opensource)，[picgo-Core中文文档](http://blog.come2rss.xyz/2020/05/03/tools/blog/md文件cdn加速/[https://picgo.github.io/PicGo-Core-Doc/zh/guide/config.html#默认配置文件](https://picgo.github.io/PicGo-Core-Doc/zh/guide/config.html#默认配置文件)) 包括了七牛配置。

```
{
  "picBed": {
    "uploader": "qiniu", // 代表当前的默认上传图床
    "qiniu": {
      "accessKey": "",
      "secretKey": "",
      "bucket": "", // 存储空间名
      "url": "", // 自定义域名
      "area": /"z0" | "z1" | "z2" | "na0" | "as0", // 存储区域编号, 这个一定要选对，不知道多试几次
      "options": "", // 网址后缀，比如？imgslim
      "path": "" // 自定义存储路径，比如 img/， 测试后好像没法使用
    }
  },
  "picgoPlugins": {} // 为插件预留
}
```

## 使用

我的方案是复制图片到固定文件夹`FilePath/${filename}`，实现图片的本地分类管理，并在编辑框中使用typore自身功能快键上传图片的七牛，同时typore会自动获取并替换图片连接URL。

当然也可以从七牛空间管理中复制图片外链（要求空间为公共）。