# PHP基础

## 简介

### 什么是 PHP？

- PHP 是 "PHP Hypertext Preprocessor" 的首字母缩略词
- PHP 是一种被广泛使用的开源脚本语言
- PHP 脚本在服务器上执行
- PHP 没有成本，可供免费下载和使用

### PHP 能够做什么？

- PHP 能够生成动态页面内容
- PHP 能够创建、打开、读取、写入、删除以及关闭服务器上的文件
- PHP 能够接收表单数据
- PHP 能够发送并取回 cookies
- PHP 能够添加、删除、修改数据库中的数据
- PHP 能够限制用户访问网站中的某些页面
- PHP 能够对数据进行加密

## 环境配置

### 在您的 PC 上运行 PHP

不过如果您的服务器不支持 PHP，那么您必须：

- 安装 web 服务器
- 安装 PHP
- 安装数据库，比如 MySQL

官方的 PHP 网站 (PHP.net) 提供了 PHP 的安装说明：http://php.net/manual/zh/install.php

推荐使用：phpstudy、WampServer

## 基本语法

首先还是入门标志：Hello World!

```php+HTML
<!DOCTYPE html>
<html>
<body>
<h1>我的第一张 PHP 页面</h1>
<?php
echo "Hello World!";
?>
</body>
</html>
```

PHP脚本可放置于文档中的任何位置。

PHP 脚本以 * 开头，以 *?>* 结尾：

```php
<?php
// 此处是 PHP 代码
?>
```

PHP的注释：

```php+HTML
<!DOCTYPE html>
<html>
<body>
<?php
// 这是单行注释
# 这也是单行注释
/*
这是多行注释块
它横跨了
多行
*/
?>
</body>
</html>
```

### 大小写敏感

在 PHP 中，所有用户定义的函数、类和关键词（例如 if、else、echo 等等）都对大小写不敏感。

## 变量

变量是存储信息的容器

```php
<?php
$x=5;
$y=6;
$z=$x+$y;
echo $z;
?>
```

在代数中我们使用字母（比如 x）来保存值（比如 5）。

从上面的表达式 z=x+y，我们能够计算出 z 的值是 11。

在 PHP 中，这三个字母被称为*变量*。

### PHP 变量规则：

- 变量以 $ 符号开头，其后是变量的名称
- 变量名称必须以字母或下划线开头
- 变量名称不能以数字开头
- 变量名称只能包含字母数字字符和下划线（A-z、0-9 以及 _）
- 变量名称对大小写敏感（$y 与 $Y 是两个不同的变量）

**注释：**PHP 变量名称对大小写敏感！

### 创建 PHP 变量

PHP 没有创建变量的命令。变量会在首次为其赋值时被创建。

**注释：**如果您为变量赋的值是文本，请用引号包围该值。

PHP 不是一门强类型语言，不用指定变量的数据类型。

### 变量的作用域

在 PHP 中，可以在脚本的任意位置对变量进行声明。

变量的作用域指的是变量能够被引用/使用的那部分脚本。

PHP 有三种不同的变量作用域：

- local（局部）
- global（全局）
- static（静态）

### PHP global 关键词

global 关键词用于在函数内访问全局变量。

要做到这一点，请在（函数内部）变量前面使用 global 关键词：

```php
<?php
$x=5;
$y=10;
function myTest() {
  global $x,$y;
  $y=$x+$y;
}
myTest();
echo $y; // 输出 15
?>
```

PHP 同时在名为 $GLOBALS[index] 的数组中存储了所有的全局变量。下标存有变量名。这个数组在函数内也可以访问，并能够用于直接更新全局变量。

```php
<?php
$x=5;
$y=10;
function myTest() {
  $GLOBALS['y']=$GLOBALS['x']+$GLOBALS['y'];
} 
myTest();
echo $y; // 输出 15
?>
```

### PHP static 关键词

通常，当函数完成/执行后，会删除所有变量。不过，有时我需要不删除某个局部变量。实现这一点需要更进一步的工作。

要完成这一点，请在您首次声明变量时使用 *static* 关键词：

```php
<?php
function myTest() {
  static $x=0;
  echo $x;
  $x++;
}
myTest();
myTest();
myTest();
?>
```

### 输出语句

在 PHP 中，有两种基本的输出方法：echo 和 print。

