---
title: Hexo建站
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
date: 2020-08-07 11:10:10
tags:
 - 折腾
categories:
---

# Hexo + Github Page 建站方案

终于开始了建站之旅，之前都是采用信息源（知乎+B站+RSS）->onenote笔记来记录知识点。随着时间的推移也发现更开源、令人兴奋的方法是写博客。一来是对自己要求提高了不少，写博客可不像自己随手摘的笔记, 要求严谨而逻辑清楚，二来便于分享知识和交往新胖友。

陆陆续续装了好久也踩了不少的坑，在今天2020.04.26写下这篇博文，记录博客的开端吧！
<!-- more -->

# 必要工具安装

首先有必要说明的是，Hexo建站不可避免的是Node等工具，不得不说Linux仍是建站初最好的环境，同时Window推出的WSL可以很好的提供Linux的包管理体验——真香。本蒻姬喜欢在用VSCODE + WSL来建站，同时使用原MD文件来渲染网页的Hexo还会保留MD文件，配合WSL文件可以被WINDOW访问的功能，可以直接使用VSCODE 和 Typora 写作——不要太方便。

Node.js建议安装比较新的版本，可以看[Github](https://github.com/nodesource/distributions)上下载源码（linux）并按照指示操作。以下是我安装的软件版本。

```
➜  _posts node -v
v10.20.1
➜  _posts npm -v
6.14.4
➜  _posts hexo -v
hexo: 4.2.0
```



npm作为强大的Node包管理工具可以使用以下命令安装。推荐阅读：[npm简介](https://juejin.im/entry/583d425161ff4b007eda246d)。

```
sudo apt update
sudo apt install npm
```

接下来安装hexo框架，hexo是静态页面博客框架，拥有丰富的主题资源和活跃的开发社区，很多Github Page的都是hexo搭建的，其中使用Next风格的网站尤其多~~~~~

hexo可使用npm全局安装，如下。

```
sudo hexo install hexo-cli -g
# -g：global
```

最会自行安装git并配置好ssh哦。

# 建站

hexo的使用逻辑是一键生成文章、页面、渲染页面、部署。在你想要存放建站文件的目录下运行以下命令可以初始化hexo博客文件。

```
hexo init [blog] #[$name]表name
cd blog
#局部安装hexo的指定本目录下的package.json的依赖包所指定的包
npm install
```

如果一切顺利的话，可以执行以下命令启动本地hexo服务器来测试是否安装成功。

```
hexo s #s: serve; 可选参数 -p 50100：指定监听端口
```

hexo可以通过以下命令来生成新文章——在source的_post文件下生成一个md文件。实际上hexo也会用这个md文件来渲染html页面，那就是后话了。在这里我非常推荐使用vscode自带的编辑器或者typero来编辑文件，尤其在文章的图片采取本地存储的情况下，typore支持直接插入图片并书写好合适的MD语句（typore扩展也支持图片上传服务器）。

```
#尽量避免 图片名、MD文件名出现空格，不然容易出BUG
hexo new "new-post"
```

当当！如果一切就绪，新文章也写好了，可以把本地文件部署到Github Page上去了。在Github上新建一个`用户名.github.io`的仓库，可以尝试去访问你的网站`用户名.github.io`~

deploy部署配置——在本地`bog`文件下的hexo配置文件`_config.yml`的部分内容，注意这里的配置连接最好使用SSH连接——免密输入的基操。

```
deploy:
  type: git
  repository: 'git@github.com:yourName/yourName.github.io.git'
  branch: master
```

使用以下命令可以把本地文件直接部署到GIthub上了,真方便啊。

```
# npm install hexo-deployer-git 如果不能直接d的话，装一下插件
hexo d
# 先生成再部署 更方便
hexo g -d
```

# 主题

找了两三个很Nice的博客主题[icarus](https://blog.zhangruipeng.me/hexo-theme-icarus/)，[yun](https://yun.yunyoujun.cn/) 和满大街的[Next](https://theme-next.org/)。其中安装教程详见官网。推荐阅读：[可能是最最完整的博客搭建教程](https://cloud.tencent.com/developer/article/1520557)

# Post！

## 图片

本地图片无法正常显示——本地图片引用网址多出了一个`.com/`，直到第二次重装工具和hexo这个问题曾经困扰才解决。图片在本地的放置方案如下：

设置`_config.yml`中的`post_asset_folder: true` ，以便在新建文章的时候同时生成可以放置图片同名文件夹。在MD文章中的图片引用格式为`[](./fileName/picName.png)`（注意，这两个名字不要带空格，不然有非常多的BUG，可以使用`-`代替）， 配合[hexo-asset-image](https://www.jianshu.com/p/3db6a61d3782)插件可以让HTML渲染的地址符合变化。

```
npm install https://github.com/7ym0n/hexo-asset-image --save
```

当然也有图床和OSS的解决方案，我这里暂时不去尝试，算是留一个坑。

## 个性化

### tags和categories

设置文章的`tags`和`categories`可以在文章的yaml语段中书写，具体如下，[官网介绍](https://theme-next.org/docs/theme-settings/custom-pages)。

> yaml 形如开头和结尾为三个横杠的键值对序列语段。
>
> ```
> ---
> title: Hello World
> date: 2013/7/13 20:46:25
> ---
> ```

```
categories:
#两层categories 
- [Sports, Baseball]
- [MLB, American League, Boston Red Sox]
- [MLB, American League, New York Yankees]
- Rivalries
tags:
- Injury
- Fight
- Shocking
```

设置博客页面`tags`和`categories`

```
hexo new page tags
hexo new page categories
```


**强烈推荐** 安装`hexo-auto-category`插件，使用目录自动化生成category，一劳永逸！下载
### 添加目录

确保`themes/icarus/_config.yml`中有

```
widgets:
    -
        # Widget name
        type: toc
        # Where should the widget be placed, left or right
        position: left
```

然后在文章头部添加标签

```
toc: true
```

### 阅读统计

[详见](https://susreal.com/article/2019/hexo-theme-icarus-2/#二、添加阅读统计)

### 文章置顶功能

在`themes/icarus/_config.yml`配置

```
index_generator:
    path: ''
    per_page: 10
    order_by:
        top: -1
        date: -1
```

修改`/⁨node_modules⁩/hexo-generator-index⁩/lib⁩/generator.js`

```
var paginationDir = config.pagination_dir || 'page';

// added code
posts.data = posts.data.sort(function(a, b) {
if(a.top && b.top) {
    if(a.top == b.top) return b.date - a.date;
    else return b.top - a.top;
}
else if(a.top && !b.top) {
    return -1;
}
else if(!a.top && b.top) {
    return 1;
}
else return b.date - a.date;
});
// end

var path = config.index_generator.path || '';
```

修改模板中的post.md，添加top属性并设置默认值为0

```
/scaffolds/post.md
---
title: {{ title }}
date: {{ date }}
tags:
top: 0
---
```

最后，根据大家自己的喜好在前端添加标签咯~

```
/themes/icarus/layout/common/article.ejs

<% if (post.top>0) { %>
<i class="fas fa-arrow-alt-circle-up" style="color:#3273dc"></i>
<span class="level-item" style="color:#3273dc">&nbsp;置顶</span>
<% } %>
```

### 更多阅读

现在已知最省事的还是直接在md文件中添加`<!-- more -->`

### 域名绑定

在本地_post文件的新建文件`CNAME`(大小写一致)，写上需要绑定的域名,比如一个二级域名`blog.yourhost.xyz`。
在购买域名的服务商那添加CNAME解析，比如原域名为A,主记录为`blog`,那么博客访问的地址如`XXXXX.github.io`就多了一个`blog.yourhost.xyz`。

> 这里注意，如果在github setting 添加域名绑定，要注意新的版本可能会移除掉`CNAME`文件。

### 添加缩略图到你的文章

你可以用两个步骤来添加缩略图到你的文章。首先，确保主题配置文件中已经开启缩略图的功能：

```
_config.yml
article:
	thumbnail: true
```

文章的front-matter中提供一个图像的链接或路径：

```
post.md
thumbnail: /gallery/thumbnails/desert.jpg
---
```

### 目录表（Table of Contents / Catalogue）

要在发布页显示目录表（toc）部件，请先在你文章markdown文件的front-matter中添加toc:true：

```
---
post.md
title: Table of Contents Example
toc: true
---
```

接着，在主题配置文件添加toc部件：

```
_config.yml
widgets:
    -
        type: toc
        position: left
```

#### front-matter模板

在scaffolds/post.md中修改为

```
---
title: {{ title }}
date: {{ date }}
tags:
-
categories: []
thumbnail: http://static.come2rss.xyz/尼尔机械.jpg
toc: true
top: 10
---



<!-- more -->
```

#### 添加自定义域名
在`public`文件下添加`CNAME`文件。内容仅为需要映射的自定义域名。

### 添加评论系统

Matery主题自带Gittalk模块，只需要配置Gittalk参数即可。Gittalk利用GitHup的repo中ISSUE功能，实现了全部用前端代码的强大评论功能。那么需要我们创建一个[OAuth应用](https://github.com/settings/installations)来存储评论信息，并且添加对应信息。

> Homepage:博客地址
>
> Authorization callback URL:存储评论的库地址
>
> [详细可以查看](https://blog.csdn.net/qing_gee/article/details/100133060)

接下来在`hexo-theme-matery`文件下的配置文件`_config.yml`中配置相关关键词`repo`、`clientID`、`clientSecret`等等。

![image-20200917133230897](http://static.come2rss.xyz/image-20200917133230897.png)

# 常用命令

## 部署步骤

至此，部署到GitHub的工作已经完成，之后如果我们希望对自己的博客进行修改或者需要发布新的文章时，可以按以下三步进行。

```
$ hexo clean # 删除已经生成的静态页面
#下面两个命令可以简写为 hexo g -d
$ hexo generate
$ hexo deploy
```

## 命令总结

### 常用命令

```
hexo new "postName" #新建文章
hexo generate #生成静态页面至public目录
hexo server #开启预览访问端口（默认端口4000，'ctrl + c'关闭server）
hexo deploy #将.deploy目录部署到GitHub
hexo help  # 查看帮助
hexo version  #查看Hexo的版本
hexo clean; hexo g -d; #清理已生成的页面，重新生成并部署。
```

启动本地服务器并监视文件变化，同时编译渲染。

```
hexo s --watch
```

## 命令简写

```
hexo n == hexo new
hexo g == hexo generate
hexo s == hexo server
hexo d == hexo deploy
```



## 快速在新环境下搭建网站


讲本地的源码上传到github的一个新分支hexocode中，与此同时，master保存着网页源代码，实现了快速下载hexo搭建配置的要求。
上传内容不多阐述，注意库中库问题就行。

更多[参考知乎内容](https://www.zhihu.com/question/21193762/answer/489124966)

### 下载分支搭建环境
更换电脑操作一样的，跟之前的环境搭建一样，安装gitsudo apt-get install git
设置git全局邮箱和用户名
```
git config --global user.name "yourgithubname"
git config --global user.email "yourgithubemail"
```
设置s
```
sh keyssh-keygen -t rsa -C "youremail"
```
生成后填到github和coding上（有coding平台的话）
验证是否成功

```shell
ssh -T git@github.com
ssh -T git@git.coding.net #(有coding平台的话)
```
安装nodejssudo 
```
apt-get install nodejs
sudo apt-get install npm
```
安装hexo  
```
sudo npm install hexo-cli -g
```
但是已经不需要初始化了，直接在任意文件夹下，
```
git clone git@………………
```
然后进入克隆到的文件夹：
```
cd xxx.github.io
npm install
npm install hexo-deployer-git --save
```
生成，部署：
```
hexo g
hexo d
```
然后就可以开始写你的新博客了hexo new newpage
Tips:不要忘了，每次写完最好都把源文件上传一下git add .
```
git commit –m "xxxx"
git push 
```
如果是在已经编辑过的电脑上，已经有clone文件夹了，那么，每次只要和远端同步一下就行了
```
git pull
```


### 改进
可能可以使用githook，比如pre-commit完成hexo部署时自动化提交本地配置变化。现在不做过多研究。




## 更新2021年1月28日 22:22:06 

## 插件 hexo-enchancer 推荐

[hexo-enhancer](https://segmentfault.com/a/1190000018402194)是一个Hexo功能增强插件。完全可以取代之前的hexo-auto-categories插件。

此插件支持的功能较多，并且未来会继续增加，可以理解为插件包。到目前为止，此插件支持的功能如下：

自动生成title：根据文件名自动生成标题。
自动生成date：根据文件名自动生成日期，具体策略类似Jekyll。
自动生成abbrlink：根据标题进行base32和crc32生成短链接。
自动生成categories：根据文件的路径解析文章所属分类。
自动生成tags：根据配置在_config.yml中的可用tags和keywords自动扫描文章中出现的标签。