---
title: linux有趣的工具
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Linux
date: 2020-08-07 12:59:58
tags:
---





 这是慕课上的作业笔记，网站以后再补。

## 编辑器

<!-- more -->

[VIM](https://missing.csail.mit.edu/2020/editors/)

## 命令和CLI工具

见shell命令学习和Linux常用工具的笔记。

## 数据处理

`|` 管道，典型的案例就是查看远程服务器历史记录。

```
$ ssh myserver 'journalctl | grep sshd | grep "Disconnected from"' > ssh.log
$ less ssh.log
```

`sed`数据流编辑器在`ed`编辑器上发展而来，可以使用命令来修改文件。

```
ssh myserver journalctl
 | grep sshd
 | grep "Disconnected from"
 | sed 's/.*Disconnected from //'
```

The `s` command is written on the form: `s/REGEX/SUBSTITUTION/`, where `REGEX` is the regular expression you want to search for, and `SUBSTITUTION` is the text you want to substitute matching text with.

> 更多关于正则表达式的内容可参见[Regular Expressions](https://missing.csail.mit.edu/2020/data-wrangling/)

`akw`一个可以处理数据的编程语言

`R`和`bc`可以计算数据

`gnuplot`可以方便的画图

`xrags`可安装或者卸载包

`ffmpeg`可获取并处理图像数据

## 进程处理

#### killing a processes

`Ctrl-C`可以停止执行当前执行的进程。它会发送一个`SIGINT`信号给正在执行的进程。

`Ctrl-\` 让进程退出执行，它会发送一个`SIGQUIT`信号给正在执行的进程。

> Note that `^` is how `Ctrl` is displayed when typed in the terminal.

`kill -TERM <PID>`会杀死一个进程，它会发送一个`SIGTERM`signal给进程。

#### Pausing and backgrounding processes

`Ctrl-Z`可暂停一个进程，会发送一个`SIGTSTP`信号给进程。

[`fg`](http://man7.org/linux/man-pages/man1/fg.1p.html) and [`bg`](http://man7.org/linux/man-pages/man1/bg.1p.html)分别可以在前台运行和在后台运行程序（唤醒程序或者启动程序）。

> 可配合`Ctrl-Z`将已经运行的程序暂停，再放到后台运行。

[`jobs`](http://man7.org/linux/man-pages/man1/jobs.1p.html) command lists the unfinished jobs associated with the current terminal session.You can refer to those jobs using their pid (you can use [`pgrep`](http://man7.org/linux/man-pages/man1/pgrep.1.html) to find that out)

> To refer to the last backgrounded job you can use the `$!` special parameter.

`&`作为运行命令后缀，可使命令在后台运行，但是其提示信息仍会使用terminal的STDOUT，也就是说这些信息还是会显示在屏幕上。

注意上面的操作中，运行的程序还是terminal的子程序，也就是说terminal关闭时，也会发送一个`SIGHUP`给子程序，从而结束程序的运行。可以使用[`nohup`](http://man7.org/linux/man-pages/man1/nohup.1.html)忽略该信号，或者针对已经运行的进程使用`disown`。

`SIGKILL`总是可以杀死进程，但是无法杀死其进程的子进程。所以可能产生orphaned children processes。

> You can learn more about these and other signals [here](https://en.wikipedia.org/wiki/Signal_(IPC)) or typing [`man signal`](http://man7.org/linux/man-pages/man7/signal.7.html) or `kill -t`.

##### 例子

```
$ sleep 1000
^Z
[1]  + 18653 suspended  sleep 1000

$ nohup sleep 2000 &
[2] 18745
appending output to nohup.out

$ jobs
[1]  + suspended  sleep 1000
[2]  - running    nohup sleep 2000
# "%" 表示的后面的数字是jobs显示进程的对应数字
$ bg %1
[1]  - 18653 continued  sleep 1000

$ jobs
[1]  - running    sleep 1000
[2]  + running    nohup sleep 2000

$ kill -STOP %1
[1]  + 18653 suspended (signal)  sleep 1000

$ jobs
[1]  + suspended (signal)  sleep 1000
[2]  - running    nohup sleep 2000

# 给第一个进程发了一个SIGHUP信号，自然死掉了
$ kill -SIGHUP %1
[1]  + 18653 hangup     sleep 1000

$ jobs
[2]  + running    nohup sleep 2000

$ kill -SIGHUP %2
# 给第二个进程发了一个SIGHUP信号，但是由于忽略掉了该信号，所以没有死掉
$ jobs
[2]  + running    nohup sleep 2000

$ kill %2
[2]  + 18745 terminated  nohup sleep 2000

$ jobs
```

## 命令行环境

### Terminal Multiplexers

[`tmux`](http://man7.org/linux/man-pages/man1/tmux.1.html)可以方便的在一个terminal上操作多个对话窗口，便捷的令人惊叹。每个`tmux`的`sesstion`都可有`window`,每个`window`可以有多个`plane`。`tmux`创建出来的进程和原本的shell进程分离，所以不受原来进程关闭的影响，不同`session`之间也是独立的。他的强大之处在于方便快捷的切换到不同的`window`，并提供类似于vim的同一个`window`不同`plane`的排列方式。

（非常非常的令人惊喜，噢立给！）

`tmux` expects you to know its keybindings, and they all have the form `<C-b> x` where that means (1) press `Ctrl+b`, (2) release `Ctrl+b`, and then (3) press `x`. `tmux` has the following hierarchy of objects:

- **Sessions**

  \- a session is an independent workspace with one or more windows

  - `tmux` starts a new session.
  - `tmux new -s NAME` starts it with that name.
  - `tmux ls` lists the current sessions
  - Within `tmux` typing `<C-b> d` detaches the current session
  - `tmux a` attaches the last session. You can use `-t` flag to specify which

- Windows

  \- Equivalent to tabs in editors or browsers, they are visually separate parts of the same session

  - `<C-b> c` Creates a new window. To close it you can just terminate the shells doing `<C-d>`
  - `<C-b> N` Go to the *N* th window. Note they are numbered
  - `<C-b> p` Goes to the previous window
  - `<C-b> n` Goes to the next window
  - `<C-b> ,` Rename the current window
  - `<C-b> w` List current windows

- Panes

  \- Like vim splits, panes let you have multiple shells in the same visual display.

  - `<C-b> "` Split the current pane horizontally
  - `<C-b> %` Split the current pane vertically
  - `<C-b> <direction>` Move to the pane in the specified *direction*. Direction here means arrow keys.
  - `<C-b> z` Toggle zoom for the current pane
  - `<C-b> [` Start scrollback. You can then press `<space>` to start a selection and `<enter>` to copy that selection.
  - `<C-b> <space>` Cycle through pane arrangements.

For further reading, [here](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) is a quick tutorial on `tmux` and [this](http://linuxcommand.org/lc3_adv_termmux.php) has a more detailed explanation that covers the original `screen` command. You might also want to familiarize yourself with [`screen`](http://man7.org/linux/man-pages/man1/screen.1.html), since it comes installed in most UNIX systems.

### Aliases

`alias` 提供了将命令行替换为一个别名的功能。

> 赋值”=”旁中不可有空格

```
# Make shorthands for common flags
alias ll="ls -lh"

# Save a lot of typing for common commands
alias gs="git status"
alias gc="git commit"
alias v="vim"

# Save you from mistyping
alias sl=ls

# Overwrite existing commands for better defaults
alias mv="mv -i"           # -i prompts before overwrite
alias mkdir="mkdir -p"     # -p make parent dirs as needed
alias df="df -h"           # -h prints human readable format

# Alias can be composed
alias la="ls -A"
alias lla="la -l"

# To ignore an alias run it prepended with \
\ls
# Or disable an alias altogether with unalias
unalias la

# To get an alias definition just call it with alias
alias ll
# Will print ll='ls -lh'
```

> Note that aliases do not persist shell sessions by default. To make an alias persistent you need to include it in shell startup files, like `.bashrc` or `.zshrc`, which we are going to introduce in the next section.

### Dotfiles

Dotfiles就是文件名前面带点的文件，即隐藏文件。

For `bash`, editing your `.bashrc` or `.bash_profile` will work in most systems. Here you can include commands that you want to run on startup, like the alias we just described or modifications to your `PATH` environment variable. In fact, many programs will ask you to include a line like `export PATH="$PATH:/path/to/program/bin"` in your shell configuration file so their binaries can be found.

Some other examples of tools that can be configured through dotfiles are:

- `bash` - `~/.bashrc`, `~/.bash_profile`
- `git` - `~/.gitconfig`
- `vim` - `~/.vimrc` and the `~/.vim` folder
- `ssh` - `~/.ssh/config`
- `tmux` - `~/.tmux.conf`

Dotfiles文件管理是使用版本管理工具方便快捷地管理多个Dotfils。只需几个命令，就能在一台新机子上安装和以前一模一样的文件和软件，真是诱惑。[资源](https://dotfiles.github.io/bootstrap/)、

> 现在暂时不尝试

[![image-20200526182325028](http://static.come2rss.xyz/image-20200526182325028.png)](http://static.come2rss.xyz/image-20200526182325028.png)

[image-20200526182325028](http://static.come2rss.xyz/image-20200526182325028.png)



#### SSH

[这内容是真的丰富](https://missing.csail.mit.edu/2020/command-line/)

## Dubugging and Profiling

[明天继续吧](https://missing.csail.mit.edu/2020/debugging-profiling/)

