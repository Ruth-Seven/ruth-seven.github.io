---
title: Git笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Git
date: 2020-08-07 12:47:30
tags:
---



基础概念

七个非常非常常用的命令如下图所示。

[![img](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note//%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4.jpg)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note//常用命令.jpg)

<!-- more -->

## 提交\查看\删除命令

`.git`文件就是**版本库（**Repository），一般的目录就是**工作区**（Working Directory）

[![image-20200425184450980](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/%E5%B7%A5%E4%BD%9C%E5%8C%BA%E7%A4%BA%E6%84%8F.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/工作区示意.png)

[image-20200425184450980](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/工作区示意.png)



`git init`初始化Git仓库（也不一定必须在空目录下创建Git仓库，选择一个已经有东西的目录也是可以的）

`git add`把多个文件添加到stage; `git add fiilename`可单独添加文件。`git add`的工作就是要提交的所有修改放到**暂存区**（Stage）

`git commit -m "comment it"` 次性把暂存区的所有修改提交到分支。（

Note：add之后的修改是不会被commit上去的; 要使用双引号而不是引号。

`git status`查看仓库当前的状态

> Note:一般有三种状态`untracked`(文件没被添加）,`Changes not staged for commit`:（修改存没有存放在stage中），`Changes to be committed:`（修改已经添加到stage但是没有提交）、`nothing to commit, working tree clean`(全部已提交)；`changes`中也有几种状态`modified`,`deleted`等等。

`git diff` 查可以查看**工作区和版本库**里面最新版本的区别：`git diff HEAD -- readme.txt`可指定文件

Note：diff好像是按行比较的， `@@ -1,2 +1,7 @@`表示变化的开始和结束的行数和变化号（？）`git diff --cached`针对**暂存区**查看差别。

`git rm filename`可以删除**暂存区和工作区**中的的文件。

> Note: 若有误删，只能使用`reset HEAD filename`恢复到最新提交的版本，而commited之后的**修改都会丢失**，即存在数据丢失的情况。

## 版本控制

`git log`查看commit的日志；`--pretty=oneline`参数可简化输出。

> 如1094adb7b9b3807259d8cb349e7df1d4d6477073 (HEAD -> master) append GPL
>
> *1094adb7b9b3807259d8cb349e7df1d4d6477073* 是commit id(版本号)

`git log --all --graph --decorate`: visualizes history as a DAG

`git reflog` 查看使用的每一条commit和reset [ren’e’san’tian]命令，可用来查找从新版本回退的到旧版本之时的新版本的ID号。

首先在Git中，用`HEAD`表示当前版本，上一个版本就是`HEAD^`，上上一个版本就是`HEAD^^`，也可以写成`HEAD~DIFF_VERSION_NUMBER`。

[![image-20200425184637910](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/head%E6%8C%87%E9%92%88.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/head指针.png)

[image-20200425184637910](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/head指针.png)



`git checkout -- filename`可以丢弃**工作区**的**修改或者`rm`的删除** （这里很有意思！），这个文件回到最近一次`git commit`或`git add`时的状态。

> Note:`git checkout -- file`没有`--`，就变成了“切换到另一个分支”的命令；

`git checkout`其实是用**版本库里的版本替换工作区的版本**，无论工作区是**修改还是删除**，都可以“一键还原”。

`git reset HEAD filename`可以把暂存区的**修改和删除**撤销掉，重新放回工作区。（状态从to be committed 变成了 changes）。用于应对提交了错误代码或者`git rm`到stage，操作完后再用上述`checkout`命令改回原来的代码。

> Note：`git reset`命令既可以回退版本，也可以把暂存区的修改回退到工作区

`git reset --hard HEAD` 回退到上一个版本。也可以这么写`git reset --hard 1022a`,这个例子中`1022a`是所需要回退的版本的ID前几位（长度足够长而不至于重了就行）。

> Note: 如果在没有把已经commit的错误代码推送到远程库中，可在本地版本库中版本回退。

`git mergetool`: use a fancy tool to help resolve merge conflicts

`git rebase`: rebase set of patches onto a new base

# Git学习资源推荐

## Miscellaneous

- **GUIs**: there are many [GUI clients](https://git-scm.com/downloads/guis) out there for Git. We personally don’t use them and use the command-line interface instead.
- **Shell integration**: it’s super handy to have a Git status as part of your shell prompt ([zsh](https://github.com/olivierverdier/zsh-git-prompt), [bash](https://github.com/magicmonty/bash-git-prompt)). Often included in frameworks like [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh).
- **Editor integration**: similarly to the above, handy integrations with many features. [fugitive.vim](https://github.com/tpope/vim-fugitive) is the standard one for Vim.
- **Workflows**: we taught you the data model, plus some basic commands; we didn’t tell you what practices to follow when working on big projects (and there are [many](https://nvie.com/posts/a-successful-git-branching-model/) [different](https://www.endoflineblog.com/gitflow-considered-harmful) [approaches](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)).
- **GitHub**: Git is not GitHub. GitHub has a specific way of contributing code to other projects, called [pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).
- **Other Git providers**: GitHub is not special: there are many Git repository hosts, like [GitLab](https://about.gitlab.com/) and [BitBucket](https://bitbucket.org/).

## Resources

- [Pro Git](https://git-scm.com/book/en/v2) is **highly recommended reading**. Going through Chapters 1–5 should teach you most of what you need to use Git proficiently, now that you understand the data model. The later chapters have some interesting, advanced material.
- [Oh Shit, Git!?!](https://ohshitgit.com/) is a short guide on how to recover from some common Git mistakes.
- [Git for Computer Scientists](https://eagain.net/articles/git-for-computer-scientists/) is a short explanation of Git’s data model, with less pseudocode and more fancy diagrams than these lecture notes.
- [Git from the Bottom Up](https://jwiegley.github.io/git-from-the-bottom-up/) is a detailed explanation of Git’s implementation details beyond just the data model, for the curious.
- [How to explain git in simple words](https://smusamashah.github.io/blog/2017/10/14/explain-git-in-simple-words)
- [Learn Git Branching](https://learngitbranching.js.org/) is a browser-based game that teaches you Git.

# 远程仓库

Github允许使用了HTTP和SSH两种方式使用GIT，设置SSH能免去HTTP的权限和输入密码等限制。

## ssh

ssh — Secure Shell 工具是与远程服务器沟通的渠道。我们不仅可以使用 ssh 登录远程服务器，还可以利用 ssh 在不输入 GitHub 账户密码的情况下将 Git 仓库内容推送至 GitHub 远程仓库。

### ssh 登录 GitHub

下面配置与 GitHub 连接的 SSH 密钥（linux）

- 在 WSL 下生成 SSH 公钥 — 私钥对，此时生成的 SSH 密钥默认位于 `~/.ssh` 路径下，公钥为 `id_rsa.pub`，私钥为 `id_rsa`：

  > windows下的私钥放在个人用户的文件夹下`.ssh`。

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

- 打开 ssh-agent 使之在后台运行：

```
eval "$(ssh-agent -s)"
```

- 将私钥添加到 ssh-agent 之中：

```
ssh-add ~/.ssh/id_rsa
```

- 查看公钥并将之复制到剪贴板：

```
# 查看公钥内容
cat ~/.ssh/id_rsa.pub

# 将公钥复制到剪贴板
cat ~/.ssh/id_rsa.pub | clip.exe
```

- 将复制好的公钥添加到 GitHub 账户密钥里面[[2\]](https://dowww.spencerwoo.com/1.0/2-cli/2-3-others.html#fn2)

### 测试ssh

`ssh -T git@github.com`测试ssh是否能连接到github上 `ssh -T -p 443 git@ssh.github.com`换端口测试

编辑`~/.ssh/config`文件（没有则创建一个），然后补充下面的代码：

```
Host github.com
Hostname ssh.github.com
Port 443
```

## **新建仓库**

远程仓无内容：在本地仓上**新建一个仓库名与远程仓**一样的仓库，记得`add\\commit`

```
git remote add origin git@github.com:michaelliao/learngit.git
#push after commiting your code.
git push -u origin master
```

我们第一次推送`master`分支时，加上了`-u`参数，Git不但会把本地的`master`分支内容推送的远程新的`master`分支，还会把本地的`master`分支和远程的`master`分支关联起来。以后可以使用`git push origin master`推送最新修改。

> `git push --set-upstream [origin_source] [origin brance]` 也可以把本地分支追踪到远程分支。

本地仓无内容：（最好）新建一个远程仓，在`clone`下来，使用`$ git clone git@github.com:michaelliao/gitskills.git`。如果有多个人协作开发，那么每个人各自从远程克隆一份就可以了。

命令实例：

> ```
> //显示remote仓库
> git remote -v
> //添加远程仓库
> git remote add <shortname> https://github.com/paulboone/ticgit
> git pull <remote>
> git push <remote> <branch>
> //设置远程仓库上游分支
> git push --set-upstream origin master
> ```

### 如果远程仓库已经提交过代码

在本地和远程仓库都提交了至少一次commit之后，无法直接push上去代码，只能先pull下来（我观察）。可使用以下命令

```
#
git  pull origin master 
# 允许无相关历史的代码合并
git  pull origin master --allow-unrelated-histories   
`
```


## 远程分支

### 推送本地分支到远程
倘若远程仓库不存在被推得分支，远程仓库就会创建一个，且保持和推送内容一致。
```shell
git add *
git commit -m "@@"
git push -u <remote repo> <local branch>:<origin branch>
```
### 远程分支和本队分支不同步
远程分支如果内容被其他人更新或者本地分支重新创建的，需要先把远程分支pull到本地，进行合并,最后进行合并。
> 最好不要用`-f`。
```shell
# git remote add <shortname> https://github.com/paulboone/ticgit 如果没有添加远程仓库
git pull  <remote repo> <local branch>:<origin branch>
git push 
```
也存在本地分支内容无法和远程分支并存的情况，直接按上一节开一个新分支上传即可。


# 多人协作

由于涉及到一些多人操作，所以暂时不学了 等待下一个机会

[廖老师的多人协作](https://www.liaoxuefeng.com/wiki/896043488029600/900375748016320)

### 一些错误

win10可能未开启ssh服务， 在powershell中测试并打开, `Get-Service ssh-agent`可获取openssh服务运行状态，`Get-Service -Name ssh-agent | Set-Service -StartupType Manual`开启ssh服务。[SO的答案](https://stackoverflow.com/questions/52113738/starting-ssh-agent-on-windows-10-fails-unable-to-start-ssh-agent-service-erro)

`ssh -T git@github.com`可用于测试ssh秘钥是否连接正常；一定要输入yes不然会一直报错。。。

# 分支管理

传统的工作分支示例:

一人对应一个支线，**每个feature对应一个新支线**。

[![image-20200425185348609](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/%E5%B7%A5%E4%BD%9C%E5%88%86%E6%94%AF.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/工作分支.png)

[image-20200425185348609](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/工作分支.png)



廖雪峰关于GIT分支管理的讲述很清晰，精彩；[连接如下](https://www.liaoxuefeng.com/wiki/896043488029600/900003767775424)

本质上，每一个所谓的分支都是一个指针，每一个指针指向都是个提交的节点，创建和删除一个新的分支只不过是添加删除了一个指针。而一个新的**提交commit**也不过需要额外再移动一下指针罢了。而`HEAD`更是一个指向当前工作区的分支的指针。如图

[![image-20200425185438219](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/master%E5%88%86%E6%94%AF.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/master分支.png)

[image-20200425185438219](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/master分支.png)



## 基操

**友情提示**：每次在一个分支做的修改一定要commit之后，再去switch分支,不然出现会出现内容混乱的现象。保存现场参见下文。

`git brabch`列出所有分支，当前分支前面会标一个`*`号

`git switch -c dev` 创建（`-c` create）和切换到一个新的分支。相当于

```
创建：
git branch dev 
切换：
git checkout dev 或者 git switch dev
```

> Note: `git chechout -c dev`作用等同。

`git branch -d dev` (合并完成后，当然不是必须的，只是从工程目的上讲),可以删除`dev`分支了。`git branch -D dev` 可删除没有合并的分支，即**强行删除**（`-D`）。因为该分支没有被合并，如果删除，就会失去修改。

`git merge dev` 把dev分支合并到master（**现在所在的分支**,这里有两个信息，一个是隐含的）分支上。dev的修改就合并到了master上。

> Note：`Fast-forward`意味着“快进模式”，也就是直接把`master`指向`dev`的当前提交，合并速度非常快。但这种模式下，删除分支后，会丢掉分支信息。请使用`--no-ff`参数，表示禁用`Fast forward`：

## 分支冲突

分支冲突出现在两个在同一文件下修改相同地方的分支合并之时。（那都得是commit过了）

[![image-20200425185901715](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/%E5%88%86%E6%94%AF%E5%86%B2%E7%AA%81.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/分支冲突.png)

[image-20200425185901715](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/分支冲突.png)



Git用`<<<<<<<`，`=======`，`>>>>>>>`标记出不同分支的内容 。修改源文件，解决冲突后，提交过可得；

[![image-20200425185942196](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/%E8%A7%A3%E5%86%B3%E5%86%B2%E7%AA%81.png)](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/解决冲突.png)

[image-20200425185942196](http://blog.come2rss.xyz/2020/04/25/tools/linux/Git-note/Git-note/解决冲突.png)



`git log --graph --pretty=oneline --abbrev-commit`可以以图形化方式查看提交合并结果；`git log`本身也能查看结果。

## 保存现场以及修改BUG

如果当前任务没有完成，不能commit。则可以把**未被追踪过的文件（即没有被add过）**`git add`（追踪后），使用`git stash`保存现场。而Git把stash内容存在某个地方了，恢复现场有两个办法：一是用`git stash apply`恢复，但是恢复后，stash内容并不删除。另一种方式是用`git stash pop`，恢复的同时把stash内容也删了。

> 很像堆栈思想的上下文恢复

`git stash list`可以查看 git保存的工作现场的内容。

**应用：**工作中突然发现在过去的分支就出现一个bug，补救方法如下：[廖雪峰教程](https://www.liaoxuefeng.com/wiki/896043488029600/900388704535136)

如果不能直接把当前的工作commit掉，只能先`stash`,在切换分支、开分支、修bug然后commit，merge, 删除分支；如果后来开发的支线也有主线的bug，可以方便的使用`

`git cherry_pick commit-id`可在**当前分支**“**复制**”一次commit-id所修改的内容，他会自动提交一次**commit**。可以方便的解决不同支线相同bug的处理问题。

# 其他操作

## 配置别名

`git config --global alias.st status`就把`git st`就等价于`git status`。实例：

```
#花里胡哨的命令！
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

配置Git的时候，加上`--global`是针对**当前用户**起作用的，如果不加，那只针对当前的仓库起作用。每个**仓库的Git配置文件**都放在`.git/config`文件中：

```
$ cat .git/config 
[core]
    repositoryformatversion = 0
    filemode = true
    bare = false
    logallrefupdates = true
    ignorecase = true
    precomposeunicode = true
[remote "origin"]
    url = git@github.com:michaelliao/learngit.git
    fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
    remote = origin
    merge = refs/heads/master
[alias]
    last = log -1
```

别名就在`[alias]`后面，要删除别名，直接把对应的行删掉即可。

而当前用户的Git配置文件放在用户主目录下的一个隐藏文件`.gitconfig`中：

```
$ cat .gitconfig
[alias]
    co = checkout
    ci = commit
    br = branch
    st = status
[user]
    name = Your Name
    email = your@email.com
```

## 忽略文件

忽略特殊文件： 有时必须把某些文件放到Git工作目录中，但又不能提交它们，比如保存了数据库密码的配置文件啦，每次`git status`都会显示`Untracked files ...`。解决起来也很简单，在Git工作区的根目录下创建一个特殊的`.gitignore`文件，然后把要忽略的文件名填进去，Git就会自动忽略这些文件。

> Note:`.gitignore`文件本身要放到版本库里，并且可以对`.gitignore`做版本管理；不需要从头写`.gitignore`文件，GitHub已经为我们准备了各种配置文件，只需要组合一下就可以使用了。所有配置文件可以直接[在线浏览](https://github.com/github/gitignore)

编写忽略文件的**原则**是：

1. 忽略操作系统自动生成的文件，比如缩略图等；
2. 忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如Java编译产生的`.class`文件；
3. 忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。

对被忽略的文件，可以用`-f`**强制**添加到Git：

```
$ git add -f App.class
```

可以用`git check-ignore`命令**检查**`.gitignore`忽略某文件的某行：

```
$ git check-ignore -v App.class
.gitignore:3:*.class	App.class
```

## git 设置代理

```
$ git config --global http.proxy http://proxyUsername:proxyPassword@proxy.server.com:port
```

例如设置本地无认证的socks5代理，端口1080

```
$ git config --global http.proxy socks5://127.0.0.1:1080
```

## 常识

首先这里再明确一下，所有的版本控制系统，其实只能跟踪文本文件的改动，比如TXT文件，网页，所有的程序代码等等，Git也不例外。版本控制系统可以告诉你每次的改动，比如在第5行加了一个单词“Linux”，在第8行删了一个单词“Windows”。而图片、视频这些二进制文件，虽然也能由版本控制系统管理，但没法跟踪文件的变化，只能把二进制文件每次改动串起来，也就是只知道图片从100KB改成了120KB，但到底改了啥，版本控制系统不知道，也没法知道。所以版本控制是无法追踪WORD之类的二进制文件的。