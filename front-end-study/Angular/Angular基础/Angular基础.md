## AngularJs基础

## 搭建开发环境

### 安装NodeJs

 打开nodejs官网下载地址 http://nodejs.cn/download ,下载Windows 安装包64位12.10.0版本,下载完成之后运行安装软件进行安装,这里没有特别的配置,直接下一步下一步即可,安装完成后打开命令行进行测试 

```
node -v
```

 输出nodejs版本号即为安装成功,安装之后测试下npm是否可用 

```
npm -v
```

 输出npm版本号即为成功 

### 安装Angular Cli

Angular Cli是一个命令行界面工具，它可以创建项目、添加文件以及执行一大堆开发任务，比如测试、打包和发布。

打开命令行窗口进行安装

```
# -g 为全局安装
npm install -g @angular/cli
```

## Angular Cli的使用

 Angular Cli是一个命令行界面工具，它可以创建项目、添加文件以及执行一大堆开发任务，比如测试、 打包和发布。说白了就是为了能让开发者更容易的搭建angular工程。 

### 新建项目(命令行)

 语法: ng new 项目名,打开命令行输入 

```
ng new angular-demo
```

执行完后会在本地自动创建angular-demo项目,但这只是创建的初始项目,不包含我们需要的路由等一些必要的东西,通常我们会在命令后追加一些可选参数,常用如下:

1. --routing 添加带路由的模块(module)并import到main app module中

2. --skip-git 不执行Git repository初始化工作

3. --skip-tests 跳过测试文件

4. --skip-install 在项目第一次创建时不执行npm install
   
   所以,完整的创建项目应该是
   
   ```
   ng new angular-demo --routing --skip-git --skip-tests --skip-install
   ```

### 新建项目(WebStorm)

 打开WebStorm,点击File=>New=>Project=>Angular Cli进行创建,如图 

![1](G:\个人\博客\图片文件\1.jpg)

### 创建组件

 我们可以理解为一段带有业务逻辑和数据的代码,执行完创建组件的命令后,会在components目录新建home文件夹,该文件夹内一般包含一个css文件,一个html文件以及一个component.ts文件 

```
ng g component components/home
```

### 创建服务

 用来封装可重用的业务逻辑,会自动生成home.service.ts 

```
ng g service home
```

### 启动项目

 默认端口4200 

```
ng serve
```

## 目录结构

接着我们先来观察下Angular Cli生成项目的目录结构

![1 (1)](G:\个人\博客\图片文件\1 (1).jpg)

### 首层目录

```
e2e                 端到端的测试目录  用来做自动测试的
node_modules        第三方依赖包存放目录
src                 应用源代码目录 
karma.conf.js       karma是单元测试的执行器，karma.conf.js是karma的配置文件
package.json        这是一个标准的npm工具的配置文件，这个文件里面列出了该应用程序所使用的第三方依赖包。实际上我们在新建项目的时候，等了半天就是在下载第三方依赖包。下载完成后会放在node_modules这个目录中，后期我们可能会修改这个文件。
tsconfig.app.json   TypeScript编译器的配置,添加第三方依赖的时候会修改这个文件
tsconfig.spec.json  不用管
tslint.json         是tslint的配置文件，用来定义TypeScript代码质量检查的规则，不用管它
```

### src目录

```
app目录               包含应用的组件和模块，我们要写的代码都在这个目录
assets目录            资源目录，存储静态资源的  比如图片
environments目录      环境配置。Angular是支持多环境开发的，我们可以在不同的环境下（开发环境，测试环境，生产环境）共用一套代码，主要用来配置环境的
index.html          整个应用的根html，程序启动就是访问这个页面
main.ts             整个项目的入口点，Angular通过这个文件来启动项目
polyfills.ts        主要是用来导入一些必要库，为了让Angular能正常运行在老版本下
styles.css          主要是放一些全局的样式
test.ts             也是自动化测试用的
```

### app目录(重点)

app目录是我们要编写的代码目录。我们写的代码都是放在这个目录。

一个Angular程序至少需要一个模块和一个组件。在我们新建项目的时候命令行已经默认生成出来了,其中app.component.ts为组件,app.module.ts为模块,app-routing.module.ts为路由配置

## Typescript结构语法

TypeScript 是 JavaScript 的一个超集，支持 ECMAScript 6 标准。它由微软开发的自由和开源的编程语言。。它的设计目标是开发大型应用，它可以编译成纯 JavaScript，编译出来的 JavaScript 可以运行在任何浏览器上。

这里推荐一个学习TypeScript基础语法的网站https://www.runoob.com/typescript/ts-tutorial.html

我们重点关注实际项目中我们经常遇到的ts文件结构

### app.module.ts(根模块)

 Angular模块类描述应用的部件是如何组合在一起的,每个应用都至少有一个Angular模块,也就是根模块,用来引导并运行应用,你可以为它取任何名字,常规名字是AppModule,也就是app.module.ts文件,接下来我们详细看下代码,介绍及说明都写在注释里了 

```javascript
// 浏览器解析的模块
import { BrowserModule } from '@angular/platform-browser'; 
// angular的核心模块
import { NgModule } from '@angular/core';
// 路由组件
import { AppRoutingModule } from './app-routing.module';
// 根组件
import { AppComponent } from './app.component';
// home组件
import { HomeComponent } from './components/home/home.component';
// @NgModule接受一个元数据对象,告诉angular如何编译和启动应用
@NgModule({
  // 引入当前项目运行的组件,你新建的需要展示的组件都需要在这里引入
  declarations: [
    AppComponent,
    HomeComponent
  ],
  // 引入当前模块运行依赖的其他模块
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  // 定义的服务
  providers: [],
  // 指定应用的主视图(根组件),通过引导根AppModule来启动应用
  bootstrap: [AppComponent]
})
// 根模块不需要导出任何东西,因为其他组件不需要导入根模块,但一定要写...
export class AppModule { }
```

### home.component.ts(组件)

```javascript
// 引入angular的核心
import { Component, OnInit } from '@angular/core';

@Component({
  // 使用这个组件的名称
  selector: 'app-home',
  // html模板
  templateUrl: './home.component.html',
  // css样式
  styleUrls: ['./home.component.css']
})
// 实现OnInit接口
export class HomeComponent implements OnInit {
  // 构造函数
  constructor() { }
  // 初始化加载的生命周期函数
  ngOnInit() {
  }

}
```
