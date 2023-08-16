import { CanActivate } from '@angular/router';

export class LoginGuard implements CanActivate {
  canActivate() {
    // Math.random()为获取随机数
    const loggedIn: boolean = Math.random() < 0.5;
    console.log(loggedIn);
    if (!loggedIn) {
      console.log('用户未登录');
    }
    return loggedIn;
  }
}
