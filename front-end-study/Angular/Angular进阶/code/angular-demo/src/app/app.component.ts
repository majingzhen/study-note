import { Component } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(
    // 声明路由
    public router: Router
  ) {
  }
  /**
   * 跳转父页面按钮点击事件
   */
  toParent() {
    this.router.navigateByUrl('/parent');
  }
}
