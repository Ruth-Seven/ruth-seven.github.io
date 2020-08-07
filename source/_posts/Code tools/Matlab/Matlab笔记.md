---
title: Matlab笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Code tools
  - Matlab
date: 2020-08-07 12:53:36
tags:
---



待学习的内容 [绘图大量的笔记](https://blog.csdn.net/wangcj625/article/details/6287735)

# 常用函数

`disp(Var)` 打印很方便

<!-- more -->

# 数据

## 常量

```
>>a = pi; %pi = pai 
>> disp(sprintf('2 decimals: %0.6f', a)) %字符串拼接和显示
2 decimals: 3.141593
```

:happy:

:kissing_heart:

:carousel_horse:

## **矩阵**

**创建**

逗号和分号的运算起了标志行的作用

```
>> v = [1 2 3]
v =

     1     2     3

>> v  = [1 ; 2; 3;]
v =

     1
     2
     3
>> v = 1:0.1:2
v =

    1.0000    1.1000    1.2000    1.3000    1.4000    1.5000    1.6000    1.7000    1.8000    1.9000    2.0000
```

**常见函数：**

`ones(shape)` `zeroe(shape)` `rand(shape)` `randi(shape)` % shape 代表数字列， 如2，3，5，1。

`randn(shape)` %正态分布的随机数 Gussses rand?

`eye(K)` % 单位矩阵

**矩阵运算：**

常见的有矩阵乘法和矩阵点乘，点除，点方。

matlab不主持类似python的numpy的广播机制，但是仍然支持数字 + 矩阵的模式，同时 不同维度的矩阵无法相加减。

**广播**

只要阵列具有“兼容大小”，就允许在阵列之间进行上述二进制操作。当一个数组中的每个维度正好等于另一个数组中的相同维度，或者等于`1`时，大小被认为是“兼容的”。比如。

```
>> magic(3) + (1:3)
ans =

     9     3     9
     4     7    10
     5    11     5
```

| 描述           | 第一个数组大小 | 第二个数组大小 | 结果大小      |
| :------------- | :------------- | :------------- | :------------ |
| 矢量和标量     | `[3x1]`        | `[1x1]`        | `[3x1]`       |
| 行和列向量     | `[1x3]`        | `[2x1]`        | `[2x3]`       |
| 矢量和二维矩阵 | `[1x3]`        | `[5x3]`        | `[5x3]`       |
| ND和KD阵列     | `[1x3x3]`      | `[5x3x1x4x2]`  | `[5x3x3x4x2]` |

**复制扩展**

`repmat( A , m , n )` : 将向量／矩阵在垂直方向复制为m倍，在水平方向复制为n倍。

**求和以及其他函数**

引出一个matlab与python极为类似的但略有不同的概念，`axis`。常常在函数计算中起到指定运算方向的作用，如axis=1，则计算沿着竖直方向计算。

如`sum(A, axis)`

[![1581927781476](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1581927781476.png)](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1581927781476.png)

[1581927781476](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1581927781476.png)



其他函数 如`mean()` `max()` 也是如此。

## 索引以及选择

matlab的数据索引从1开始。对于矩阵可以使用`[C]`进行矩阵的数据合并，`(C)`进行索引。对于cell元胞可以通过`{}`索引。

**Boolean索引** 是一个非常强大的功能，通过逻辑表达式的组合可以删选出复杂的规则条件下的数据。而矩阵的逻辑运算一般都是扩展到各个元素的，这就方便了通过一个条件判断矩阵来索引出真正数据的操作。

**下标索引** 拿一维矩阵来举例，常见的操作有 单一索引`A(1)`, 范围索引`A(1:end)`, 间隔索引 `A(1:2:end)` , 向量索引`A([1,3,5], :)`。如果其他维度的数据需要索引最好把其他维度索引也写上，不管是不是需要全部索引。（这些索引名字 我自己想的~~ ）:kiss: :kiss:

## 数据管理

```
>> length(A) % give the longest dimension.
>> who % 查看变量
您的变量为:

A    I    a    ans  c    v    w    
>> whos % 查看变量
  Name      Size                   Bytes  Class     Attributes
  A         2x3                       48  double             
  I         4x4                      128  double            

%保存
>> save  test 		% 保存所有变量 当然也可以用laod 载入mat
>> save test2.mat Y % 保存单个变量
>> save test2.txt Y -ascii % save as test(ASCII)
```

## 运算

```
% 乘法
>> A = [1 2 ; 3 4 ; 5 6];
>> B = [2 3 ; 4 5];
>> c = A * B 

c =

    10    13
    22    29
    34    45
    
    
% element-wise operation
% 一个3*1的矩阵和一个3*2的矩阵相乘类似于两个3 * 2的矩阵element-wise乘， 但是只要一个矩阵不是n*1或是1*n，或者两个矩阵维度不一样，那么就会无法element-wise乘。
>> D = A .* c 
D =

    10    26
    66   116
   170   270
   
>> A.^2 % element-wise operation
ans =

     1     4
     9    16
    25    36
>> 1./A % element-wise operation 

ans =

    1.0000    0.5000
    0.3333    0.2500
    0.2000    0.1667
>> v < 3 % every element is judged.

ans =

  1×6 logical 数组

   1   1   0   0   0   0


%% such as log(), abs() and exp() is element-wise opetation too.


%add
>> A + ones(3,2)

ans =

     2     3
     4     5
% 也可直接➕1

>> A + 1

ans =

     2     3
     4     5
     6     7
     
     
%transpose
>> A'

ans =

     1     3     5
     2     4     6
     
     
%max
>> A

A =

     1     2
     3     4
     5     6
>> max(A) % if A is matrix, output is column-wise

ans =

     5     6
     

>> [val, idx] = max([1     2     3     4     7     6])

val =

     7


idx =

     5
     

>> max([1     2     3     4     7     6])

ans =

     7
     
>> R1 = rand(3) % element-wise max

R1 =

    0.4873    0.4805    0.8880
    0.6459    0.1431    0.3434
    0.8356    0.6037    0.5764

>> R2 = rand(3)

R2 =

    0.2988    0.6937    0.2178
    0.3194    0.7549    0.4476
    0.6043    0.2309    0.6584
>> max(R1, R2)

ans =

    0.4873    0.6937    0.8880
    0.6459    0.7549    0.4476
    0.8356    0.6037    0.6584

>> max(A, [], 1) % 1 means that get the max column-wise value. 

ans =

     5     6

>> A

A =

     1     2
     3     4
     5     6

>> max(A, [], 2) % 2 is 

ans =

     2
     4
     6

>> max(A(:))

ans =

     6

>> max(max(A))

ans =

     6
     
     
%%find
>> v
v = 

     1     2     3     4     5     6

>> find(v < 3) % to vector

ans =

     1     2
     
>> M = magic(3) % to matrix 

M =

     8     1     6
     3     5     7
     4     9     2

>> find(M < 7) 

ans =

     2
     3
     4
     5
     7
     9

>> [r, c] = find(M < 7) % anther way to get index

r =

     2
     3
     1
     2
     1
     3


c =

     1
     1
     2
     2
     3
     3
     
     
     
% 其他函数
>> a = [1, 15, 0.5, 2.5]

a =

    1.0000   15.0000    0.5000    2.5000

%sum
>> sum(a)

ans =

    19

A =

     1     2
     3     4
     5     6

>> sum(A,1) % 以列为单位相加

ans =

     9    12

>> sum(A,2) % 以行为单位相加

ans =

     3
     7
    11


>> prod(a)%

ans =

   18.7500

>> floor(a)

ans =

     1    15     0     2

>> ceil(a)

ans =

     1    15     1     3


%flipud
>> sum(sum( flipud(eye(9)) .* magic(9)) ) %矩阵上下翻转

ans =

   369


% identity matrix
>> M = magic(3)

M =

     8     1     6
     3     5     7
     4     9     2

>> N = pinv(M)

N =

    0.1472   -0.1444    0.0639
   -0.0611    0.0222    0.1056
   -0.0194    0.1889   -0.1028

>> N * M

ans =

    1.0000    0.0000   -0.0000
   -0.0000    1.0000    0.0000
    0.0000   -0.0000    1.0000
```

## 字符串

字符串本质来说只是带**字符**的向量，可以进行多种类似向量的操作，比如索引、拼接之类。

### 比较 `strcmp`

`tf = strcmp(s1,s2)` 比较 `s1` 和 `s2`，如果二者相同，则返回 `1` (`true`)，否则返回 `0` (`false`)。如果文本的大小和内容相同，则它们将视为相等。返回结果 `tf` 的数据类型为 `logical`。

### 格式化 `sprintf`

`str = sprintf(formatSpec,A1,...,An)` 使用 `formatSpec` 指定的格式化操作符格式化数组 `A1,...,An` 中的数据，并在 `str` 中返回结果文本。`sprintf` 函数按列顺序格式化 `A1,...,An` 中的值。如果 `formatSpec` 是字符串，则输出 `str` 也是字符串。否则，`str` 是字符向量。

比如

```
formatSpec = 'The array is %dx%d.';
A1 = 2;
A2 = 3;
str = sprintf(formatSpec,A1,A2)
```

### 打印字符串 `fprintf`

直接格式化并打印字符串到显示器上，其中格式方式同`sprintf`。

### 字符串拼接 三种方法

```
方法一：用中括号将str1和str2像矩阵元素一样包含起来：
>> SC=[str1,str2]
方法二：用strcat函数
>> SB=strcat(str1,str2) 
% 其他用途 >> strcat({'Red','Yellow'},{'Green','Blue'})
方法三：利用sprintf函数
>> number=123;
>> STR=sprintf('%s%d',str1,number)
```

# 画图

强大的绘图功能是Matlab的特点之一，Matlab提供了一系列的绘图函数，用户不需要过多的考虑绘图的细节，只需要给出一些基本参数就能得到所需图形，这类函数称为高层绘图函数。此外，Matlab还提供了直接对图形句柄进行操作的低层绘图操作。这类操作将图形的每个图形元素（如坐标轴、曲线、文字等）看做一个独立的对象，系统给每个对象分配一个句柄，可以通过句柄对该图形元素进行操作，而不影响其他部分

## **PLOT**

1. 基本用法： 一组向量对

```
>> plot(t,y);
>> hold on;
>> z = pi * cos(t);
>> plot(t,z);
```

1. 多组向量对

```
%plot函数可以包含若干组向量对，每一组可以绘制出一条曲线。含多个输入参数的plot函数调用格式为：plot(x1，y1，x2，y2，…，xn，yn)
%如下列命令可以在同一坐标中画出3条曲线。
>> x=linspace(0,2*pi,100);
>> plot(x,sin(x),x,2*sin(x),x,3*sin(x))
```

1. 当输入参数有矩阵形式时，配对的x,y按对应的列元素为横坐标和纵坐标绘制曲线，曲线条数等于矩阵的列数

1. 绘图选项

| 线型      | 颜色  | 标记符号 |               |
| :-------- | :---- | :------- | :------------ |
| - 实线    | b蓝色 | . 点     | s 方块        |
| : 虚线    | g绿色 | o 圆圈   | d 菱形        |
| -. 点划线 | r红色 | × 叉号   | ∨朝下三角符号 |
| – 双划线  | c青色 | + 加号   | ∧朝上三角符号 |
|           | m品红 | * 星号   | <朝左三角符号 |
|           | y黄色 |          | >朝右三角符号 |
|           | k黑色 |          | p 五角星      |
|           | w白色 |          | h 六角星      |

1. 坐标控制

   想要精密的控制坐标轴的表现，需要下面多条命令的操作。

```
xlim([2, 46]);%只设定x轴的绘制范围
ylim([0, 132]);%只设定x轴的绘制范围
set(gca,'XTick',[2:2:46]) %改变x轴坐标间隔显示 这里间隔为2
%以上就可以对x轴做很好的控制了，y轴类似。

axis([2,46,0,2]) % axis([xmin,xmax,ymin,ymax])，用这个语句可以对x，y轴的上限与下限绘制范围一起做控制，但是间隔还是要用上面的set来改
```

1. 其他注释

```
xlabel('x name');% x轴名称
ylabel('y name');
legend('xxx'); %线条注释,多条的话: 	    legend('xxx','xxx2','xxx3'）
```

1. 文字注释

`text`可以接受向量化的数据输入，从而同时注释多个点的文字。

```
xt = [-2 2];
yt = [16 -16];
str = {'local max','local min'};
text(xt,yt,str)
```

1. **hold on** 维持画布不变化； **figure** 新开两个figure画板。subplot在同一个窗口上开多个子画板。

```
>> subplot(1,2,1); plot(t,z);
>> subplot(1,2,2); plot(t,y);
>> axis([5 10 0 4]) % X轴范围为[5,10],y轴范围为[0,4];

>> clf - 清除当前图窗窗口
    此 MATLAB 函数 从当前图窗中删除其句柄未隐藏的所有图形对象（即它们的 HandleVisibility 属性设置为 on）。
```

[![img](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1578539038766.png)](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1578539038766.png)

## SCATTER

还是看[官方文档](https://ww2.mathworks.cn/help/matlab/ref/scatter.html?searchHighlight=scatter#btrj9jn-1-c)

## 画圆

```
function [x,y] = circle(R,cx,cy,nb_pts)
%%%%%%%%%%%%%%%%%%%
% 画圆函数
%%%%%%%%%%%%%%%%%%%
alpha=0:pi/nb_pts:2*pi;%角度[0,2*pi]
%R=2;%半径
x=R*cos(alpha)+cx;
y=R*sin(alpha)+cy;
plot(cx,cy,'r+',x,y);
grid on;
axis equal;

end
```

## IMAGESC 涂色

```
>> figure(3)
>> imagesc(magic(15)),colorbar, colormap gray
% imagesc 生成一个对应于矩阵数值和数量的‘像素块’图像
```

[![img](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1578539625571.png)](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1578539625571.png)

# 控制语句

```
for i = 1:10, %这里也可遍历矩阵
w = w +  5;
if( i > 5) break;
end;
end;
>> w
w =

    35

>> if( v == 2)
disp("dsf is the strongest person in the confusing world!")
else v = 0 ;
end;

v =

     3
```

# 函数

```
function [value1, value2] = Function_name(par1, par2)
value1 = 
value2 =
```

# 其他操作

typing ctrl-c to quit the running program.

# 文件操作

## 保存与载入程序数据

非常使用的两个函数，不过我一般只用来保存临时变量。

`save('FILENAME', 'VARIABLES')` `load('FILENAME', 'VARIABLES')` 的括号可以去掉

## Excel文件的导入与导出

```
[num, txt, raw] = xlsread('文件名.xls','工作表', '数据范围')
status = xlswrite(‘filename.xls’, ‘数据’, ‘工作表’, ‘指定区域’)
```

## 混合文本读入（目前可用csv）

一般来说，最难读入是这种文办，数据内容比较复杂，常常带有数字、字符串等内容。

```
textscan(fid, 'format', N, 'param', value);
```

其中，`fid`为文件句柄；`format`为读取格式；`N`表示用该格式读取N次数据；`param`,`value`（可选项）指定分隔符和值对。 N其实也是可选项。

注意：使用`textscan`之前，必须先用`fopen`打开要读入的文件；函数`textread`用法类似。

```
fid=fopen('data6.txt','r');  %打开文件句柄

C=textscan(fid, '%s%s%f32%d8%u%f%f%s%f');  %按格式读入元胞数组C

fclose(fid);  %关闭文件句柄
```

# 向量化编程

[![img](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1578547281323.png)](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1578547281323.png)

可见图中的两个更新公式中，仅有xixi的部分是不同的。把多个xixi座位一个整体，那么就可以得到一个简洁的公式：

[![img](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1578547400047.png)](http://blog.come2rss.xyz/2020/04/26/tools/windows/matlab-note/matlab-note/1578547400047.png)

（图中各个符号的维度如图所示）

## 其他函数

```
%标准差
std
>> help std
std - 标准差

    此 MATLAB 函数 返回 A 沿大小不等于 1 的第一个数组维度的元素的标准差。 如果 A 是观测值的向量，则标准差为标量。 如果 A
    是一个列为随机变量且行为观测值的矩阵，则 S 是一个包含与每列对应的标准差的行向量。
    
%help
>> help mean
mean - 数组的均值

    此 MATLAB 函数 返回 A 沿大小不等于 1 的第一个数组维度的元素的均值。

    M = mean(A)
    M = mean(A,dim)
    M = mean(___,outtype)
    M = mean(___,nanflag)

    另请参阅 median, mode, std, sum, var

    mean 的参考页
    名为 mean 的其他函数

>> M = magic(5);
>> mean(M,1)

ans =

    13    13    13    13    13

>> mean(M,2)

ans =

    13
    13
    13
    13
    13
```

# 高阶操作

## STRING 命令化

主要应对多个重复但无法向量化处理的操作，比如多个不同长度的数据的绘图任务，不可以直接塞给plot一个矩阵完事，会有多与少数据掺杂进去的。

其实现方式是通过eval执行命令的string。eval函数的功能是将字符串转换为matlab可执行语句。

比如重复执行导入随名次变化的名字的mat文件。

```
for i=1:100 
	eval([‘load ’ num2str(i) ‘.mat’]) 
	
end 
% 当然也可以使用 sprintf打印字符串；
```

Note：string中不能含有**’**，也就是说遇到**’**，需要特殊处理比如，

```
% 执行 plot(nii, 'LineWidth', '2');
eval(['plot(n',num2str(ii),char(39),'LineWidth', char(39), ',2');
```

## 像素点级画图

出自Andrew的第四周编程练习PlotPic。

```
function [h, display_array] = displayData(X, example_width)
%DISPLAYDATA Display 2D data in a nice grid
%   [h, display_array] = DISPLAYDATA(X, example_width) displays 2D data
%   stored in X in a nice grid. It returns the figure handle h and the 
%   displayed array if requested.

% Set example_width automatically if not passed in
if ~exist('example_width', 'var') || isempty(example_width) 
	example_width = round(sqrt(size(X, 2)));
end

% Gray Image
colormap(gray);

% Compute rows, cols
[m n] = size(X);
example_height = (n / example_width);

% Compute number of items to display
display_rows = floor(sqrt(m));
display_cols = ceil(m / display_rows);

% Between images padding
pad = 1;

% Setup blank display
% 画板
display_array = - ones(pad + display_rows * (example_height + pad), ...
                       pad + display_cols * (example_width + pad));

% Copy each example into a patch on the display array
curr_ex = 1;
for j = 1:display_rows
	for i = 1:display_cols
		if curr_ex > m, 
			break; 
		end
		% Copy the patch
		
		% Get the max value of the patch
        % 格子作画： reshape改变图片像素排列方式
		max_val = max(abs(X(curr_ex, :)));
		display_array(pad + (j - 1) * (example_height + pad) + (1:example_height), ...
		              pad + (i - 1) * (example_width + pad) + (1:example_width)) = ...
						reshape(X(curr_ex, :), example_height, example_width) / max_val;
		curr_ex = curr_ex + 1;
	end
	if curr_ex > m, 
		break; 
	end
end

% Display Image
% 每个元素代表了一个像素点
h = imagesc(display_array, [-1 1]);

% Do not show axis
axis image off

drawnow;

end
```

# 系统操作

编辑文件: edit file ： 可同时创建文件

## 工作路径

```
your path here')`这条语句就可以把此路径加入到matlab工作路径中。


比如一些基本的 `cd`, `pwd`, `ls`都可以使用。

​```matlab
> > pwd % give the path where works
ans =


```

‘G:\Matlab\bin’
​```

> > cd ‘H:\重要文件\在校学习比赛\学习资料\机器学习\机器学习 Andrew’
> > ls

Linear Regression with multiple variables.md
2 Linear Regression with multiple variables.assets

```
# 错误笔记

$n*1$的矢量相加或相减与一个$1*n$的矢量得到的确实一个$n*n$的矩阵！

## 

# 快捷键



MATLAB 命令栏显示处理的常用命令

清屏：clc

紧凑显示格式：format compact

宽松显示格式：format loose

数据高精度显示：format longG

数据低精度显示：format short





**编辑器窗口（Editor）下的常用快捷键：**
自动对齐程序（整理缩进）-自动整理代码 用鼠标选中代码行，按Ctrl + I
**快速注释**代码段 拖动鼠标选中需要注释的代码行，按Ctrl + R
快速取消注释代码段 拖动鼠标选中已经注释的代码行，按Ctrl + T
撤销改动 Ctrl + Z
取消撤销（撤销过多时使用） Ctrl + Y
多行代码增加缩进（代码段右移） 选中代码段，按   Tab键   或   Ctrl + ]
多行代码减少缩进（代码段左移） 选中代码段，按   Shift+Tab键   或   Ctrl + [
自动补全命令（记不全函数名时使用） 输入函数的前几个字母，再按Tab
查找或替换变量名、函数名 Ctrl + F
关闭当前的程序文本（.m）文件 Ctrl + W
在Editor窗体中**切换**
Ctrl + PageUp/PageDown

Ctrl+PgUp表示编辑器窗口向左切换文件

Ctrl+PgDn表示编辑器窗口向右切换文件

 Ediotor\命令行**窗口切换**：ctrl+Tab

**代码调试常用快捷键：**
运行 F5可保存并直接运行程序
执行选中代码段 F9
单步执行 F10
F11 表示step in，即当遇见子函数时，使用此快捷键，进入函数内部
Shift + F11 表示step out，即使用此快捷键，执行完子函数的剩余程序，并跳出子函数
设置或取消断点的方法有两种
(1) 在要设置断点的行左侧的-处单击；

(2) 可按F12设置断点。

直接跳至某行 Ctrl + G， 
强制中断程序的运行 Ctrl + C
命令窗口（Command Window）下的常用快捷键与命令：
再现历史命令
上下光标键↑↓   ，在命令窗口中，上下光标键可以调用Matlab最近使用过的历史命令，便于快速重新执行。 如果输入命令的前几个字母，再使用光标键，则只会选择以这些字母开始的命令。 上下箭头寻找此前和此后输入的命令，每次一条。

快速退出MATLAB Ctrl + Q
清除输入的命令 Esc
将光标处至结尾之间的代码删除 Ctrl + K
what 显示当前工作路径中的所有代码文件
type 代码文件名 显示代码文件的内容
edit 启动编辑器，并新建一个空白文件
edit 代码文件名 打开相应代码文件
whatsnew 列出MATLAB新版本更新的内容


**切换窗口快捷键：**
Ctrl+0 命令行窗口（Command Window）
Ctrl + Shift + 0 编辑器窗口（Editor）
Ctrl + 1 历史命令窗口（Command History）
Ctrl + 2 当前工作窗口（Current Folder）
Ctrl + 3

**工作空间（Workspace）**

初学者要把下面的基本使用规则，牢记于心：

1. 输入时，标点必须是英文状态下的
2. 大多数情况下，MATLAB对空格不予处理
3. 小括号代表运算级别，中括号用于生成矩阵，大括号用于构成单元数组
4. 分号  ;  的作用：不显示运算结果（抑制输出），但对图形窗口不起作用。分号也用于区分行。
5. 逗号  ,  的作用：函数参数分隔符，也用于区分行，显示运算结果，当然不加标点也显示运算结果
6. 冒号  :  多用于数组
7. 续行号  ...  不能放在等号后面使用，不能放在变量名中间使用，起作用时默认显蓝色
8. 双引号 'string' 是字符串的标识符
9. 感叹号  !  用于调用操作系统运算
10. 百分号  %  是注释符号，对于百分号后面直到行末的语句，matlab跳过执行。另外还可用于代码块注释，即对多行代码一次注释，  格式为：（注意%{ 和%}都要单独成行
11. 乘号 * 总是不能省略的，除了表示复数，比如2+3i时可以省略
12. 除号有 / 或 \ ，它两个的关系是：a除以b表示为a/b，或 b\a
13. 等号 = 用于赋值
14. == 表示数学意义上的等号

15. 主窗口（Command Window）里面，输入时，换行用Shift+Enter

16. 主窗口（Command Window）里面，运行程序，执行命令用Enter

17. 矩阵中用圆括号表示下标，单元数组（cell）用大括号表示下标

18. 对变量名的基本要求：区分大小写，不超过63个字符，以字母开头，只能是字母，数字和下划线

19. clc             clear command（命令窗口中清除所有代码）（清屏），

        clf              clear figure（清理图形窗口）（并非关闭figure窗口）

         close         关闭最近的figure窗口

         close all     关闭所有figure窗口

         clear          清理工作空间（workspace）中的所有变量

          clear+变量名     清理工作空间中的指定变量（如果是多个变量，用空格隔开）

          edit+函数名       查看或编辑源文件

          who      显示工作空间中的所有变量名（仅展示出变量的名字）

          whos    显示工作空间中的所有变量名及其属性（大小、字节数、数据类型，等等）

          which+函数名     证实该函数是否在当前路径

          what      列出当前路径的所有matlab文件

          load       加载外部文件

          save      保存变量到外部文件。如果save后面没有任何东西，则默认将工作空间中的所有变量保存在文件matlab.mat中。

          save 文件名  指定变量列表——将指定变量保存在文件中（其中文件名不需要用单引号括起来，文件名的 .mat 后缀也可省略）。（具体地，可以执行doc save来查看save如何使用。）  例如：

          \>>save var2 x y ;  —— 将变量x和y保存在文件var2.mat中。

          \>>load var2

          在 save 和 load 命令中，文件名、变量名可以用字符串来表示，这时将 save 和 load 看作函数来调用：（推荐使用这种形式）

          \>>save( 'var2', 'x', 'y' );  % 功能与  save var2 x y ;  相同。

          \>>s = 'var2';

          \>>load( s ) % 功能与  load var2  相同。



20. MATLAB的帮助函数：

          help

          help+函数名   或   help+函数类名      精确查询

          helpwin                   打开帮助窗口

          helpwin+函数名      精确查询

          helpdesk                 打开帮助窗口

          doc                          打开帮助窗口

          doc+函数名             打开帮助窗口， 精确查询 

          lookfor+关键字        matlab中的谷歌，模糊查询

21. 函数式M文件的文件名，在MATLAB主窗口下不区分大小写，

          函数式M文件中，变量都是局部变量

          脚本式M文件中，变量都是全局变量

22. MATLAB搜索路径

          MATLAB通过搜索路径来查找M文件。因此，MATLAB的系统文件、Toolboxes工具箱函数、用户自己编写的M文件等都应该保存在搜索路径中。当用户输入一个标识符（例如Value）时，MATLAB按下列步骤处理：

          （1）检查 Value 是否为变量

          （2）检查 Value 是否为内部函数

          （3）在当前的工作目录下是否存在 Value.m 文件

          （4）在MATLAB搜索路径中是否存在 Value.m 文件

          如果在搜索路径中存在多个 Value.m 文件，则只执行第一个 Value.m 文件；如果找不到这一文件，则报错。

23. eps —— 在MATLAB编程中，对于除法运算，为了避免分母为零的情况出现，将分母的数与eps相加。（直接在命令窗口输入eps，再回车，会返回eps的值——2.2204e-16）。

准确讲，eps表示数1.0到与它相邻的最大的双精度浮点数。简单记，就是代表一个特别小的数。

    
```