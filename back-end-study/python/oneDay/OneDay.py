# # 输出
# print("Hello,World!")
#
# # 多字符串输出
# print("你好", "世界")
#
# # 计算数值
# print(100 + 200)
#
# # 或者我们可以这样
# print('100 + 200 =', 100 + 200)
#
# # 输入
# name = input()
# print(name)
#
# # input()函数可以加入提示语
# name = input("请输入你的名字：")
# print("hello,", name)

# 数据类型
# 数字

# 数字类型是不可更改的对象。对变量改变数字值就是生成/创建新的对象。Python支持多种数字类型：
# 整型、布尔型、双精度浮点型、十进制浮点型、复数。

# 布尔型
# bool, 布尔类型有两种True和False。对于值为0的数字、空集（空列表、空元组、空字典等）在Python中的布尔类型中都是False。
# print(bool(1))
#
# print(bool('a'))
#
# print(bool(0))
#
# print(bool(''))

### 空值
# 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

### 字符串
# 字符串(string)是不可变类型，就是说改变一个字符串的元素需要新建一个新的字符串。字符串是由独立的字符组成的，并且这些字符可以通过切片操作顺序地访问。Python里面通过在引号间包含字符的方式创建字符串，单引号和双引号的作用是相同的。
### 列表
# 列表(list)像字符串类型一样，列表类型也是序列式的数据类型。字符串只能由字符组成，而且是不可变的（不能单独改变它的某个值），而列表则是能保留任意数目的Python对象的灵活的容器。<br>
# 列表可以执行pop,sort、reverse等操作。列表也可以添加或者减少元素，还可以跟其他的列表结合或者把一个列表分成几个。可以对单独一个元素或者多个元素执行insert、update或remove操作。
### 元组
# 元组类型在很多操作上都跟列表一样，许多用在列表上的例子在元组上照样能跑，它们的主要不同在于元组是不可变的，或者说是只读的，所以那些用于更新列表的操作，比如用切片操作来更新一部分元素的操作，就不能用于元组类型。
### 字典
# 字典是Python语言中唯一的映射类型。映射类型对象里哈希值（键，key）和指向的对象（值。value）是一对多的关系。一个字典对象是可变的，它是一个容器类型，能存储任意个数的Python对象，其中也包括其他容器类型。
## 变量
# Python的变量是可以任意赋值的不用指定变量的类型。
# a = 1
# print(a)
# a = 'a'
# print(a)
# a = True
# print(a)
#
# x = 10
# x = x + 2
# print(x)
# 变量赋值
# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# ### Python中的字符串
# print('包含中文的str')
#
# # ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字
# print(ord('A'))
# print(ord('中'))
# print(chr(66))
# print(chr(25991))
#
# # 用十六进制写str
# print('\u4e2d\u6587')

# # 函数encode()可以编码为指定的bytes
# print('ABC'.encode('ascii'))
# print('中文'.encode('utf-8'))
# # 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错
# print('中文'.encode('ascii'))

# # 要把bytes变为str，就需要用decode()方法
# print(b'ABC'.decode('ascii'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# # 如果bytes中包含无法解码的字节，decode()方法会报错
# # print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
# # 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
# print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# # `len()`函数可以计算`str`中包含多少个字符：
# print(len('ABC'))
# print(len('中文'))
#
# # len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
# print(len(b'ABC'))
# print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
# print(len('中文'.encode('utf-8')))

# ## 格式化字符
# print('Hello, %s' % 'world')
# print('你好, %s, 你一共需要支付%d元钱.' % ('张三', 5000))
#
# # 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
# print('年龄：%s,是否结婚：%s' % (25, True))
#
# # 字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
# print('今天的盈利比昨天上涨了：%d %%' % 7)
#
# # 使用farmat()函数格式化字符串
# print('{0}的成绩提升了 {1}%'.format('小明', 17.155))

# # 使用list和tuple
# # list
# # Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
# # 比如，列出一个部门所有人员的名字，就可以用一个list表示：
# demp = ['张三', '李四', '王五']
# print(demp)

# # 变量demp就是一个list。用len()函数可以获得list元素的个数：
# print(len(demp))

# # 访问list中每一个位置的元素使用索引，索引从`0`开始:
# print(demp[0])
# print(demp[1])
# print(demp[2])
# print(demp[3])

# # 当索引超出了范围时，Python会报一个`IndexError`错误，所以，要确保索引不要越界，记得最后一个元素的索引是`len(demp) - 1`。
# # Python的list还可以直接使用-1来访问最后一个元素：
# print(demp[-1])
#
# # 以此类推，可以获取倒数第2个、倒数第3个：
# print(demp[-2])
# print(demp[-3])

# # list是一个可变的有序表，所以，可以使用append()方法往list中追加元素到末尾：
# demp.append('赵六')
# print(demp)
#
# # 也可以使用insert()方法把元素插入到指定的位置，比如索引号为1的位置：
# demp.insert(1, '钱二')
# print(demp)
#
# # 要删除list末尾的元素，用pop()方法：
# demp.pop()
# print(demp)
#
# # 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
# demp.pop(1)
# print(demp)
#
# # 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
# demp[1] = '周七'
# print(demp)

# # list里面的元素的数据类型也可以不同，比如：
# L = ['张三', 123, True]
#
# # list元素也可以是另外一个list, 比如
# s = ['java', 'python', ['php','asp'], '.net']
# print(len(s))
# # 或者可以写成
# p = ['php', 'asp']
# s = ['java', 'python', p, '.net']
#
# # 如果一个list中一个元素也没有，就是一个空的list，它的长度为0：
# L = []
# print(len(L))

# ### tuple
# # 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用demp[0]，demp[-1]，但不能赋值成另外的元素。
# demp = ('张三', '李四', '王五')
# print(demp)
# print(demp[0])
#
# # 当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
# t = (1, 2)
# print(t)
#
# # 如果要定义一个空的tuple，可以写成()：
# t = ()
# print(t)
#
# # 需要注意的是，如果要定义一个只有1个元素的tuple，那么你就必须这样定义：
# t = (1,)
# print(t)
#
# # 因为小括号即可以标识tuple，又可以表示数学公式中的小括号，容易产生歧义，如果不加逗号的话，结果就会像下方所示：
# t = (1)
# print(t)

# # 可变的tuple
# t = ('a', 'b' ,['A' ,'B'])
# t[2][0] = 'X'
# t[2][1] = 'Y'
# print(t)

# ## 使用dict和set
# ### dict
# # Python内置了字典：dict的支持，dict全称dictionary，即java中的map，使用键-值（key-value）存储，具有极快的查找速度。
# d = {'张三': 98, '李四': 75,'王五': 90}
# print(d['张三'])

# # 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
# d['李四'] = 68
# print(d['李四'])

# # 如果key不存在，dict就会报错：
# print(d['赵六'])

# # 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
# print('赵六' in d)
#
# # 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
# print(d.get('赵六'))
# print(d.get('赵六', False))
#
# # 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
# d.pop('张三')
# print(d)

### set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3])
print(s)

# # set中的元素不能重复，重复的元素将被自动过滤：
# s = set([1,1,2,3,2,3])
# print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s)
s.add(4)
print(s)

# 通过remove(key)方法可以删除元素：
s.remove(4)
print(s)

# 两个set可以做交集、并集等操作：
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)
