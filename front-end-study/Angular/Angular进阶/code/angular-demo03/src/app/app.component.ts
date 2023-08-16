import { Component } from '@angular/core';
import {SubjectUtil} from './utils/SubjectUtil';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  // 定义初始name
  private name = 'one';
  constructor(
    // 引入定义的SubjectUtil
    private subjectUtil: SubjectUtil
  ) {
  }

  /**
   * 切换组件的方法
   */
  switchComponent() {
    // 如果当前的name为one则切换到two,反之一样
    if (this.name === 'one') {
      this.subjectUtil.emitName('two');
      this.name = 'two';
    } else {
      this.subjectUtil.emitName('one');
      this.name = 'one';
    }
  }
}
