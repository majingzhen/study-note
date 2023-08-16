# Tmpl模板文件变量输出问题

今天在使用 tmpl 模板编写生成 vue 代码的工具时发现字符串变量在进行填充时会附加上双引号，网上的解释是 ”如果 `.ObjectName` 是一个字符串类型的变量，生成的代码会默认添加双引号“

从网上找到两种解决方式，两种方法都是对字符串进行处理。

1：使用 `printf` 函数：在模板中，您可以使用 `printf` 函数来生成不带双引号的代码。

```
name: '{{printf "%s" .ObjectName}}Add',
// 把值传回了{{printf "%s" .ObjectName}}Add
props: {
    visible: Boolean, // 更新了<{{printf "%s" .ObjectName}}Add v-model:visible
    name: String
},
```

2：使用 `strings.Trim` 函数来删除生成的代码中的双引号

```go
strings.Trim(s, "\"")
```

发现都不好用，还是不起作用。



### 解决方法

使用 `text/template` 包

在 使用 template 对象进行模板处理的时候，没有关注到自己导入的包，发现使用的`html/template` 改成 `text/template` 具体原因还不清楚，有空了还需要研究一下。


