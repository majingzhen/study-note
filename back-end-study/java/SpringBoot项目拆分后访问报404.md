# SpringBoot项目拆分后报错404

原有一个 SpringBoot 项目，将项目进行拆分，将 domain、mapper、server拆分为一个子模块 被 原项目引用，但是在拆分后启动正常，但是访问 controller 时报错，报错内容如下：

```shell
Servlet.service() for servlet [dispatcherServlet] threw exception
javax.servlet.ServletException: Circular view path [error]: would dispatch back to the current handler URL [/system/error] again. Check your ViewResolver setup! (Hint: This may be the result of an unspecified view, due to default view name generation.)
```

转战各种搜索引擎后，发现大致是引入子模块依赖以及 依赖注入的问题

后来在启动类的上加入注解解决问题：

```java
@ComponentScan(basePackages = {"com.matuto.server", "com.matuto.system"})
```


