import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HomeComponent} from './components/home/home.component';
import {UserComponent} from './components/user/user.component';
import {ParentComponent} from './components/parent/parent.component';
import {ChildComponent} from './components/child/child.component';
import {LoginGuard} from './guard/login.guard';
import {UnsaveGuard} from './guard/unsave.guard';


const routes: Routes = [
  // 定义路由
  {path: '', component: HomeComponent, canDeactivate: [UnsaveGuard]},
  {path: 'user', component: UserComponent, canActivate: [LoginGuard]},
  // 父路由
  {
    path: 'parent',
    component: ParentComponent,
    // 子路由，可添加多个
    children: [
      // 动态路由传参，可以理解为占位
      {path: 'child', component: ChildComponent}
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
