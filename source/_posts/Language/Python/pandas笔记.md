---
title: pandas笔记
thumbnail: 'http://static.come2rss.xyz/尼尔机械.jpg'
toc: true
top: 10
categories:
  - Language
  - Python
date: 2020-08-07 13:09:27
tags:
---

<!-- more -->



# 常用函数

```
pandas.read_excel(io, sheet_name, dtype)
```

神奇的函数：`io`可使用多种URL，如http、ftp、file、path。

sheet_name 指定读取的工作簿

dtype：以dict的形式指定多列的数据类型



## DataFrame以及Df对象

记一个DataFrame对象为df， 当然一个Narray对象为Na。

`pd.DataFrame()` 创建一个Df对象

如下例

```
df = pd.DataFrame([('bird', 389.0),
...                    ('bird', 24.0),
...                    ('mammal', 80.5),
...                    ('mammal', np.nan)],
...                   index=['falcon', 'parrot', 'lion', 'monkey'],
...                   columns=('class', 'max_speed'))
```

`df.values` 为一个Narray对象（实现从Df转化Na）

> 同样也有pd。DataFrame(na), 即从Narray转化为Df。

`df.dropna(inplace=True, how='any'， axis=0)` 删除一行中带有Nan的 一行数据（how=‘any’， axis=0）。其中axis可为1，即从列中寻找，how=‘all’，即一个数据集中必须都为Nan。

`inplace`参数经常出现，若为`True`表示直接对源对象修改，不返回一个新对象。`False`表示生成一个新对象，并只对新对象进行修改。

如

```
>>> df=pd.DataFrame(np.random.randn(4,3),columns=["A","B","C"])
>>> df.loc[1, 'A'] = np.nan
>>> df
          A         B         C
0  1.184976  0.757937 -1.403958
1       NaN -0.459589  0.774141
2 -1.522429  0.789742 -0.486841
3 -0.188630  0.511300  1.807077
>>> x = df.dropna(axis=0, inplace=True, how='any')
>>> x
>>> df
          A         B         C
0  1.184976  0.757937 -1.403958
2 -1.522429  0.789742 -0.486841
3 -0.188630  0.511300  1.807077

>>> df=pd.DataFrame(np.random.randn(4,3),columns=["A","B","C"])
>>> df.loc[1, 'A'] = np.nan
>>> x = df.dropna(axis=0, inplace=False, how='any')
>>> x
          A         B         C
0  0.999307 -1.473423 -0.255439
2  2.322430  0.228044 -1.383975
3 -0.734672  0.643534  1.203060
>>> df
          A         B         C
0  0.999307 -1.473423 -0.255439
1       NaN  0.438706  0.278976
2  2.322430  0.228044 -1.383975
3 -0.734672  0.643534  1.203060
>>>
```

`df.drop`类似与`df.dropna()`都是删除之用。

`df.reset_index(drop=True, inplace=True)` 用来重新生成index（行的索引）。`drop=True`表示重新生成index，否则则保留原来的index。

### 索引

`df.loc[:, [col1, col2] ]`（尤其是修改df原本数据时）可以有效选择数据。

`df.index` 返回df的**index ranger**

`df.values`返回一个Narray。

`df.columns`返回df的columns的list。

### 添加一行

```
df = pd.DataFrame(columns=['A', 'B'], data = [[1,2],[3,4]]) 
df.loc['B'] = dict
```

## 文件IO

`ExcelWriter(path, )` 返回一个ExcelWriter，配合就**多个**`df.to_excle(Ewriter,sheet_name)`写入DataFrame的数据，并用`EecelWriter.save()`来写入文件。

```
>>> writer = pd.ExcelWriter('output.xlsx')
>>> df1.to_excel(writer,'Sheet1')
>>> df2.to_excel(writer,'Sheet2')
>>> writer.save()
```

