import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ContainerComponent } from './container/container.component';
import { OneComponent } from './one/one.component';
import { TwoComponent } from './two/two.component';
import {SubjectUtil} from './utils/SubjectUtil';

@NgModule({
  declarations: [
    AppComponent,
    ContainerComponent,
    OneComponent,
    TwoComponent
  ],
  entryComponents: [
    // 注入one组件
    OneComponent,
    TwoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    // 注入SubjectUtil
    SubjectUtil
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
