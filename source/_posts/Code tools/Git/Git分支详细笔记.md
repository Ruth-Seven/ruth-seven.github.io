---
title: Git分支详细笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Git
date: 2020-08-07 12:46:06
tags:
---





> 很神奇 很有趣 仔细做了笔记 很有收获



## 何谓分支

> Tips：简而言之 分支都是指向commit的指针，每一个分支都随着commit的提交而向新commit移动



Git 保存的不是文件差异或者变化量，而只是一系列文件快照。<!-- more -->

在 Git 中提交时，会保存一个提交（commit）对象，该对象包含一个指向暂存内容快照的指针，包含本次提交的作者等相关附属信息，包含零个或多个指向该提交对象的父对象指针：首次提交是没有直接祖先的，普通提交有一个祖先，由两个或多个分支合并产生的提交则有多个祖先。

为直观起见，我们假设在工作目录中有三个文件，准备将它们暂存后提交。暂存操作会对每一个文件计算校验和（即第一章中提到的 SHA-1 哈希字串），然后把当前版本的文件快照保存到 Git 仓库中（Git 使用 blob 类型的对象存储这些快照），并将校验和加入暂存区域：

```
$ git add README test.rb LICENSE
$ git commit -m 'initial commit of my project'
```

当使用 `git commit` 新建一个提交对象前，Git 会先计算每一个子目录（本例中就是项目根目录）的校验和，然后在 Git 仓库中将这些目录保存为树（tree）对象。之后 Git 创建的提交对象，除了包含相关提交信息以外，还包含着指向这个树对象（项目根目录）的指针，如此它就可以在将来需要的时候，重现此次快照的内容了。

现在，Git 仓库中有五个对象：三个表示文件快照内容的 blob 对象；一个记录着目录树内容及其中各个文件对应 blob 对象索引的 tree 对象；以及一个包含指向 tree 对象（根目录）的索引和其他提交信息元数据的 commit 对象。概念上来说，仓库中的各个对象保存的数据和相互关系看起来如图 3-1 所示：

