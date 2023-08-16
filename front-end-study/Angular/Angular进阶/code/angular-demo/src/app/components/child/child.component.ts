import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.css']
})
export class ChildComponent implements OnInit {

  constructor(
    // 声明ActivatedRoute
    public route: ActivatedRoute
  ) { }

  ngOnInit() {
    // 接收父页面传来的参数
    this.route.queryParams.subscribe((res) => {
      console.log(res);
    });
  }
}
