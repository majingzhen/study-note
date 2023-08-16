# OneDay - Python基础
## 输入输出
---
### 输出
用`print()`在括号中加上字符串，就可以向屏幕上输出指定的文字。比如输出'hello, world'，用代码实现如下：

```python
print('Hello, World!')
```
`print()`函数也可以接受多个字符串，用逗号","隔开，就可以连成一串输出：

```python
print("你好", "世界")
```
`print()`会依次打印每个字符串，遇到逗号","会输出一个空格。<br>
`print()`可以直接计算结果：
```python
>>> print(100 + 200)
300

# 或者我们可以这样
>>> print('100 + 200 =', 100 + 200)
100 + 200 = 300
```
### 输入
Python提供了一个`input()`函数，可以让用户输入字符串，并存放到一个变量里。比如：
```python
>>> name = input()
# 执行完input()函数后，控制台会等待你的输入，输入任意字符后，按回车完成。
>>> print(name)
```
这里的name是声明的一个变量，python的变量不需要指定类型，后面具体讲到。`print()`还可以直接打印变量的值。
`input()`函数中可以加入提示语，比如这样：
```python
>>> name = input("请输入你的名字：")
>>> print("hello,", name)
请输入你的名字：林钟小二
hello, 林钟小二
```

## 数据类型和变量
### 数据类型
在Python中，能够直接处理的数据类型有以下几种：
#### 数字
数字类型是不可更改的对象，对变量改变数字值就是生成/创建新的对象python支持多种数字类型：
1.  整形
2.  布尔型
3.  双精度浮点型
4.  十进制浮点型
5.  复数

#### 布尔型
bool, 布尔类型有两种True和False。对于值为0的数字、空集（空列表、空元组、空字典等）在Python中的布尔类型中都是False。
```python
>>> print(bool(1))
True
>>> print(bool('a'))
True
>>> print(bool(0))
False
>>> print(bool(''))
False
```
#### 空值
空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

#### 字符串
字符串(string)是不可变类型，就是说改变一个字符串的元素需要新建一个新的字符串。字符串是由独立的字符组成的，并且这些字符可以通过切片操作顺序地访问。Python里面通过在引号间包含字符的方式创建字符串，单引号和双引号的作用是相同的。
#### 列表
列表(list)像字符串类型一样，列表类型也是序列式的数据类型。字符串只能由字符组成，而且是不可变的（不能单独改变它的某个值），而列表则是能保留任意数目的Python对象的灵活的容器。<br>
列表可以执行pop,sort、reverse等操作。列表也可以添加或者减少元素，还可以跟其他的列表结合或者把一个列表分成几个。可以对单独一个元素或者多个元素执行insert、update或remove操作。
#### 元组
元组类型在很多操作上都跟列表一样，许多用在列表上的例子在元组上照样能跑，它们的主要不同在于元组是不可变的，或者说是只读的，所以那些用于更新列表的操作，比如用切片操作来更新一部分元素的操作，就不能用于元组类型。
#### 字典
字典是Python语言中唯一的映射类型。映射类型对象里哈希值（键，key）和指向的对象（值。value）是一对多的关系。一个字典对象是可变的，它是一个容器类型，能存储任意个数的Python对象，其中也包括其他容器类型。
### 变量
Python的变量是可以任意赋值的不用指定变量的类型。
```python
# a是整数
>>> a = 1
>>> print(a) 
# a是字符串
>>> a = 'a'
>>> >>> print(a)
# a是布尔值
>>> a = True
>>> print(a)

1
a
True
```
赋值语句的等号不等同于数学的等号，比如下面的代码：
```python
>>> x = 10
>>> x = x + 2
```
如果从数学上理解`x = x +  2`那无论如何是不成立的，在程序中，赋值语句先计算右侧的表达式`x + 2`，得到结果`12`，再赋给变量`x`。由于x之前的值是`10`，重新赋值后，`x`的值变成`12`。<br>
当我们写:
```python
a = 'ABC'
```
时，Python解释器干了两件事情：
1. 在内存中创建了一个`'ABC'`的字符串
2. 在内存中创建了一个名为`a`的变量，并把它指向`'ABC'`。

