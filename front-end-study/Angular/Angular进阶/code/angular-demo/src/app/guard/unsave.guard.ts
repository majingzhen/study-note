import { CanDeactivate } from '@angular/router';
import { HomeComponent } from '../components/home/home.component';

export class UnsaveGuard implements CanDeactivate<HomeComponent> {
  // 第一个参数 范型类型的组件
  // 根据当前要保护组件 的状态 判断当前用户是否能够离开
  canDeactivate(component: HomeComponent) {
    return window.confirm('你还没有保存，确定要离开吗？');
  }
}