echo 和 print 之间的差异：

- echo - 能够输出一个以上的字符串
- print - 只能输出一个字符串，并始终返回 1

**提示：**echo 比 print 稍快，因为它不返回任何值。

```php+HTML
<?php
$txt1="Learn PHP";
$txt2="W3School.com.cn";
$cars=array("Volvo","BMW","SAAB");
echo $txt1;
echo "<br>";
echo "Study PHP at $txt2";
echo "My car is a {$cars[0]}";
print $txt1;
print "<br>";
print "Study PHP at $txt2";
print "My car is a {$cars[0]}";
?>
```

## 数据类型

### 字符串

字符串是字符序列，比如 "Hello world!"。

字符串可以是引号内的任何文本。您可以使用单引号或双引号。

### 整数

整数是没有小数的数字。整数规则：

- 整数必须有至少一个数字（0-9）
- 整数不能包含逗号或空格
- 整数不能有小数点
- 整数正负均可
- 可以用三种格式规定整数：十进制、十六进制（前缀是 0x）或八进制（前缀是 0）

### 浮点数

浮点数是有小数点或指数形式的数字。

PHP中 var_dump() 会返回变量的数据类型和值。

### 逻辑

逻辑是 true 或 false。

### 数组

数组在一个变量中存储多个值。

```php
<?php 
$cars=array("Volvo","BMW","SAAB");
var_dump($cars);
?>
```

### 对象

对象是存储数据和有关如何处理数据的信息的数据类型。在 PHP 中，必须明确地声明对象。

首先我们必须声明对象的类。对此，我们使用 class 关键词。类是包含属性和方法的结构。

然后我们在对象类中定义数据类型，然后在该类的实例中使用此数据类型：

```php
<?php
class Car
{
  var $color;
  function Car($color="green") {
    $this->color = $color;
  }
  function what_color() {
    return $this->color;
  }
}
?>
```

### NULL值

特殊的 NULL 值表示变量无值。NULL 是数据类型 NULL 唯一可能的值。

NULL 值标示变量是否为空。也用于区分空字符串与空值数据库。

可以通过把值设置为 NULL，将变量清空。

### 查看数据类型

  1.gettype(传入一个变量) 能够获得变量的类型

  2.var_dump(传入一个变量) 输出变类型和值

### 判断数据类型

我们使用is_* 系列函数。 is_types这一系列的函数，来进行判断某个东西是不是某个类型。如果是这个类型返回真，不是这个类型返回假。

is_int 是否为整型
is_bool 是否为布尔
is_float 是否是浮点
is_string 是否是字符串
is_array 是否是数组
is_object 是否是对象
is_null 是否为空
is_resource 是否为资源
is_scalar 是否为标量
is_numeric 是否为数值类型
is_callable 是否为函数

### 数据类型之自动转换和强制转换

#### 布尔值的自动类型转换

1，整型的0为假，其他整型值全为真

2, 浮点的0.0，布尔值的假。小数点后只要有一个非零的数值即为真。

3，空字符串为假，只要里面有一个空格都算真。

4，字符串的0，也将其看作是假。其他的都为真

5，空数组也将其视为假，只要里面有一个值，就为真。

6，空也为假

7, 未声明成功的资源也为假

#### 其他类型的自动类型转换

```php
<?php
//布尔变整型参与运算
$fo = true;
$result = $fo + 10;
//$result 结果为整型的11，因为$fo布尔的true变为了1
//如果$fo的值为0
var_dump($result);
//字符串类型
$str = '419不要爱';
$result = $str + 1;
//结果为420。因为将$str变为了整型的419参与运算
//将419放在字符串中间和结尾试试
var_dump($result);
?>
```

#### 强制类型转换

 1.intval()、floatval()、strval()

  2.变量前加上()里面写上类型，将它转换后赋值给其他变量

  3.settype(变量，类型) 直接改变量本身

##### intval()、floatval()、strval()转换

```php
<?php
    $float = 1.23;
    $result = intval($float);
    //看看结果是不是变了？
    var_dump($result);
    //整型的5
    $int = 5;
    $re = floatval($int);
    var_dump($re);
    //定义整型的变量
    $int = 23;
    $bian = strval($int);
    //强制变成字符串试试
    var_dump($bian);
?>
```

##### 变量前加上()里面写上类型，将它转换后赋值给其他变量

