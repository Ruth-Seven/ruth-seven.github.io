---
title: shell命令笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Linux
date: 2020-08-07 13:19:34
tags:
---





## [Shell Tools and Scripting](https://missing.csail.mit.edu/2020/shell-tools/)

> [前面部分参考课程](https://missing.csail.mit.edu/2020/shell-tools/)

## 简单规则

**赋值：**`foo=bar` 赋值语句中不可添加空格

<!-- more -->

**`"`和`'`的区别：**Strings in bash can be defined with `'` and `"` delimiters but they are **not equivalent.** Strings delimited with `'` are literal strings and will not substitute variable values whereas `"` delimited strings will.

```
foo=bar
echo "$foo"
# prints bar
echo '$foo'
# prints $foo
```

**函数体定义：**As with most programming languages, bash supports control flow techniques including `if`, `case`, `while` and `for`. Similarly, `bash` has functions that take arguments and can operate with them. Here is an example of a **function** that creates a directory and `cd`s into it.

```
mcd () {
    mkdir -p "$1"
    cd "$1"
}
```

**变量名定义：**Here `$1` is the first argument to the script/function. Unlike other scripting languages, bash uses a variety of special variables to refer to **arguments, error codes and other relevant variables**. Below is a list of some of them. A more comprehensive list can be found [here](https://www.tldp.org/LDP/abs/html/special-chars.html).

- `$0` - Name of the script
- `$1` to `$9` - Arguments to the script. `$1` is the first argument and so on.
- `$@` - All the arguments
- `$#` - Number of arguments
- `$?` - Return code of the previous command
- `$$` - Process Identification number for the current script
- `!!` - Entire last command, including arguments. A common pattern is to execute a command only for it to fail due to missing permissions, then you can quickly execute it with sudo by doing `sudo !!`
- `$_` - Last argument from the last command. If you are in an interactive shell, you can also quickly get this value by typing `Esc` followed by `.`

Commands will often return output using `STDOUT`, errors through `STDERR` and a Return Code to report errors in a more script friendly manner. Return code or exit status is the way scripts/commands have to communicate how execution went. **A value of 0 usually means everything went OK,** anything different from 0 means an error occurred.

**神奇的脚本符号：**

`false || echo "opes its false"` `||`语句会在第一个命令执行失败后执行第二条。

The `true` program will always have a 0 return code and the `false` command will always have a 1 return code.

> 注意仅当返回值为`0`时命令

`true && echo "Things went well"` 那就是仅在第一条命令执行成功后，第二条命令才会继续执行

`command1 ; command2` 就是无论如何都会按顺序执行两条命令

`!!` 一个神奇的命令，可以获取上一条运行过的完整的命令，可以使用在再次调用Sudo上，可用tap或者enter获取。

`foo=$(pwd)` （*command substitution*）等号两边不可加空格，因为他不是命令。其次`$(pwd)`是获取命令的返回值的意思。再其次，`echo $foo`才能打印出变量`$foo`的结果。

`<( CMD )`(*process substitution*), will execute `CMD` and place the output in a temporary file and substitute the `<()` with that file’s name. This is useful when commands expect values to be passed by file instead of by STDIN. For example, `diff <(ls foo) <(ls bar)` will show differences between files in dirs `foo` and `bar`.

**Wildcards** - Whenever you want to perform some sort of wildcard matching you can use `?` and `*` to match one or any amount of characters respectively. For instance, given files `foo`, `foo1`, `foo2`, `foo10` and `bar`, the command `rm foo?` will delete `foo1` and `foo2` whereas `rm foo*` will delete all but `bar`.

**Curly braces `{}`** - Whenever you have a common substring in a series of commands you can use curly braces for bash to expand this automatically. This comes in very handy when moving or converting files.

```
# Globbing techniques can also be combined
mv *{.py,.sh} folder
# Will move all *.py and *.sh files

mkdir foo bar
# This creates files foo/a, foo/b, ... foo/h, bar/a, bar/b, ... bar/h
touch {foo,bar}/{a..h}
touch foo/x bar/y
```

### 例子

,`grep` for the string `foobar` and append it to the file as a comment if it’s not found.

```
#!/bin/bash

echo "Starting program at $(date)" # Date will be substituted

echo "Running program $0 with $# arguments with pid $$"

for file in $@; do
    grep foobar $file > /dev/null 2> /dev/null
    # When pattern is not found, grep has exit status 1
    # We redirect STDOUT and STDERR to a null register since we do not care about them
    if [[ $? -ne 0 ]]; then
        echo "File $file does not have any foobar, adding one"
        echo "# foobar" >> "$file"
    fi
done
```

In the comparison we tested whether `$?` was not equal to 0. Bash implements many comparisons of this sort, you can find a detailed list in the manpage for [`test`](http://man7.org/linux/man-pages/man1/test.1.html). When performing comparisons in bash try to use double brackets `[[ ]]` in favor of simple brackets `[ ]`. Chances of making mistakes are lower although it won’t be portable to `sh`. A more detailed explanation can be found [here](http://mywiki.wooledge.org/BashFAQ/031).

**shell检查工具：**Writing `bash` scripts can be tricky and unintuitive. There are tools like [shellcheck](https://github.com/koalaman/shellcheck) that will help you find out errors in your sh/bash scripts.

**scripts：**

Python脚本使用[shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))（下面例子中的`#!`开头的句子）来确定Python脚本语言的执行解释器。更灵活的写法是使用`env`命令，比如`#!/usr/local/bin/env python`

```
#!/usr/local/bin/python
import sys
for arg in reversed(sys.argv[1:]):
    print(arg)
```

Some differences between shell functions and scripts that you should keep in mind are:

- 函数定义以后就会载入，执行时无需再载入，速度快。
- 函数可以在当前shell环境执行，但是脚本运行在他们的进程中；所以函数可以改变环境变量，比如进入目录，然而脚本不能。Scripts will be passed by value environment variables that have been exported using [`export`](http://man7.org/linux/man-pages/man1/export.1p.html)
- As with any programming language functions are a powerful construct to achieve modularity, code reuse and clarity of shell code. Often shell scripts will include their own function definitions.

## Shell Tools

### 命令帮助

```
-h`或者`-help
man command
```

[TLDR pages](https://tldr.sh/) are a nifty complementary solution that focuses on giving example use cases of a command so you can quickly figure out which options to use. （推荐！）

### Finding files

[`find`](http://man7.org/linux/man-pages/man1/find.1.html) 即时查找文件，强大的文本属性描述，可支持对文件执行命令。

```
# Find all directories named src
find . -name src -type d
# Find all python files that have a folder named test in their path
find . -path '**/test/**/*.py' -type f
# Find all files modified in the last day
find . -mtime -1
# Find all zip files with size in range 500k to 10M
find . -size +500k -size -10M -name '*.tar.gz'
# Delete all files with .tmp extension
find . -name '*.tmp' -exec rm {} \;
# Find all PNG files and convert them to JPG
find . -name '*.png' -exec convert {} {.}.jpg \;
```

在数据库支持下的文件搜索程序，速度更快，但是由于数据库更新频率限制，可能结果不完整。 `locate` uses a database that is updated using [`updatedb`](http://man7.org/linux/man-pages/man1/updatedb.1.html). In most systems `updatedb` is updated daily via [`cron`](http://man7.org/linux/man-pages/man8/cron.8.html). Therefore one trade-off between the two is speed vs freshness.

A more in depth comparison between `find` and `locate` can be found [here](https://unix.stackexchange.com/questions/60205/locate-vs-find-usage-pros-and-cons-of-each-other).

### Finding code

[`grep`](http://man7.org/linux/man-pages/man1/grep.1.html), a generic tool for matching patterns from the input text. It is an incredibly valuable shell tool and we will cover it more in detail during the data wrangling lecture.

`-C` for getting **C**ontext（上下文） around the matching line

`-v` for in**v**erting the match, i.e. print all lines that do **not** match the pattern.

`-R` since it will **R**ecursively go into directories and look for text files for the matching string.

其他`grep`的升级版 [ack](https://beyondgrep.com/), [ag](https://github.com/ggreer/the_silver_searcher) and [rg](https://github.com/BurntSushi/ripgrep). All of them are fantastic but pretty much cover the same need. For now I am sticking with ripgrep (`rg`) given how fast and intuitive it is. Some examples:

```
# Find all python files where I used the requests library
rg -t py 'import requests'
# Find all files (including hidden files) without a shebang line
rg -u --files-without-match "^#!"
# Find all matches of foo and print the following 5 lines
rg foo -A 5
# Print statistics of matches (# of matched lines and files )
rg --stats PATTERN
```

Note that as with `find`/`fd`, it is important that you know that these problems can be quickly solved using one of these tools, while **the specific tools you use are not as important**.

### Finding shell commands

up arrow（方向向上键）可以查找历史命令

`history` ：可以显示运行过的命令，可以配合`grep`使用，如 `history | grep find` will print commands with the substring “find”.

`Ctrl+R` ：perform backwards search through your history.`zsh`也可以使用上下方向键来搜索。`fzf`提供更强大的模糊搜索命令功能。可见[fzf](https://github.com/junegunn/fzf/wiki/Configuring-shell-key-bindings#ctrl-r)、[zsh](https://github.com/zsh-users/zsh-history-substring-search)。

`fish`: [fish](https://fishshell.com/) shell, this feature dynamically **autocompletes** your current shell command with the most recent command that you typed that shares a common prefix with it. It can be enabled in [zsh](https://github.com/zsh-users/zsh-autosuggestions) and it is a great quality of life trick for your shell.

消除敏感信息：If you make the mistake of not adding the leading space you can always manually remove the entry by editing your `.bash_history` or `.zhistory`.

### Directory Navigation

`fasd`: 支持将命令重命名，支持使用文件名的子串并填充为完整文件。

[`fasd`](https://github.com/clvv/fasd) Fasd ranks files and directories by [*frecency*](https://developer.mozilla.org/en/The_Places_frecency_algorithm), that is, by both *frequency* and *recency*. The most straightforward use is *autojump* which adds a `z` command that you can use to quickly `cd` using a substring of a *frecent* directory. E.g. if you often go to `/home/user/files/cool_project` you can simply `z cool` to jump there.

More complex tools exist to quickly get an overview of a directory structure [`tree`](https://linux.die.net/man/1/tree), [`broot`](https://github.com/Canop/broot) or even full fledged file managers like [`nnn`](https://github.com/jarun/nnn) or [`ranger`](https://github.com/ranger/ranger)

## shell学习笔记

基础和变量



```
#!/bin/bash

# string , variable 
readonly your="Ruth_name" #readonly

# unset your:delete 'your'

#echo
echo "Hi Guys!" "Welcome to my world!"


# this a variable
name1="HU, hahahaha"

# string :strcat;
echo "$name1:"${name1}"!"

# string len 
echo ${#name1}

# string substring
echo `expr index "${name1}" ha`

# string substring
string_cat="aaaaaaaaaaaaa"
string_cat=${string_cat:1:5}
echo $string_cat

###########################
#array 
array_name=(1 2 3 4 5 6)
array_name[7]=7
echo ${array_name[7]}
# 取得数组元素的个数
length=${#array_name[@]}
length=${#array_name[*]}
# 取得数组单个元素的长度
lengthn=${#array_name[n]}

######################
  
:<<EOF
注释内容...
EOF

#########################
a=10;
b=20;
val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"
#乘号(*)前边必须加反斜杠(\)才能实现乘法运算；
val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"
#条件表达式要放在方括号之间，并且要有空格，例如: [$a==$b] 是错误的，必须写成 [ $a == $b ]
if [ $a == $b ]
then
   echo "a 等于 b"
fi
if [ $a != $b ]
then
   echo "a 不等于 b"
fi

if [ $a -eq $b ]
then
   echo "$a -eq $b : a 等于 b"
else
   echo "$a -eq $b: a 不等于 b"
fi
if [ $a -ne $b ]
then
   echo "$a -ne $b: a 不等于 b"
else
   echo "$a -ne $b : a 等于 b"
fi
if [ $a -gt $b ]
then
   echo "$a -gt $b: a 大于 b"
else
   echo "$a -gt $b: a 不大于 b"
fi
if [ $a -lt $b ]
then
   echo "$a -lt $b: a 小于 b"
else
   echo "$a -lt $b: a 不小于 b"
fi
if [ $a -ge $b ]
then
   echo "$a -ge $b: a 大于或等于 b"
else
   echo "$a -ge $b: a 小于 b"
fi
if [ $a -le $b ]
then
   echo "$a -le $b: a 小于或等于 b"
else
   echo "$a -le $b: a 大于 b"
fi
```

## 逻辑运算

```
#!/bin/bash
#----------------------------导论----------------------
:<<EOF
Shell 和其他编程语言一样，支持多种运算符，包括：

    算数运算符
    关系运算符
    布尔运算符
    字符串运算符
    文件测试运算符

原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr，expr 最常用。

expr 是一款表达式计算工具，使用它能完成表达式的求值操作。

例如，两个数相加(注意使用的是反引号 ` 而不是单引号 ')：
EOF

val=`expr 2 + 2`
echo "两数之和为 : $val"
#表达式和运算符之间要有空格，例如 2+2 是不对的，必须写成 2 + 2，这与我们熟悉的大多数编程语言不一样。
#完整的表达式要被 ` ` 包含，注意这个字符不是常用的单引号，在 Esc 键下边。
#----------------------------运算----------------------
:<<EOF
+ 	加法 	`expr $a + $b` 结果为 30。
- 	减法 	`expr $a - $b` 结果为 -10。
* 	乘法 	`expr $a \* $b` 结果为  200。
/ 	除法 	`expr $b / $a` 结果为 2。
% 	取余 	`expr $b % $a` 结果为 0。
= 	赋值 	a=$b 将把变量 b 的值赋给 a。
== 	相等。用于比较两个数字，相同则返回 true。 	[ $a == $b ] 返回 false。
!= 	不相等。用于比较两个数字，不相同则返回 true。 	[ $a != $b ] 返回 true。
EOF
a=10
b=20

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

#----------------------------关系运算符----------------------
:<<EOF
 关系运算符只支持数字，不支持字符串，除非字符串的值是数字。

下表列出了常用的关系运算符，假定变量 a 为 10，变量 b 为 20：
运算符 	说明 	举例
-eq 	检测两个数是否相等，相等返回 true。 	[ $a -eq $b ] 返回 false。
-ne 	检测两个数是否不相等，不相等返回 true。 	[ $a -ne $b ] 返回 true。
-gt 	检测左边的数是否大于右边的，如果是，则返回 true。 	[ $a -gt $b ] 返回 false。
-lt 	检测左边的数是否小于右边的，如果是，则返回 true。 	[ $a -lt $b ] 返回 true。
-ge 	检测左边的数是否大于等于右边的，如果是，则返回 true。 	[ $a -ge $b ] 返回 false。
-le 	检测左边的数是否小于等于右边的，如果是，则返回 true。 	[ $a -le $b ] 返回 true。



布尔运算符

下表列出了常用的布尔运算符，假定变量 a 为 10，变量 b 为 20：
运算符 	说明 	举例
! 	非运算，表达式为 true 则返回 false，否则返回 true。 	[ ! false ] 返回 true。
-o 	或运算，有一个表达式为 true 则返回 true。 	[ $a -lt 20 -o $b -gt 100 ] 返回 true。
-a 	与运算，两个表达式都为 true 才返回 true。 	[ $a -lt 20 -a $b -gt 100 ] 返回 false。

逻辑运算符

以下介绍 Shell 的逻辑运算符，假定变量 a 为 10，变量 b 为 20:
运算符 	说明 	举例
&& 	逻辑的 AND 	[[ $a -lt 100 && $b -gt 100 ]] 返回 false
|| 	逻辑的 OR 	[[ $a -lt 100 || $b -gt 100 ]] 返回 true

字符串运算符

下表列出了常用的字符串运算符，假定变量 a 为 "abc"，变量 b 为 "efg"：
运算符 	说明 	举例
= 	检测两个字符串是否相等，相等返回 true。 	[ $a = $b ] 返回 false。
!= 	检测两个字符串是否相等，不相等返回 true。 	[ $a != $b ] 返回 true。
-z 	检测字符串长度是否为0，为0返回 true。 	[ -z $a ] 返回 false。
-n 	检测字符串长度是否为0，不为0返回 true。 	[ -n "$a" ] 返回 true。
str 	检测字符串是否为空，不为空返回 true。 	[ $a ] 返回 true。


文件测试运算符

文件测试运算符用于检测 Unix 文件的各种属性。

属性检测描述如下：
操作符 	说明 	举例
-b file 	检测文件是否是块设备文件，如果是，则返回 true。 	[ -b $file ] 返回 false。
-c file 	检测文件是否是字符设备文件，如果是，则返回 true。 	[ -c $file ] 返回 false。
-d file 	检测文件是否是目录，如果是，则返回 true。 	[ -d $file ] 返回 false。
-f file 	检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 	[ -f $file ] 返回 true。
-g file 	检测文件是否设置了 SGID 位，如果是，则返回 true。 	[ -g $file ] 返回 false。
-k file 	检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。 	[ -k $file ] 返回 false。
-p file 	检测文件是否是有名管道，如果是，则返回 true。 	[ -p $file ] 返回 false。
-u file 	检测文件是否设置了 SUID 位，如果是，则返回 true。 	[ -u $file ] 返回 false。
-r file 	检测文件是否可读，如果是，则返回 true。 	[ -r $file ] 返回 true。
-w file 	检测文件是否可写，如果是，则返回 true。 	[ -w $file ] 返回 true。
-x file 	检测文件是否可执行，如果是，则返回 true。 	[ -x $file ] 返回 true。
-s file 	检测文件是否为空（文件大小是否大于0），不为空返回 true。 	[ -s $file ] 返回 true。
-e file 	检测文件（包括目录）是否存在，如果是，则返回 true。 	[ -e $file ] 返回 true。

实例
变量 file 表示文件"/var/www/runoob/test.sh"，它的大小为100字节，具有 rwx 权限。下面的代码，将检测该文件的各种属性：

#!/bin/bash
EOF
```

## 函数

```
:<<EOF
shell 函数
linux shell 可以用户定义函数，然后在shell脚本中可以随便调用。

shell中函数的定义格式如下：

[ function ] funname [()]

{

    action;

    [return int;]

}
1.可以带function fun() 定义，也可以直接fun() 定义,不带任何参数。
2、参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255)


#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
funWithReturn
echo "输入的两个数字之和为 $? !"
#函数返回值在调用该函数后通过 $? 来获得。


#------------------------------------函数参数
在Shell中，调用函数时可以向其传递参数。
在函数体内部，通过 $n 的形式来获取参数的值，例如，$1表示第一个参数，$2表示第二个参数...

带参数的函数示例：

#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73

注意，$10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数。
另外，还有几个特殊字符用来处理参数：

参数处理	说明
$#	传递到脚本的参数个数
$*	以一个单字符串显示所有向脚本传递的参数
$$	脚本运行的当前进程ID号
$!	后台运行的最后一个进程的ID号
$@	与$*相同，但是使用时加引号，并在引号中返回每个参数。
$-	显示Shell使用的当前选项，与set命令功能相同。
$?	显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。


EOF
```

## 特殊函数

```
# ----------------------echo
#这里的双引号完全可以省略，以下命令与上面实例效果一致：
echo "It is a test"

echo It is a test
#2.显示转义字符
echo "\"It is a test\""
"It is a test"

#--------------------read
#read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量
:<<EOF
read name 
echo "$name It is a test"
以上代码保存为 test.sh，name 接收标准输入的变量，结果将是:

[root@www ~]# sh test.sh
OK                     #标准输入
OK It is a test        #输出
EOF
#------------------换行
#4.显示换行
echo -e "OK! \n" # -e 开启转义
echo "It is a test"

#5.显示不换行

echo -e "OK! \c" # -e 开启转义 \c 不换行
echo "It is a test"


#--------------结果定向至文件
echo "It is a test" > myfile

#---原样输出字符串，不进行转义或取变量(用单引号)
echo '$name\"'


#----显示命令执行结果
echo `date`
#注意： 这里使用的是反引号 `, 而不是单引号 '。

#-----------结果将显示当前日期

#Thu Jul 24 10:08:46 CST 2014
 
 
#------------------------------------------------
#------------------------------------------------
#------------------------------------------------
#------------------------------------------------
#------------------------------------------------#------------------------------------------------

# ------------------printf-----------------------
:<<EOF
rintf 命令的语法：
printf  format-string  [arguments...]
参数说明：
format-string: 为格式控制字符串
arguments: 为参数列表。
EOF


printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg  
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234 
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543 
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876

:<<EOF
%s %c %d %f都是格式替代符

%-10s 指一个宽度为10个字符（-表示左对齐，没有则表示右对齐），任何字符都会被显示在10个字符宽的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来。

%-4.2f 指格式化为小数，其中.2指保留2位小数。

\a	警告字符，通常为ASCII的BEL字符
\b	后退
\c	抑制（不显示）输出结果中任何结尾的换行字符（只在%b格式指示符控制下的参数字符串中有效），而且，任何留在参数里的字符、任何接下来的参数以及任何留在格式字符串中的字符，都被忽略
\f	换页（formfeed）
\n	换行
\r	回车（Carriage return）
\t	水平制表符
\v	垂直制表符
\\	一个字面上的反斜杠字符
\ddd	表示1到3位数八进制值的字符。仅在格式字符串中有效
\0ddd	表示1到3位的八进制值字符
EOF
 

 
 
#------------------------------------------------
#------------------------------------------------
#------------------------------------------------
#------------------------------------------------
#------------------------------------------------#------------------------------------------------

# ------------------test-----------------------
:<<EOF
Shell中的 test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。

数值测试
参数	说明
-eq	等于则为真
-ne	不等于则为真
-gt	大于则为真
-ge	大于等于则为真
-lt	小于则为真
-le	小于等于则为真
EOF



num1=100
num2=100
if test $[num1] -eq $[num2]
then
    echo '两个数相等！'
else
    echo '两个数不相等！'
fi

#代码中的 [] 执行基本的算数运算，
a=5
b=6

result=$[a+b] # 注意等号两边不能有空格
echo "result 为： $result"
:<<EOF

字符串测试
参数	说明
=	等于则为真
!=	不相等则为真
-z 字符串	字符串的长度为零则为真
-n 字符串	字符串的长度不为零则为真
实例演示：

num1="ru1noob"
num2="runoob"
if test $num1 = $num2
then
    echo '两个字符串相等!'
else
    echo '两个字符串不相等!'
fi


文件测试
参数	说明
-e 文件名	如果文件存在则为真
-r 文件名	如果文件存在且可读则为真
-w 文件名	如果文件存在且可写则为真
-x 文件名	如果文件存在且可执行则为真
-s 文件名	如果文件存在且至少有一个字符则为真
-d 文件名	如果文件存在且为目录则为真
-f 文件名	如果文件存在且为普通文件则为真
-c 文件名	如果文件存在且为字符型特殊文件则为真
-b 文件名	如果文件存在且为块特殊文件则为真


另外，Shell还提供了与( -a )、或( -o )、非( ! )三个逻辑操作符用于将测试条件连接起来，其优先级为："!"最高，"-a"次之，"-o"最低。例如：

cd /bin
if test -e ./notFile -o -e ./bash
then
    echo '至少有一个文件存在!'
else
    echo '两个文件都不存在'
fi
EOF
```

## 重定向

```
:<<EOF
shell 函数
linux shell 可以用户定义函数，然后在shell脚本中可以随便调用。

shell中函数的定义格式如下：

[ function ] funname [()]

{

    action;

    [return int;]

}
1.可以带function fun() 定义，也可以直接fun() 定义,不带任何参数。
2、参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255)


#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
funWithReturn
echo "输入的两个数字之和为 $? !"
#函数返回值在调用该函数后通过 $? 来获得。


#------------------------------------函数参数
在Shell中，调用函数时可以向其传递参数。
在函数体内部，通过 $n 的形式来获取参数的值，例如，$1表示第一个参数，$2表示第二个参数...

带参数的函数示例：

#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73

注意，$10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数。
另外，还有几个特殊字符用来处理参数：

参数处理	说明
$#	传递到脚本的参数个数
$*	以一个单字符串显示所有向脚本传递的参数
$$	脚本运行的当前进程ID号
$!	后台运行的最后一个进程的ID号
$@	与$*相同，但是使用时加引号，并在引号中返回每个参数。
$-	显示Shell使用的当前选项，与set命令功能相同。
$?	显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。


EOF
```

## 监控系统信息

```
#!/bin/bash
#Get system infomation
(
sys_time=$(date +"%Y-%m-%d %k:%M:%S")
#os_version=$(lsb_release -a | sed -n '/Description/p' | awk -F '[:]' '{print $2}' | sed 's/^[[:space:]]*//')
os_version=$(cat /etc/issue | grep Linux)
kernel_release=$(uname -r)
netcard_num=$(ifconfig -a | grep eth | wc -l)
echo "[public_info]"
echo -e "sys_time=$sys_time\t#系统时间"
echo -e "os_version=$os_version\t#操作系统版本"
echo -e "kernel-release=$kernel_release\t#内核版本"

#########NETCADE INFOMATION##########
echo 
echo "[netcard_info]"
echo "netcard_num=$netcard_num"
echo "#网卡名字|IP|MAC|网卡驱动|网卡速率|网卡发送流量(bytes)|网卡接收流量(bytes)|网卡总流量(bytes)"
for((n=0;n<$netcard_num;n++))
do
Receive_byte=$(cat /proc/net/dev | grep eth$n | awk '{print$2}')
Send_byte=$(cat /proc/net/dev | grep eth$n | awk '{print$10}')
echo "netcard_$((n+1))=eth$n|\
$(ifconfig eth$n | grep "inet addr" | awk '{print$2}' | awk -F'[:]' '{print$2}')|\
$(ifconfig -a | grep eth$n | awk '{print$5}')|\
$(ethtool eth$n | grep Speed | awk '{print$2}' | sed 's/^[[:space:]]*//')|\
${Receive_byte}|\
${Send_bytei}|\
$(($Receive_byte + $Send_byte))"
done

##########CPU INFOMATION##############
cpu_phical_count=$(cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l)
cpu_model=$(cat /proc/cpuinfo | grep "model name" | uniq | awk -F'[:]' '{print$2}')
cpu_core_num=$(cat /proc/cpuinfo | grep cores | uniq | awk -F'[:]' '{print $2}' | sed 's/^[[:space:]]*//')
cpu_process_num=$(cat /proc/cpuinfo | grep process | wc -l)
cpu_frequency=$(cat /proc/cpuinfo |grep MHz|uniq | awk -F'[:]' '{print $2}' | sed 's/^[[:space:]]*//')
cache_size=$(cat /proc/cpuinfo | grep "cache size" | uniq | awk -F'[:]' '{print$2}')
cpu_idle=$(mpstat | grep all | awk '{print$11}')
cpu_used=$(mpstat | grep all | awk '{print$3}')
echo
echo "[cpu_info]"
echo -e "cpu_model=$cpu_model\t#cpu型号"
echo -e "cpu_core_num=$cpu_core_num\t#cpu核数"
echo -e "cpu_phical_count=$cpu_phical_count\t#cpu个数"
echo -e "cpu_frequendy=$cpu_frequency\t#主频/单个"
echo -e "cache_size=${cache_size}*$cpu_process_num\t#缓存"
echo -e "cpu_idle=${cpu_idle}%\t#空闲率"
echo -e "cpu_used=${cpu_used}%\t#使用率"

###########memeber info###############
echo
echo "[mem_info]"
echo -e "mem_total=$(free -m | grep Mem | awk '{print$2}')\t#总内存"
echo -e "mem_used=$(free -m | grep buffers/cache | awk '{print$3}')\t#已使用"
echo -e "mem_free=$(free -m | grep buffers/cache | awk '{print$4}')\t#可使用"

###########hard info ##################
file_system_num=$(df -Ph | grep / | wc -l)
echo
echo "[hard_info]"
echo "file_system_num=$file_system_num"
echo "#磁盘总容量(单位M)|已用容量(单位M)|可用流量(单位M)|已用百分比（%）|挂载目录"
df -Pm | grep / | awk '{print$2"|"$3"|"$4"|"$5"|"$6}'
exit 0
) >system_infomation.txt
```