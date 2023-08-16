# Angular进阶

## 显示数据及数据绑定

本节简单的介绍下angular的数据显示及数据绑定,我们首先新建一个项目,作为演示

```bash
ng new angular-demo --routing --skip-git --skip-tests
```

将app.component.html清空

## 显示数据

​    angular 可以通过把 HTML 模板中的控件绑定到 Angular 组件的属性来显示数据。要显示组件的属性，最简单的方式就是通过插值表达式 (interpolation) 来绑定属性名。要使用插值表达式，就把属性名包裹在双花括号里放进视图模板，如 {{ name }}。

​    首先我们在 app.component.ts 中定义几个属性：

```javascript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  // 这里定义了两个属性，一个name，一个title
  title = 'angular-demo';
  name = '张三';
}
```

​    接着使用插值表达式来读取该值，将 app.component.html 修改为如下：

```html
<p>{{title}}</p>
<p>姓名是: {{name}}</p>
```

​    运行项目并访问：127.0.0.1:4200 

​    ![](F:\person\leaning\Angular\Angular进阶\img\1.png)

​    