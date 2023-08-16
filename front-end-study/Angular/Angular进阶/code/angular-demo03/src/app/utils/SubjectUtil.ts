import {Injectable} from '@angular/core';
import {Subject} from 'rxjs';

/**
 * 定义Subject工具集，用于广播全局性数据
 */
@Injectable()
export class SubjectUtil {

  private nameSource = new Subject();
  // 获得一个Observable;
  sideObservable = this.nameSource.asObservable();

  // 发射数据，当调用这个方法的时候，Subject就会发射这个数据，所有订阅了这个Subject的Subscription都会接受到结果
  // 如:thissubjectUtile.name('哈哈哈');
  emitName(name: string) {
    this.nameSource.next(name);
  }
}