当我们把一个变量`a`赋值给另一个变量`b`，这个操作实际上是把变量`b`指向变量`a`所指向的数据，例如下面的代码:
```python
>>> a = 'ABC'
>>> b = a
>>> a = 'XYZ'
>>> print(b)
```
让我们猜想一下最后一行打印变量`b`的内容到底是`'ABC'`呢还是`'XYZ'`？让我们来一行一行的分析下到底发生了什么事情：

执行`a = 'ABC'`,解释器创建了字符串`'ABC'`和变量`a`，并把`a`指向`'ABC'`：
```python
graph LR
a --> ABC
```
执行`b = a`，解释器创建了变量`b`，并把`b`指向`a`指向的字符串`'ABC'`：
```python
graph LR
a --> ABC
b --> ABC
```
执行`a = 'XYZ'`，解释器创建了字符串`'XYZ'`，并把`a`的指向改为`'XYZ'`，但`b`并没有更改：
```python
graph LR
a --> XYZ
b --> ABC
```
最后打印变量`b`的结果自然是`'ABC'`了。

### 常量
所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
```python
PI = 3.14159265359
```

## 字符串与编码
### 字符编码
字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。<br>
常用的编码格式有：ASCII编码，Unicode编码，UTF-8编码。
### Python的字符串
在Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：
```python
>>> print('包含中文的str')
包含中文的str
```
对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
```python
>>> print(ord('A'))
65
>>> print(ord('中'))
20013
>>> print(chr(66))
'B'
>>> print(chr(25991))
'文'
```
还可以使用十六进制写字符串:
```python
>>> print('\u4e2d\u6587')
'中文'
```
由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
Python对bytes类型的数据用带b前缀的单引号或双引号表示：
```python
x = b'ABC'
```
要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
`str`可以通过`encode()`方法可以编码为指定的`bytes`，例如：

```python
>>> print('ABC'.encode('ascii'))
b'ABC'
>>> print('中文'.encode('utf-8'))
b'\xe4\xb8\xad\xe6\x96\x87'
>>> print('中文'.encode('ascii'))
Traceback (most recent call last):
  File ".../HelloWorld.py", line 82, in <module>
    print('中文'.encode('ascii'))
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```
纯英文的`str`可以用`ASCII`编码为`bytes`，内容是一样的，含有中文的`str`可以用`UTF-8`编码为`bytes`。含有中文的`str`无法用`ASCII`编码，因为中文编码的范围超过了`ASCII`编码的范围，Python会报错。<br>
在`bytes`中，无法显示为`ASCII`字符的字节，用`\x##`显示。<br>
反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是`bytes`。要把`bytes`变为`str`，就需要用`decode()`方法：
```python
>>> print(b'ABC'.decode('ascii'))
'ABC'
>>> print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
'中文'
```
如果bytes中包含无法解码的字节，decode()方法会报错：
```python
>>> print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
Traceback (most recent call last):
  File ".../HelloWorld.py", line 87, in <module>
    print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
```
如果`bytes`中只有一小部分无效的字节，可以传入`errors='ignore'`忽略错误的字节：
```python
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
'中'
```
`len()`函数可以计算`str`中包含多少个字符：
```python
>>> print(len('ABC'))
3
>>> print(len('中文'))
2
```
`len()`函数计算的是`str`的字符数，如果换成`bytes`，`len()`函数就计算字节数：
```python
>>> print(len(b'ABC'))
3
>>> print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
6
>>> print(len('中文'.encode('utf-8')))
6
```

### 格式化
#### 占位符
我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。<br>
在Python中使用的也是占位符`%`来替换，举例如下：
```python
>>> print('Hello, %s' % 'world')
Hello, world
>>> print('你好, %s, 你一共需要支付%d元钱.' % ('张三', 5000))
你好, 张三, 你一共需要支付5000元钱.
```
常见的占位符如下所示：

