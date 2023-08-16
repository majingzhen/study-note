import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.css']
})
export class ChildComponent implements OnInit {

  // 定义一个输入属性，用来接收父组件传来的值，通常使用 @Input装饰器
  @Input() content: string;
  constructor() { }

  ngOnInit() {
  }

}
