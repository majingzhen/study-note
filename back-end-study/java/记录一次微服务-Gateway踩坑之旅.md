# gateway 踩坑之旅

最近尝试拾起 SpringCloud 相关的知识，重新开始搭建微服务架构，再进行到 gateway 网关配置的时候，发生了一点小插曲，记录一下。

先贴出 gateway 及 system 服务的相关代码及配置

```yaml
server:
  port: 9092
spring:
  application:
    name: gateway
  cloud:
    gateway:
      discovery:
        locator:
          enabled: true
          lower-case-service-id: true
      routes:
        - id : hai
          uri: http://127.0.0.1:9091
          predicates:
            - Path=/system/**
eureka:
  client:
    # 表示是否将自己注册进eurekaServer,默认为true
    register-with-eureka: true
    # 是否从EurekaServer抓取已有的注册信息，默认为true.单节点无所谓，集群必须设置为true才能配合ribbon使用负载均衡
    fetchRegistry: true
    service-url:
      # 本机入住eurekaServer 地址
      defaultZone: http://localhost:8761/eureka
```

```java
@SpringBootApplication(exclude = DataSourceAutoConfiguration.class)
@EnableEurekaClient
public class GatewayApplication {
    public static void main(String[] args) {
        SpringApplication.run(GatewayApplication.class, args);
    }
}
```

```xml
<dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-gateway</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
    </dependencies>
```

```java
@RestController
public class TestController {

    @RequestMapping("/system/test")
    public String test() {
        return "success";
    }
}
```

```yaml
# 服务名称
spring:
  application:
    name: hai

# 端口
server:
  port: 9091
#  servlet:
#    context-path: /system
  error:
    whitelabel:
      enabled: false
# 注册中心
eureka:
  client:
    service-url:
      defaultZone: http://localhost:8761/eureka/
```

```xml
<dependencies>
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
```

配置服务的时候一切正常，但是配置了路由转发之后，发现不生效。

按照正常情况

访问系统服务：http://127.0.0.1:9091/system/test  正常

访问路由服务：http://127.0.0.1:9092/system/test  应该也是正常的，但是一直报错404 查不到原因

后来尝试了多种方式：

1.修改 gateway 网关服务的配置

```yaml
routes:
  - id : hai
      uri: lb://hai
      predicates:
          - Path=/system/**
```

根据服务名去匹配

2.检查 SpringBoot 及 SpringCloud 版本问题

在SpringCloud官网（<https://spring.io/projects/spring-cloud>）可以看到描述SpringCloud发布版本与SpringBoot版本兼容性的表格

或者可以去 SpringCloud 参考文档推荐使用的SpringBoot版本

检查之后发现也没有问题。

后来在其他电脑上进行了一组服务搭建，发现没有问题，对比之后发现，代码、配置、pom依赖都没有任何区别。

开始尝试使用玄学解决问题，将 gateway 的端口号修改为 9090

这时发现了一个问题，gateway 网关服务启动后，控制台打印出的端口号，还是 9092 不是我们在配置文件中配置的 9090 

该配置文件没生效，配置的内容没能覆盖默认配置

最终解决方案如下：

mvn clean compile

mvn install