[![image-20200425191333714](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-commit-%E5%AF%B9%E8%B1%A1.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/Git-commit-对象.png)

[image-20200425191333714](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/Git-commit-对象.png)



 图 3-1. 单个提交对象在仓库中的数据结构

作些修改后再次提交，那么这次的提交对象会包含一个指向上次提交对象的指针（译注：即下图中的 parent 对象）。两次提交后，仓库历史会变成图 3-2 的样子：

[![image-20200425191533650](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/%E5%A4%9A%E4%B8%AA%E6%8F%90%E4%BA%A4%E5%AF%B9%E8%B1%A1%E4%B9%8B%E9%97%B4%E7%9A%84%E9%93%BE%E6%8E%A5%E5%85%B3%E7%B3%BB.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/多个提交对象之间的链接关系.png)

[image-20200425191533650](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/多个提交对象之间的链接关系.png)



 图 3-2. 多个提交对象之间的链接关系

Git 中的分支，其实本质上仅仅是个指向 commit 对象的可变指针。Git 会使用 master 作为分支的默认名字。在若干次提交后，你其实已经有了一个指向最后一次提交对象的 master 分支，它在每次提交的时候都会自动向前移动。

[![image-20200425191623606](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/%E5%88%86%E6%94%AF%E5%85%B6%E5%AE%9E%E5%B0%B1%E6%98%AF%E4%BB%8E%E6%9F%90%E4%B8%AA%E6%8F%90%E4%BA%A4%E5%AF%B9%E8%B1%A1%E5%BE%80%E5%9B%9E%E7%9C%8B%E7%9A%84%E5%8E%86%E5%8F%B2.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/分支其实就是从某个提交对象往回看的历史.png)

[image-20200425191623606](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/分支其实就是从某个提交对象往回看的历史.png)



 图 3-3. 分支其实就是从某个提交对象往回看的历史

## 创建和增长分支

那么，Git 又是如何创建一个新的分支的呢？答案很简单，创建一个新的分支指针。比如新建一个 testing 分支，可以使用 `git branch` 命令：

```
$ git branch testing
```

这会在当前 commit 对象上新建一个分支指针

其实答案也很简单，它保存着一个名为 HEAD 的特别指针。它指向你正在工作中的本地分支。运行 `git branch` 命令，仅仅是建立了一个新的分支，但不会自动切换到这个分支中去，所以在这个例子中，我们依然还在 master 分支里工作（参考图 3-5）。

[![image-20200425191947610](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/HEAD-%E6%8C%87%E5%90%91%E5%BD%93%E5%89%8D%E6%89%80%E5%9C%A8%E7%9A%84%E5%88%86%E6%94%AF.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/HEAD-指向当前所在的分支.png)

[image-20200425191947610](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/HEAD-指向当前所在的分支.png)



 图 3-5. HEAD 指向当前所在的分支

要切换到其他分支，可以执行 `git checkout` 命令。我们现在转换到新建的 testing 分支：

```
$ git checkout testing
```

这样 HEAD 就指向了 testing 分支（见图3-6）。

[![image-20200425192041060](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/HEAD-%E5%9C%A8%E4%BD%A0%E8%BD%AC%E6%8D%A2%E5%88%86%E6%94%AF%E6%97%B6%E6%8C%87%E5%90%91%E6%96%B0%E7%9A%84%E5%88%86%E6%94%AF.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/HEAD-在你转换分支时指向新的分支.png)

[image-20200425192041060](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/HEAD-在你转换分支时指向新的分支.png)



 图 3-6. HEAD 在你转换分支时指向新的分支

这样的实现方式会给我们带来什么好处呢？好吧，现在不妨再提交一次：

```
$ vim test.rb
$ git commit -a -m 'made a change'
```

图 3-7 展示了提交后的结果。

[![image-20200425192314264](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/%E9%9A%8F%E7%9D%80%E5%88%86%E6%94%AF%E4%B8%80%E8%B5%B7%E5%90%91%E5%89%8D%E7%A7%BB%E5%8A%A8.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/随着分支一起向前移动.png)

[image-20200425192314264](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/随着分支一起向前移动.png)



 图 3-7. 每次提交后 HEAD 随着分支一起向前移动

非常有趣，现在 testing 分支向前移动了一格，而 master 分支仍然指向原先 `git checkout` 时所在的 commit 对象。现在我们回到 master 分支看看：

```
$ git checkout master
```

图 3-8 显示了结果。

[![image-20200425192426649](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/HEAD%E5%9C%A8%E4%B8%80%E6%AC%A1-checkout-%E4%B9%8B%E5%90%8E%E7%A7%BB%E5%8A%A8%E5%88%B0%E4%BA%86%E5%8F%A6%E4%B8%80%E4%B8%AA%E5%88%86%E6%94%AF.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/HEAD在一次-checkout-之后移动到了另一个分支.png)

[image-20200425192426649](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/HEAD在一次-checkout-之后移动到了另一个分支.png)



 图 3-8. HEAD 在一次 checkout 之后移动到了另一个分支

这条命令做了**两件事**。它把 HEAD 指针移回到 master 分支，并把工作目录中的文件换成了 master 分支所指向的快照内容。也就是说，现在开始所做的改动，将始于本项目中一个较老的版本。它的主要作用是将 testing 分支里作出的修改暂时取消，这样你就可以向另一个方向进行开发。

我们作些修改后再次提交：

```
$ vim test.rb
$ git commit -a -m 'made other changes'
```

现在我们的项目提交历史产生了分叉（如图 3-9 所示），因为刚才我们创建了一个分支，转换到其中进行了一些工作，然后又回到原来的主分支进行了另外一些工作。这些改变分别孤立在不同的分支里：我们可以在不同分支里反复切换，并在时机成熟时把它们合并到一起。而所有这些工作，仅仅需要 `branch` 和 `checkout` 这两条命令就可以完成。

[![image-20200425192554108](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/%E4%B8%8D%E5%90%8C%E6%B5%81%E5%90%91%E7%9A%84%E5%88%86%E6%94%AF%E5%8E%86%E5%8F%B2.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/不同流向的分支历史.png)

[image-20200425192554108](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/不同流向的分支历史.png)



 图 3-9. 不同流向的分支历史

由于 Git 中的分支实际上仅是一个包含所指对象校验和（40 个字符长度 SHA-1 字串）的文件，所以创建和销毁一个分支就变得非常廉价。说白了，新建一个分支就是向一个文件写入 41 个字节（外加一个换行符）那么简单，当然也就很快了。

Git 的实现与项目复杂度无关，它永远可以在几毫秒的时间内完成分支的创建和切换。同时，因为每次提交时都记录了祖先信息（译注：即 `parent` 对象），将来要合并分支时，寻找恰当的合并基础（译注：即共同祖先）的工作其实已经自然而然地摆在那里了，所以实现起来非常容易。Git 鼓励开发者频繁使用分支，正是因为有着这些特性作保障。

# 分支操作

`git branch` 命令不仅仅能创建和删除分支，如果不加任何参数，它会给出当前所有分支的清单：

```
$ git branch
  iss53
* master
  testing
```

若要详细查看信息，运行 `git branch -v`：

```
$ git branch -v
  iss53   93b412c fix javascript issue
* master  7a98805 Merge branch 'iss53'
  testing 782fd34 add scott to the author list in the readmes
```

要从该清单中筛选出你已经（或尚未）与当前分支合并的分支，可以用 `--merged` 和 `--no-merged` 选项。

```
$ git branch --merged
  iss53
* master
$ git branch --no-merged
  testing
```

一般来说，列表中没有 `*` 的分支通常都可以用 `git branch -d` 来删掉。原因很简单，既然已经把它们所包含的工作整合到了其他分支，删掉也不会损失什么。对应的，如果简单地用 `git branch -d` 删除未合并的分支会提示错误，因为那样做会丢失数据：

```
$ git branch -d testing
error: The branch 'testing' is not fully merged.
If you are sure you want to delete it, run 'git branch -D testing'.
```

不过，如果你确实想要删除该分支上的改动，可以用大写的删除选项 `-D` 强制执行，就像上面提示信息中给出的那样。

`git branch -r`查看远程分支。

# 分支例子

> 官方内容写的很好，我进行一些简单的概括，[官方链接](https://git-scm.com/book/zh/v1/Git-分支-分支的新建与合并)（不过廖老师的例子和官方的好像啊 hhh）

**现在让我们来看一个简单的分支与合并的例子，实际工作中大体也会用到这样的工作流程：**

1. **开发某个网站。**
2. **为实现某个新的需求，创建一个分支。**
3. **在这个分支上开展工作.。**

假设此时，你突然接到一个电话说有个很严重的问题需要紧急修补，那么可以按照下面的方式处理：

1. 返回到原先已经发布到生产服务器上的分支。
2. 为这次紧急修补建立一个新分支，并在其中修复问题。
3. 通过测试后，回到生产服务器所在的分支，将修补分支合并进来，然后再推送到生产服务器上。
4. 切换到之前实现新需求的分支，继续工作。

## **分支的新建与切换**

首先，我们假设你正在项目中愉快地工作，并且已经提交了几次更新（见图 3-10）。

[![image-20200425193307440](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/%E4%B8%80%E4%B8%AA%E7%AE%80%E7%9F%AD%E7%9A%84%E6%8F%90%E4%BA%A4%E5%8E%86%E5%8F%B2.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/一个简短的提交历史.png)

[image-20200425193307440](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/一个简短的提交历史.png)



 图 3-10. 一个简短的提交历史

现在，你决定要修补问题追踪系统上的 #53 问题。把新建的分支取名为 iss53。要新建并切换到该分支，运行 `git checkout` 并加上 `-b` 参数：

```
$ git checkout -b iss53
Switched to a new branch 'iss53'
```

这相当于执行下面这两条命令：

```
$ git branch iss53
$ git checkout iss53
```

图 3-11 示意该命令的执行结果。

[![image-20200425193327729](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/%E5%88%9B%E5%BB%BA%E4%BA%86%E4%B8%80%E4%B8%AA%E6%96%B0%E5%88%86%E6%94%AF%E7%9A%84%E6%8C%87%E9%92%88.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/创建了一个新分支的指针.png)

[image-20200425193327729](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/创建了一个新分支的指针.png)



 图 3-11. 创建了一个新分支的指针

接着你开始尝试修复问题，在提交了若干次更新后，`iss53` 分支的指针也会随着向前推进，因为它就是当前分支（换句话说，当前的 `HEAD` 指针正指向 `iss53`，见图 3-12）：

```
$ vim index.html
$ git commit -a -m 'added a new footer [issue 53]'
```

[![image-20200425193347879](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/iss53-%E5%88%86%E6%94%AF%E9%9A%8F%E5%B7%A5%E4%BD%9C%E8%BF%9B%E5%B1%95%E5%90%91%E5%89%8D%E6%8E%A8%E8%BF%9B.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/iss53-分支随工作进展向前推进.png)

[image-20200425193347879](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/iss53-分支随工作进展向前推进.png)



 图 3-12. iss53 分支随工作进展向前推进

现在你就接到了那个网站问题的紧急电话，需要马上修补。有了 Git ，我们就不需要同时发布这个补丁和 `iss53` 里作出的修改，也不需要在创建和发布该补丁到服务器之前花费大力气来复原这些修改。唯一需要的仅仅是切换回 `master` 分支。

不过在此之前，留心你的暂存区或者工作目录里，那些还没有提交的修改，它会和你即将检出的分支产生冲突从而阻止 Git 为你切换分支。**切换分支的时候最好保持一个清洁的工作区域**。目前已经提交了所有的修改，所以接下来可以正常转换到 `master` 分支：

```
$ git checkout master
Switched to branch 'master'
```

此时工作目录中的内容和你在解决问题 #53 之前一模一样，你可以集中精力进行紧急修补。这一点值得牢记：Git 会把工作目录的内容恢复为检出某分支时它所指向的那个提交对象的快照。它会自动添加、删除和修改文件以确保目录的内容和你当时提交时完全一样。

接下来，你得进行紧急修补。我们创建一个紧急修补分支 `hotfix` 来开展工作，直到搞定（见图 3-13）：

```
$ git checkout -b hotfix
Switched to a new branch 'hotfix'
$ vim index.html
$ git commit -a -m 'fixed the broken email address'
[hotfix 3a0874c] fixed the broken email address
 1 files changed, 1 deletion(-)
```

[![image-20200425193421149](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/hotfix-%E5%88%86%E6%94%AF%E6%98%AF%E4%BB%8E-master-%E5%88%86%E6%94%AF%E6%89%80%E5%9C%A8%E7%82%B9%E5%88%86%E5%8C%96%E5%87%BA%E6%9D%A5%E7%9A%84.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/hotfix-分支是从-master-分支所在点分化出来的.png)

[image-20200425193421149](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/hotfix-分支是从-master-分支所在点分化出来的.png)



 图 3-13. hotfix 分支是从 master 分支所在点分化出来的

有必要作些测试，确保修补是成功的，然后回到 `master` 分支并把它合并进来，然后发布到生产服务器。用 `git merge` 命令来进行合并：

```
$ git checkout master
$ git merge hotfix
Updating f42c576..3a0874c
Fast-forward
 README | 1 -
 1 file changed, 1 deletion(-)
```

请注意，合并时出现了“Fast forward”的提示。由于当前 `master` 分支所在的提交对象是要并入的 `hotfix`分支的直接上游，Git 只需把 `master` 分支指针直接右移。换句话说，如果顺着一个分支走下去可以到达另一个分支的话，那么 Git 在合并两者时，只会**简单地把指针右移**，因为这种单线的历史分支不存在任何需要解决的分歧，**所以这种合并过程可以称为快进（Fast forward）。**

现在最新的修改已经在当前 `master` 分支所指向的提交对象中了，可以部署到生产服务器上去了（见图 3-14）。

[![image-20200425193448731](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/%E5%88%86%E6%94%AF%E6%8C%87%E5%90%91%E5%90%8C%E4%B8%80%E4%BD%8D%E7%BD%AE.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/分支指向同一位置.png)

[image-20200425193448731](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/分支指向同一位置.png)



 图 3-14. 合并之后，master 分支和 hotfix 分支指向同一位置。

在那个超级重要的修补发布以后，你想要回到被打扰之前的工作。由于当前 `hotfix` 分支和 `master` 都指向相同的提交对象，所以 `hotfix` 已经完成了历史使命，可以删掉了。使用 `git branch` 的 `-d` 选项执行删除操作：

```
$ git branch -d hotfix
Deleted branch hotfix (was 3a0874c).
```

现在回到之前未完成的 #53 问题修复分支上继续工作（图 3-15）：

```
$ git checkout iss53
Switched to branch 'iss53'
$ vim index.html
$ git commit -a -m 'finished the new footer [issue 53]'
[iss53 ad82d7a] finished the new footer [issue 53]
 1 file changed, 1 insertion(+)
```

[![image-20200425193514085](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/iss53-%E5%88%86%E6%94%AF%E5%8F%AF%E4%BB%A5%E4%B8%8D%E5%8F%97%E5%BD%B1%E5%93%8D%E7%BB%A7%E7%BB%AD%E6%8E%A8%E8%BF%9B.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/iss53-分支可以不受影响继续推进.png)

[image-20200425193514085](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/iss53-分支可以不受影响继续推进.png)



 图 3-15. iss53 分支可以不受影响继续推进。

值得注意的是之前 `hotfix` 分支的修改内容**尚未**包含到 `iss53` 中来。如果需要纳入此次修补，可以用 `git merge master` 把 master 分支合并到 `iss53`；或者等 `iss53` 完成之后，再将 `iss53` 分支中的更新并入 `master`。

## **分支的合并**

在问题 #53 相关的工作完成之后，可以合并回 `master` 分支。实际操作同前面合并 `hotfix` 分支差不多，只需回到 `master` 分支，运行 `git merge` 命令指定要合并进来的分支：

```
$ git checkout master
$ git merge iss53
Auto-merging README
Merge made by the 'recursive' strategy.
 README | 1 +
 1 file changed, 1 insertion(+)
```

**请注意，这次合并操作的底层实现，并不同于之前 `hotfix` 的并入方式。因为这次你的开发历史是从更早的地方开始分叉的。由于当前 `master` 分支所指向的提交对象（C4）并不是 `iss53` 分支的直接祖先，Git 不得不进行一些额外处理。就此例而言，Git 会用两个分支的末端（C4 和 C5）以及它们的共同祖先（C2）进行一次简单的三方合并计算。图 3-16 用红框标出了 Git 用于合并的三个提交对象：**

[![image-20200425193538900](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E4%B8%BA%E5%88%86%E6%94%AF%E5%90%88%E5%B9%B6%E8%87%AA%E5%8A%A8%E8%AF%86%E5%88%AB%E5%87%BA%E6%9C%80%E4%BD%B3%E7%9A%84%E5%90%8C%E6%BA%90%E5%90%88%E5%B9%B6%E7%82%B9.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/Git-为分支合并自动识别出最佳的同源合并点.png)

[image-20200425193538900](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/Git-为分支合并自动识别出最佳的同源合并点.png)



 图 3-16. Git 为分支合并自动识别出最佳的同源合并点。

这次，Git 没有简单地把分支指针右移，而是对三方合并后的结果重新做一个新的快照，并自动创建一个指向它的提交对象（C6）（见图 3-17）。这个提交**对象比较特殊，它有两个祖先**（C4 和 C5）。

值得一提的是 **Git 可以自己裁决哪个共同祖先才是最佳合并基础**；这和 CVS 或 Subversion（1.5 以后的版本）不同，它们需要开发者手工指定合并基础。所以此特性让 Git 的合并操作比其他系统都要简单不少。

[![image-20200425193934126](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/%E8%87%AA%E5%8A%A8%E5%88%9B%E5%BB%BA%E4%BA%86%E4%B8%80%E4%B8%AA%E5%8C%85%E5%90%AB%E4%BA%86%E5%90%88%E5%B9%B6%E7%BB%93%E6%9E%9C%E7%9A%84%E6%8F%90%E4%BA%A4%E5%AF%B9%E8%B1%A1.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/自动创建了一个包含了合并结果的提交对象.png)

[image-20200425193934126](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/自动创建了一个包含了合并结果的提交对象.png)



 图 3-17. Git 自动创建了一个包含了合并结果的提交对象。

既然之前的工作成果已经合并到 `master` 了，那么 `iss53` 也就没用了。你可以就此删除它，并在问题追踪系统里关闭该问题。

```
$ git branch -d iss53
```

## **遇到冲突时的分支合并**

有时候合并操作并不会如此顺利。如果在不同的分支中都修改了同一个文件的同一部分，Git 就无法干净地把两者合到一起（译注：逻辑上说，这种问题只能由人来裁决。）。如果你在解决问题 #53 的过程中修改了 `hotfix` 中修改的部分，将得到类似下面的结果：

```
$ git merge iss53
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

Git 作了合并，但没有提交，它会停下来等你解决冲突。要看看哪些文件在合并时发生冲突，可以用 `git status` 查阅：

```
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

        both modified:      index.html

no changes added to commit (use "git add" and/or "git commit -a")
```

任何包含未解决冲突的文件都会以未合并（unmerged）的状态列出。Git 会在有冲突的文件里加入标准的冲突解决标记，可以通过它们来手工定位并解决这些冲突。可以看到此文件包含类似下面这样的部分：

```
<<<<<<< HEAD
<div id="footer">contact : email.support@github.com</div>
=======
<div id="footer">
  please contact us at support@github.com
</div>
>>>>>>> iss53
```

可以看到 `=======` 隔开的上半部分，是 `HEAD`（即 `master` 分支，在运行 `merge` 命令时所切换到的分支）中的内容，下半部分是在 `iss53` 分支中的内容。解决冲突的办法无非是二者选其一或者由你亲自整合到一起。比如你可以通过把这段内容替换为下面这样来解决：

```
<div id="footer">
please contact us at email.support@github.com
</div>
```

这个解决方案各采纳了两个分支中的一部分内容，而且我还删除了 `<<<<<<<`，`=======` 和 `>>>>>>>` 这些行。在解决了所有文件里的所有冲突后，运行 `git add` 将把它们标记为已解决状态（译注**：实际上就是来一次快照保存到暂存区域**。）。因为一旦暂存，就表示冲突已经解决。如果你想用一个有图形界面的工具来解决这些问题，不妨运行 `git mergetool`，它会调用一个可视化的合并工具并引导你解决所有冲突：

```
$ git mergetool

This message is displayed because 'merge.tool' is not configured.
See 'git mergetool --tool-help' or 'git help config' for more details.
'git mergetool' will now attempt to use one of the following tools:
opendiff kdiff3 tkdiff xxdiff meld tortoisemerge gvimdiff diffuse diffmerge ecmerge p4merge araxis bc3 codecompare vimdiff emerge
Merging:
index.html

Normal merge conflict for 'index.html':
  {local}: modified file
  {remote}: modified file
Hit return to start merge resolution tool (opendiff):
```

如果不想用默认的合并工具（Git 为我默认选择了 `opendiff`，因为我在 Mac 上运行了该命令），你可以在上方”merge tool candidates”里找到可用的合并工具列表，输入你想用的工具名。我们将在第七章讨论怎样改变环境中的默认值。

退出合并工具以后，Git 会询问你合并是否成功。如果回答是，它会为你把相关文件暂存起来，以表明状态为已解决。

再运行一次 `git status` 来确认所有冲突都已解决：

```
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   index.html
```

如果觉得满意了，并且确认所有冲突都已解决，也就是进入了暂存区，就可以用 `git commit` 来完成这次合并提交。提交的记录差不多是这样：

```
Merge branch 'iss53'

Conflicts:
  index.html
#
# It looks like you may be committing a merge.
# If this is not correct, please remove the file
#       .git/MERGE_HEAD
# and try again.
#
```

如果想给将来看这次合并的人一些方便，可以修改该信息，提供更多合并细节。比如你都作了哪些改动，以及这么做的原因。有时候裁决冲突的理由并不直接或明显，有必要略加注解。

## 远程分支

远程分支（ *remote branch* ）是对远程仓库中的分支的索引。它们是一些无法移动的本地分支；只有在 Git 进行网络交互时才会更新。远程分支就像是书签，提醒着你上次连接远程仓库时上面各分支的位置。

我们用 (远程仓库名)/(分支名) 这样的形式表示远程分支。比如我们想看看上次同 origin 仓库通讯时 master 分支的样子，就应该查看 origin/master 分支。如果你和同伴一起修复某个问题，但他们先推送了一个 iss53 分支到远程仓库，虽然你可能也有一个本地的 iss53 分支，但指向服务器上最新更新的却应该是 origin/iss53 分支。

可能有点乱，我们不妨举例说明。假设你们团队有个地址为 git.ourcompany.com 的 Git 服务器。如果你从这里克隆，Git 会自动为你将此远程仓库命名为 origin，并下载其中所有的数据，建立一个指向它的 master 分支的指针，在本地命名为 origin/master，但你无法在本地更改其数据。接着，Git 建立一个属于你自己的本地 master 分支，始于 origin 上 master 分支相同的位置，你可以就此开始工作

如果你在本地 master 分支做了些改动，与此同时，其他人向 git.ourcompany.com 推送了他们的更新，那么服务器上的 master 分支就会向前推进，而于此同时，你在本地的提交历史正朝向不同方向发展。不过只要你不和服务器通讯，你的 origin/master 指针仍然保持原位不会移动（见图 3-23）。

可以运行 git fetch origin 来同步远程服务器上的数据到本地。该命令首先找到 origin 是哪个服务器（本例为 git.ourcompany.com），从上面获取你尚未拥有的数据，更新你本地的数据库，然后把 origin/master 的指针移到它最新的位置上（见图 3-24）。

[![image-20200425194111488](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/git-fetch-%E5%91%BD%E4%BB%A4%E4%BC%9A%E6%9B%B4%E6%96%B0-remote-%E7%B4%A2%E5%BC%95.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/git-fetch-命令会更新-remote-索引.png)

[image-20200425194111488](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/git-fetch-命令会更新-remote-索引.png)



图 3-24. git fetch 命令会更新 remote 索引。

为了演示拥有多个远程分支（在不同的远程服务器上）的项目是如何工作的，我们假设你还有另一个仅供你的敏捷开发小组使用的内部服务器 git.team1.ourcompany.com。可以用第二章中提到的 git remote add 命令把它加为当前项目的远程分支之一。我们把它命名为 teamone，以便代替完整的 Git URL 以方便使用（见图 3-25）。

[![image-20200425194159710](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/%E6%8A%8A%E5%8F%A6%E4%B8%80%E4%B8%AA%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%8A%A0%E4%B8%BA%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/把另一个服务器加为远程仓库.png)

[image-20200425194159710](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/把另一个服务器加为远程仓库.png)



 图 3-25. 把另一个服务器加为远程仓库

现在你可以用 git fetch teamone 来获取小组服务器上你还没有的数据了。由于当前该服务器上的内容是你 origin 服务器上的子集，Git 不会下载任何数据，而只是简单地创建一个名为 teamone/master 的远程分支，指向 teamone 服务器上 master 分支所在的提交对象 31b8e（见图 3-26）。

[![image-20200425194223404](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/Git-%E5%88%86%E6%94%AF%E8%AF%A6%E8%A7%A3/%E4%BD%A0%E5%9C%A8%E6%9C%AC%E5%9C%B0%E6%9C%89%E4%BA%86%E4%B8%80%E4%B8%AA%E6%8C%87%E5%90%91.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/你在本地有了一个指向.png)

[image-20200425194223404](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-分支详解/Git-分支详解/你在本地有了一个指向.png)



图 3-26. 你在本地有了一个指向 teamone 服务器上 master 分支的索引。

#### 推送本地分支

要想和其他人分享某个本地分支，你需要把它推送到一个你拥有写权限的远程仓库。你创建的本地分支不会因为你的写入操作而被自动同步到你引入的远程服务器上，你需要明确地执行推送分支的操作。换句话说，对于无意分享的分支，你尽管保留为私人分支好了，而只推送那些协同工作要用到的特性分支。

如果你有个叫 serverfix 的分支需要和他人一起开发，可以运行 `git push (远程仓库名) (分支名)`:

```
$ git push origin serverfix
Counting objects: 20, done.
Compressing objects: 100% (14/14), done.
Writing objects: 100% (15/15), 1.74 KiB, done.
Total 15 (delta 5), reused 0 (delta 0)
To git@github.com:schacon/simplegit.git
 * [new branch]      serverfix -> serverfix
```

> 这里其实走了一点捷径。Git 自动把 serverfix 分支名扩展为
>
> refs/heads/serverfix:refs/heads/serverfix，意为“取出我在本地的 serverfix 分支，推送到远程仓库的 serverfix 分支中去”。我们将在第九章进一步介绍 refs/heads/ 部分的细节，不过一般使用的时候都可以省略它。也可以运行 git push origin serverfix:serverfix 来实现相同的效果，它的意思是“上传我本地的 serverfix 分支到远程仓库中去，仍旧称它为 serverfix 分支”。通过此语法，你可以把本地分支推送到某个命名不同的远程分支：若想把远程分支叫作 awesomebranch，可以用 git push origin serverfix:awesomebranch 来推送数据。

接下来，当你的协作者再次从服务器上获取数据时，他们将得到一个**新的远程分支** origin/serverfix，并指向服务器上 serverfix 所指向的版本:

```
$ git fetch origin
remote: Counting objects: 20, done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 15 (delta 5), reused 0 (delta 0)
Unpacking objects: 100% (15/15), done.
From git@github.com:schacon/simplegit
 * [new branch]      serverfix    -> origin/serverfix
```

值得注意的是，在 fetch 操作下载好新的远程分支之后，你仍然无法在本地编辑该远程仓库中的分支。换句话说，在本例中，你不会有一个新的 serverfix 分支，有的只是一个你无法移动的 origin/serverfix 指针。

### 合并远程分支或者分化

**如果要把该远程分支的内容合并到当前分支，可以运行 git merge origin/serverfix。如果想要一份自己的 serverfix 来开发，可以在远程分支的基础上分化出一个新的分支来:**

```
$ git checkout -b serverfix origin/serverfix
Branch serverfix set up to track remote branch refs/remotes/origin/serverfix.
Switched to a new branch "serverfix"
```

这会切换到新建的 serverfix 本地分支，其内容同远程分支 origin/serverfix 一致，这样你就可以在里面继续开发了。

#### 跟踪远程分支

从远程分支 checkout 出来的本地分支，称为**跟踪分支(tracking branch)**。跟踪分支是一种和某个远程分支有直接联系的本地分支。在跟踪分支里输入 git push，Git 会自行推断应该向哪个服务器的哪个分支推送数据。同样，在这些分支里运行 git pull 会获取所有远程索引，并把它们的数据都合并到本地分支中来。

在克隆仓库时，Git 通常会自动创建一个名为 master 的分支来跟踪 origin/master。这正是 `git push` 和 `git pull` 一开始就能正常工作的原因。当然，你可以随心所欲地设定为其它跟踪分支，比如 origin 上除了 master 之外的其它分支。刚才我们已经看到了这样的一个例子：`git checkout -b [分支名] [远程名]/[分支名]`。如果你有 1.6.2 以上版本的 Git，还可以用`–track`选项简化:

```
$ git checkout --track origin/serverfix
Branch serverfix set up to track remote branch refs/remotes/origin/serverfix.
Switched to a new branch "serverfix"
```

要为本地分支设定不同于远程分支的名字，只需在第一个版本的命令里换个名字:

```
$ git checkout -b sf origin/serverfix
Branch sf set up to track remote branch refs/remotes/origin/serverfix.
Switched to a new branch "sf"
```

现在你的本地分支 sf 会**自动将推送和抓取数据的位置定位**到 origin/serverfix 了。

#### 删除远程分支

如果不再需要某个远程分支了，比如搞定了某个特性并把它合并进了远程的 master 分支（或任何其他存放稳定代码的分支），可以用这个非常无厘头的语法来删除它：git push [远程名] :[分支名]。如果想在服务器上删除 serverfix 分支，运行下面的命令:

```
$ git push origin :serverfix
To git@github.com:schacon/simplegit.git
 - [deleted]         serverfix
```

咚！服务器上的分支没了。你最好特别留心这一页，因为你一定会用到那个命令，而且你很可能会忘掉它的语法。有种方便记忆这条命令的方法：记住我们不久前见过的 `git push [远程名] [本地分支]:[远程分支]`语法，如果省略 [本地分支]，那就等于是在说“在这里提取空白然后把它变成[远程分支]”。

经过查阅资料发现，高版本的git也可以这么删除分支。

```
git push origin --delete Chapater6
```