占位符 | 替换内容
---|---
%d | 整数
%f | 浮点数
%s | 字符串
%x | 十六进制整数

有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。<br>
如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
```python
>>> print('年龄：%s,是否结婚：%s' % (25, True))
年龄：25,是否结婚：True
```
有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
```python
>>> print('今天的盈利比昨天上涨了：%d %%' % 7)
今天的盈利比昨天上涨了：7 %
```
#### farmat()
`farmat()`是另一种格式化字符串的方法，他会用传入的参数依次替换字符串内的占位符`{0}`、`{1}`......,这种方式写起来会比较麻烦.
```python
>>> print('{0}的成绩提升了 {1:.1f}%'.format('小明', 17.155))
小明的成绩提升了 17.2%
```
注：这里的浮点型，可以指明需要显示的小数位数，超出的部分将按照四舍五入的方式截取。

## 使用list和tuple
### list
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。<br>
比如，列出一个部门所有人员的名字，就可以用一个list表示：
```python
>>> demp = ['张三', '李四', '王五']
>>> print(demp)
['张三', '李四', '王五']
```
变量`classmates`就是一个list。用`len()`函数可以获得list元素的个数：
```python
>>> print(len(demp))
3
```
访问list中每一个位置的元素使用索引，索引从`0`开始:
```python
>>> print(demp[0])
'张三'
>>> print(demp[1])
'李四'
>>> print(demp[2])
'王五'
>>> print(demp[3])
Traceback (most recent call last):
  File ".../HelloWorld.py", line 127, in <module>
    print(demp[3])
IndexError: list index out of range
```
当索引超出了范围时，Python会报一个`IndexError`错误，所以，要确保索引不要越界，记得最后一个元素的索引是`len(demp) - 1`。

list还可以直接使用-1来访问最后一个元素：
```python
>>> print(demp[-1])
'王五'
```
以此类推，可以获取倒数第2个、倒数第3个：
```python
>>> print(demp[-2])
'李四'
>>> print(demp[-3])
'张三'
```
#### 追加元素
list是一个可变的有序表，所以，可以使用`append()`方法往list中追加元素到末尾：
```python
>>> demp.append('赵六')
>>> print(demp)
['张三', '李四', '王五', '赵六']
```
#### 插入元素
也可以使用`insert()`方法把元素插入到指定的位置，比如索引号为1的位置：
```python
>>> demp.insert(1, '钱二')
>>> print(demp)
['张三', '钱二', '李四', '王五', '赵六']
```
#### 删除元素
要删除list末尾的元素，用`pop()`方法：
```python
>>> demp.pop()
>>> print(demp)
['张三', '钱二', '李四', '王五']
```
要删除指定位置的元素，用`pop(i)`方法，其中i是索引位置：
```python
>>> demp.pop(1)
>>> print(demp)
['张三', '李四', '王五']
```
#### 替换元素
要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
```python
>>> demp[1] = '周七'
>>> print(demp)
['张三', '周七', '王五']
```
list里面的元素的数据类型也可以不同，比如：
```python
>>> L = ['张三', 123, True]
```
list元素也可以是另一个list，比如：
```python
>>> s = ['java', 'python', ['php','asp'], '.net']
>>> print(len(s))
4
# 或者可以写成
>>> p = ['php', 'asp']
>>> s = ['java', 'python', p, '.net']
```
要拿到`'php'`可以写`p[0]`或者`s[2][0]`，因此s可以看成是一个二维数组，类似的还有三维、四维……数组。

