# SpringBoot整合Swagger2报错

### 依赖版本：

```xml
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.7.0</version>
</parent>

 <!--swagger-->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>
<!--swagger ui-->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>1.9.6</version>
</dependency>
```

### 项目启动时报错：

```java
org.springframework.context.ApplicationContextException: Failed to start bean 'documentationPluginsBootstrapper'; nested exception is java.lang.NullPointerException
    at org.springframework.context.support.DefaultLifecycleProcessor.doStart(DefaultLifecycleProcessor.java:181) ~[spring-context-5.3.20.jar:5.3.20]
    at org.springframework.context.support.DefaultLifecycleProcessor.access$200(DefaultLifecycleProcessor.java:54) ~[spring-context-5.3.20.jar:5.3.20]
    at org.springframework.context.support.DefaultLifecycleProcessor$LifecycleGroup.start(DefaultLifecycleProcessor.java:356) ~[spring-context-5.3.20.jar:5.3.20]
    at org.springframework.context.support.DefaultLifecycleProcessor$$Lambda$675/133579455.accept(Unknown Source) ~[na:na]
    at java.lang.Iterable.forEach(Iterable.java:75) ~[na:1.8.0_25]
    at org.springframework.context.support.DefaultLifecycleProcessor.startBeans(DefaultLifecycleProcessor.java:155) ~[spring-context-5.3.20.jar:5.3.20]
    at org.springframework.context.support.DefaultLifecycleProcessor.onRefresh(DefaultLifecycleProcessor.java:123) ~[spring-context-5.3.20.jar:5.3.20]
    at org.springframework.context.support.AbstractApplicationContext.finishRefresh(AbstractApplicationContext.java:935) ~[spring-context-5.3.20.jar:5.3.20]
    at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:586) ~[spring-context-5.3.20.jar:5.3.20]
    at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:147) ~[spring-boot-2.7.0.jar:2.7.0]
    at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:734) [spring-boot-2.7.0.jar:2.7.0]
    at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:408) [spring-boot-2.7.0.jar:2.7.0]
    at org.springframework.boot.SpringApplication.run(SpringApplication.java:308) [spring-boot-2.7.0.jar:2.7.0]
    at org.springframework.boot.SpringApplication.run(SpringApplication.java:1306) [spring-boot-2.7.0.jar:2.7.0]
    at org.springframework.boot.SpringApplication.run(SpringApplication.java:1295) [spring-boot-2.7.0.jar:2.7.0]
    at com.matuto.srb.core.ServiceCoreApplication.main(ServiceCoreApplication.java:18) [classes/:na]
Caused by: java.lang.NullPointerException: null
    at springfox.documentation.spi.service.contexts.Orderings$8.compare(Orderings.java:112) ~[springfox-spi-2.9.2.jar:null]
    at springfox.documentation.spi.service.contexts.Orderings$8.compare(Orderings.java:109) ~[springfox-spi-2.9.2.jar:null]
    at com.google.common.collect.ComparatorOrdering.compare(ComparatorOrdering.java:37) ~[guava-29.0-jre.jar:na]
    at java.util.TimSort.countRunAndMakeAscending(TimSort.java:351) ~[na:1.8.0_25]
    at java.util.TimSort.sort(TimSort.java:216) ~[na:1.8.0_25]
    at java.util.Arrays.sort(Arrays.java:1438) ~[na:1.8.0_25]
    at com.google.common.collect.Ordering.sortedCopy(Ordering.java:842) ~[guava-29.0-jre.jar:na]
    at springfox.documentation.spring.web.plugins.WebMvcRequestHandlerProvider.requestHandlers(WebMvcRequestHandlerProvider.java:57) ~[springfox-spring-web-2.9.2.jar:null]
    at springfox.documentation.spring.web.plugins.DocumentationPluginsBootstrapper$2.apply(DocumentationPluginsBootstrapper.java:138) ~[springfox-spring-web-2.9.2.jar:null]
    at springfox.documentation.spring.web.plugins.DocumentationPluginsBootstrapper$2.apply(DocumentationPluginsBootstrapper.java:135) ~[springfox-spring-web-2.9.2.jar:null]
    at com.google.common.collect.Iterators$6.transform(Iterators.java:783) ~[guava-29.0-jre.jar:na]
    at com.google.common.collect.TransformedIterator.next(TransformedIterator.java:47) ~[guava-29.0-jre.jar:na]
    at com.google.common.collect.TransformedIterator.next(TransformedIterator.java:47) ~[guava-29.0-jre.jar:na]
    at com.google.common.collect.Iterators$ConcatenatedIterator.hasNext(Iterators.java:1333) ~[guava-29.0-jre.jar:na]
    at com.google.common.collect.ImmutableList.copyOf(ImmutableList.java:268) ~[guava-29.0-jre.jar:na]
    at com.google.common.collect.ImmutableList.copyOf(ImmutableList.java:232) ~[guava-29.0-jre.jar:na]
    at com.google.common.collect.FluentIterable.toList(FluentIterable.java:619) ~[guava-29.0-jre.jar:na]
    at springfox.documentation.spring.web.plugins.DocumentationPluginsBootstrapper.defaultContextBuilder(DocumentationPluginsBootstrapper.java:111) ~[springfox-spring-web-2.9.2.jar:null]
    at springfox.documentation.spring.web.plugins.DocumentationPluginsBootstrapper.buildContext(DocumentationPluginsBootstrapper.java:96) ~[springfox-spring-web-2.9.2.jar:null]
    at springfox.documentation.spring.web.plugins.DocumentationPluginsBootstrapper.start(DocumentationPluginsBootstrapper.java:167) ~[springfox-spring-web-2.9.2.jar:null]
    at org.springframework.context.support.DefaultLifecycleProcessor.doStart(DefaultLifecycleProcessor.java:178) ~[spring-context-5.3.20.jar:5.3.20]
    ... 15 common frames omitted
```

### 原因分析

请求路径与 Spring MVC 处理映射匹配的默认策略已从AntPathMatcher更改为PathPatternParser。你可以设置spring.mvc.pathmatch.matching-strategy为ant-path-matcher来改变它。

### 解决方案

在配置文件（application.properties）中加入配置：

```properties
spring.mvc.pathmatch.matching-strategy=ant-path-matcher
```
