import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.css']
})
export class ParentComponent implements OnInit {

  constructor(
    // 引入路由
    public router: Router
  ) { }

  ngOnInit() {
  }

  /**
   * 打开子页面并携带id
   */
  toChild() {
    // 跳转路径 实现的是动态跳转数据
    this.router.navigate(['/parent/child/'], {queryParams: {id: '666'}});
  }
}