```php
<?php
   //定义一个变量，我们来变化一下试试
   $transfer = 12.8;
   //把浮点变为整型
    $jieguo = (int)$transfer;
    var_dump($jieguo);
   //把浮点变为布尔
   $jieguo = (bool) $transfer;
   var_dump($jieguo);
   //把布尔变整型
   $bool = true;
   $jieguo = (int)$bool;
   var_dump($jieguo);
    //把浮点变数组
   $fo = 250;
   $jieguo = (array)$fo;
   var_dump($jieguo);
   //其他的操作方式，按照文字总结的规律你来试试
?>
```

##### settype(变量，类型) 直接改变量本身

```php
<?php
    //定义浮点变为整型
    $fo = 250.18;
   //settype第二个参数是int，你实验的时候要记得第二个参数要为字符串类型
    settype($fo,'int');
    //输出看看结果
    var_dump($fo);
?>
```

### 常量

常量就是长久不变的值。

常量在代码中的定义、书写方式：

```php
<?php

define('MY_NAME','林钟小二');

echo MY_NAME;
//正确的调用方式该这么写
echo '我的名字是' . MY_NAME;
?>
```

#### 常用含量

| 常量名           | 说明                 |
| ------------- | ------------------ |
| **LINE**      | 当前所在的行             |
| **FILE**      | 当前文件在服务器的路径        |
| **FUNCTIOIN** | 当前函数名              |
| **CLASS**     | 当前类名               |
| **METHOD**    | 当前成员方法名            |
| PHP_OS        | PHP运行的操作系统         |
| PHP_VERSION   | 当前PHP的版本           |
| **TRAIT**     | Trait 的名字,php5.4新加 |
| **DIR**       | 文件所在的目录            |
| **NAMESPACE** | 当前命名空间的名称（区分大小写）   |

### 算术运算

| 符号  | 说明        | 举例      |
| --- | --------- | ------- |
| +   | 加号        | $x + $y |
| -   | 减号        | $x - $y |
| *   | 乘号,乘以     | $x * $y |
| /   | 除号,除以     | $x / $y |
| %   | 取余也叫取模、求模 | $x % $y |

### 赋值运算

| 符号  | 举例       | 等价式          |
| --- | -------- | ------------ |
| +＝  | $x +＝ $y | $x ＝ $x + $y |
| -＝  | $x -＝ $y | $x ＝ $x - $y |
| *＝  | $x *＝ $y | $x ＝ $x * $y |
| /＝  | $x /＝ $y | $x ＝ $x / $y |
| %＝  | $x %＝ $y | $x ＝ $x % $y |
| .＝  | $x .＝ $y | $x ＝ $x . $y |

### 自加自减

| 符号   | 说明    |
| ---- | ----- |
| $x++ | 先赋值后加 |
| $x-- | 先赋值后减 |
| ++$x | 先加后赋值 |
| --$x | 先减后赋值 |

### 比较运算符

| 说明   | 符号  |
| ---- | --- |
| 大于   | >   |
| 小于   | <   |
| 大于等于 | ≥   |
| 小于等于 | ≤   |
| 不等于  | ≠   |
| 等于   | =   |

### 逻辑运算符

| 举例        | 说明        | 详细说明                        |
| --------- | --------- | --------------------------- |
| $x and $y | 逻辑与（并且关系） | $x 和$y 为真则返回真               |
| $x && $y  | 同上        | 同上                          |
| $x or $y  | 逻辑或       | $x,$y均为false时为假，其他情况全为真     |
| $a\|\|$b  | 同上        | 同上                          |
| !$x       | 逻辑非       | 取反，即true变为false，false变为true |
| $x xor $y | 逻辑异或      | 相同取false，相异为true            |

### 其他运算符

| 符号            | 说明                                   |
| ------------- | ------------------------------------ |
| $x? 真代码段:假代码段 | 判断是否为真假 ? 真情况 : 假情况;                 |
| ``（反引号）       | 反引号中间插代命令，执行系统命令，等价于shell_exec函数     |
| @             | 单行抑制错误，把这一行的错误不让它显示出来了，效率低不建议使用      |
| =>            | 数组下标访问符                              |
| ->            | 对象访问符                                |
| instanceof    | 判断某个对象是否来自某个类，如果是的返回true，如果不是返回false |