如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
```python
>>> L = []
>>> print(len(L))
0
```
### tuple
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用`demp[0]`，`demp[-1]`，但不能赋值成另外的元素。
```python
>>> demp = ('张三', '李四', '王五')
>>> print(demp)
('张三', '李四', '王五')
>>> print(demp[0])
'张三'
```
在开发中，因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
```python
>>> t = (1, 2)
>>> print(t)
(1, 2)
```
如果要定义一个空的tuple，可以写成()：
```python
>>> t = ()
>>> print(t)
()
```
需要注意的是，如果要定义一个只有1个元素的tuple，那么你就必须这样定义：
```python
>>> t = (1,)
>>> print(t)
(1,)
```
因为`()`即可以表示tuple，又可以表示数学公式中的小括号，容易产生歧义，如果不加逗号的话，结果就会像下方所示：
```python
>>> t = (1)
>>> print(t)
1
```
#### 可变的tuple
```python
>>> t = ('a', 'b' ,['A' ,'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> print(t)
('a', 'b', ['X', 'Y'])
```
这里tuple发生了变化，不是说tuple是不可变的吗？为什么又变了呢，我们来看下发生了什么：

定义的时候tuple包含的3个元素：

![image](https://www.liaoxuefeng.com/files/attachments/923973516787680/0)

当我们把list的元素`'A'`和`'B'`修改为`'X'`和`'Y'`后，tuple变为：

![image](https://www.liaoxuefeng.com/files/attachments/923973647515872/0)

表面上看上去，tuple的元素的确变了，但其实变得不是tuple的元素，而是list的元素，tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向`'a'`，就不能改成指向`'b'`，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

## 使用dict和set
### dict
Python内置了字典：dict的支持，dict全称dictionary，即java中的map，使用键-值（key-value）存储，具有极快的查找速度。

用Python写一个dict如下：
```python
>>> d = {'张三': 98, '李四': 75,'王五': 90}
>>> print(d['张三'])
98
```
这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value。

把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
```python
>>> d['李四'] = 68
>>> print(d['李四'])
68
```
一个key只能对应一个value，多次对一个key放入value，后面的值会把前面的值冲掉。

如果key不存在，dict就会报错：
```python
>>> print(d['赵六'])
Traceback (most recent call last):
  File ".../HelloWorld.py", line 212, in <module>
    print(d['赵六'])
KeyError: '赵六'
```
要避免key不存在的错误，有两种办法，一是通过`in`判断key是否存在：
```python
>>> print('赵六' in d)
False
```
二是通过dict提供的`get()`方法，如果key不存在，可以返回`None`，或者自己指定的value：
```python
>>> print(d.get('赵六'))
None
>>> print(d.get('赵六', False))
False
```
要删除一个key，用`pop(key)`方法，对应的value也会从dict中删除：
```python
>>> d.pop('张三')
>>> print(d)
{'李四': 75, '王五': 90}
```
注：dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：
-  查找和插入的速度极快，不会随着key的增加而变慢；
-  需要占用大量的内存，内存浪费多。

而list相反：
-  查找和插入的时间随着元素的增加而增加；
-  占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。

在使用过程中，需要牢记的第一条就是dict的key必须是不可变对象。

### set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合：
```python
>>> s = set([1,2,3])
>>> print(s)
{1, 2, 3}
```
注意，传入的参数`[1, 2, 3]`是一个list，而显示的`{1, 2, 3}`只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。

set中的元素不能重复，重复的元素将被自动过滤：
```python
>>> s = set([1,1,2,3,2,3])
>>> print(s)
{1, 2, 3}
```
通过`add(key)`方法可以添加元素到set中，可以重复添加，但不会有效果：
```python
>>> s.add(4)
>>> print(s)
{1, 2, 3, 4}
>>> s.add(4)
>>> print(s)
{1, 2, 3, 4}
```
通过`remove(key)`方法可以删除元素：
```python
>>> s.remove(4)
>>> print(s)
{1, 2, 3}
```
两个set可以做交集、并集等操作：
```python
>>> s1 = set([1,2,3])
>>> s2 = set([2,3,4])
>>> print(s1 & s2)
{2, 3}
>>> print(s1 | s2)
{1, 2, 3, 4}
```
set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”