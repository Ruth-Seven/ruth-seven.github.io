---
title: DNS污染
thumbnail: 'http://static.come2rss.xyz/v2-67f3d2ee0cbe8ce18f94b0abcaabbcec_1440w.jpg'
toc: true
top: 10
categories:
date: 2020-08-31 21:29:09
tags:
---

<!-- more -->



<转载自[南通宵云网络](https://www.zhihu.com/org/nan-tong-xiao-yun-wang-luo-ke-ji-you-xian-gong-si)[](https://www.zhihu.com/question/48510028)>

更多[详细内容](https://zhuanlan.zhihu.com/p/86538629)

### 什么是DNS污染？


按照百度百科的解释就是：某些网络运营商为了某些目的，对DNS进行了某些操作，导致使用ISP的正常上网设置无法通过域名取得正确的IP地址。某些国家或地区为出于某些目的防止某网站被访问，而且其又掌握部分国际DNS根目录服务器或镜像，也可以利用此方法进行屏蔽。

和某些流氓运营商利用DNS劫持域名发些小广告不同，DNS污染则让域名直接无法访问了，非得修改DNS服务器不可。

### 怎么验证是否遭遇DNS污染？


1.点“开始”-“运行”-输入CMD，再输入 ipconfig /all ，在下“DNS SERVER”里找到你使用的DNS服务器地址。

2.再输入 nslookup [http://idcbest.com](https://link.zhihu.com/?target=http%3A//idcbest.com)（你的域名） 你的DNS服务器IP ，来查看是否能解析。

3.再输入 nslookup [http://idcbest.com](https://link.zhihu.com/?target=http%3A//idcbest.com) 8.8.8.8 使用Google的DNS服务器验证。

### 域名遭遇DNS污染怎么解决？


1.更换DNS解析服务器。一般来说，域名注册商家都是提供免费的DNS解析服务的，以我所实用的新之洲数据为例，就提供了许多免费的DNS解析服务，而且解析速度很快，比之前实用的什么万网之流要快得多，不可能全部被污染，所以更换两个DNS服务器即可。

2.使用第三方DNS解析服务。目前有很多第三方网站提供DNS解析服务，不少都是免费的，国内也有免费提供DNS解析服务的，使用第三方DNS服务可以部分解决问题，比如新之洲数据正在使用的DNSpod服务，就是国内还算比较稳定的DNS解析服务。

注意事项一：在换用第三方解析服务的时候，应该先到DNSPOD之类的解析服务商那里将域名解析，过几个小时再到新之洲数据之类的域名注册商那里去修改DNS服务器，这样可以避免博客出现因解析时间造成的空白期。

注意事项二：Godaddy目前本身域名就被DNS污染了，即使挂VPN也访问不了，只有更改自己电脑的DNS（比如改成google的8.8.8.8）才能访问。

3.搭建自己的DNS服务器。这样子最保险，当然也最是费时废财，有条件的朋友可以尝试。