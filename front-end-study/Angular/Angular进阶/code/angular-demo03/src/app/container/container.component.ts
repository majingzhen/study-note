import {Component, ComponentFactoryResolver, OnInit, ViewChild, ViewContainerRef} from '@angular/core';
import {OneComponent} from '../one/one.component';
import {TwoComponent} from '../two/two.component';
import {Subscription} from 'rxjs';
import {SubjectUtil} from '../utils/SubjectUtil';

@Component({
  selector: 'app-container',
  templateUrl: './container.component.html',
  styleUrls: ['./container.component.css']
})
export class ContainerComponent implements OnInit {

  // @viewChild是angular提供的装饰器，用于获得匹配的元素，这里获取在页面写的#nameRoom
  @ViewChild('nameRoom', {static: true, read: ViewContainerRef }) nameRoom: ViewContainerRef;
  // 定义要动态切换的组件集
  comps = [
    {name: 'one', component: OneComponent},
    {name: 'two', component: TwoComponent}
  ];

  // 声明Subscription,用于订阅广播
  subscription: Subscription;
  constructor(
    // 引入ComponentFactoryResolver,它可以讲一个组件实例呈现到另一个组件视图上
    private cfr: ComponentFactoryResolver,
    // 引入定义的SubjectUtil工具
    private subjectUtil: SubjectUtil
  ) { }

  ngOnInit() {
    // 在初始化的时候我们先加载one组件
    const com = this.cfr.resolveComponentFactory(OneComponent);
    this.nameRoom.clear();
    this.nameRoom.createComponent(com);
    // 订阅广播的值，当值发生变化会调用这里的方法
    this.subscription = this.subjectUtil.sideObservable.subscribe((name: string) => {
      // 调用切换组件的方法
      this.switchComponent(name);
    })
  }

  /**
   * 切换组件的方法，用于切换组件
   * @param name 组件名
   */
  switchComponent(name: string) {
    // 我们首先遍历实现定义好的要动态切换的组件集，判断组件名称是否一致，一致的话切换组件
    // tslint:disable-next-line:prefer-for-of
    for (let i = 0; i < this.comps.length; i++) {
      if (this.comps[i].name === name) {
        const com = this.cfr.resolveComponentFactory(this.comps[i].component);
        this.nameRoom.clear();
        this.nameRoom.createComponent(com);
      }
    }
  }
}
