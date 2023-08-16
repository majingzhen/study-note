# TwoDay - Python进阶
## 条件判断
### if
Python的`if`是不用使用`{}`的，需要使用Python的缩进规则，代码如下：
```
age = 20
if age >= 18:
    print('你的年龄是', age)
    print('你已满18岁')
```

### if ... else
可以给`if`添加一个`else`语句，意思是，如果`if`判断是`False`，不要执行`if `的内容，去把`else`执行了:
```
age = 16
if age >= 18:
    print('你的年龄是', age)
    print('你已满18岁')
else:
    print('你的年龄是', age)
    print('你未满18岁')
```
### if ... elif ... else
`if`还可以用`elif`更细致的判断，语法形式为：
```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```
示例代码如下：
```
age = 3
if age >= 18:
    print('已成年')
elif age >= 6:
    print('青少年')
else:
    print('儿童')
```
注：`if`语句执行有个特点，它是从上往下判断，如果在某个判断上是`True`，把该判断对应的语句执行后，就忽略掉剩下的`elif`和`else`，如下列代码：
```
age = 20
if age >= 6:
    print('青少年')
elif age >= 18:
    print('已成年')
else:
    print('儿童')
```
`if`的判断条件还可以简写，比如：
```
if x:
    print('True')
```
这里的`x`可以为非零数值、非空字符串、非空list等，就判断为`True`,否则为`False`.
注：`if`、`elif`、`else`后边不要少写了冒号`:`。
### 再议input
看下边这段代码：
```
birth = input('请输入出生年份：')
if birth < 2000:
    print('00前')
else:
    print('00后')
```
输入1984后，结果报错：
```
请输入出生年份：1984
Traceback (most recent call last):
  File ".../TwoDay.py", line 35, in <module>
    if birth < 2000:
TypeError: '<' not supported between instances of 'str' and 'int'
```
这是因为`input()`返回的数据类型是`str`，`str`不能直接和整数比较，必须先把`str`转换成整数。Python中把`str`转成整数的方法是`int()`:
```
s = input('请输入出生年份：')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
```
这样运行就没有问题了，但是int()函数在将str转成整数的时候如果遇到非数字会怎么处理呢，看下边的错误信息：
```
Traceback (most recent call last):
  File ".../TwoDay.py", line 42, in <module>
    birth = int(s)
ValueError: invalid literal for int() with base 10: 'abc'
```
`int()`函数发现一个字符串并不是合法的数字时就会报错.
## 循环
Python的循环有两种,一种是for...in循环,一种是while循环，让我们分别看下他们是怎么使用的。
### for...in
for...in循环可以依次把list或tuple中的每个元素迭代出来，代码如下：
```
names = ['张三', '李四', '王五']
for name in names:
    print(name)
```
这段代码回一次打印出`names`的每一个元素:
```
'张三'
'李四'
'王五'
```
所以for x in ...循环就是把每个元素代入变量`x`，然后执行缩进块的语句.

再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
```
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
```
计算1-10的整数和还可以写的更简单一点，Python提供了一个生成整数序列的函数：`range()`,然后再通过`list()`函数将其转换为list，示例如下：
```
>>> nums = list(range(11))
>>> print(nums)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
注：这里需要注意的一点是，`range()`生成的整数序列是从0开始的，如果要生成1-10的整数序列我们就要写成`range(11)`.
### while
while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现:
```
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
```
### break
在循环中，break语句可以提前退出循环,比如下面的代码,本来要打印1 ~ 100的数字：
```
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
```
观察上边的代码我们可以发现，本来是要打印1~100的，我们加了一个判断，在`n`大于10的时候执行了`break`语句，提前结束掉了程序。

可见break的作用是提前结束循环。
### continue
在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环.
```
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
```
在上面的代码中，我们让n为偶数的时候跳过本次循环，实现了打印1~10中所有奇数的功能。

可见continue的作用是提前结束本轮循环，并直接开始下一轮循环。