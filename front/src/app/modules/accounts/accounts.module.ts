import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './components/home/home.component';
import { SharedModule } from '../shared/shared.module';


import { NgIconsModule } from '@ng-icons/core';

import { heroCalendar, heroArrowRight, heroShoppingCart } from '@ng-icons/heroicons/outline';
import { LoginComponent } from './components/login/login.component';
import { AccountRepository } from 'src/app/core/repositories/account.repository';
import { AccountRepositoryImpl } from 'src/app/infrastructure/repositories/account.repository';
import { NgxPayPalModule } from 'ngx-paypal';
import { PaymentRepository } from 'src/app/core/repositories/payment.repository';
import { PaymentRepositoryImpl } from 'src/app/infrastructure/repositories/payment.repository';

@NgModule({
  declarations: [
    HomeComponent,
    LoginComponent,
  ],
  imports: [
    CommonModule,
    SharedModule,
    NgIconsModule.withIcons({ heroCalendar,heroArrowRight ,heroShoppingCart}),
    NgxPayPalModule

  ],
  exports: [
    HomeComponent
  ],
  providers: [
    {
      provide: AccountRepository,
      useClass: AccountRepositoryImpl
    },
    {
      provide: PaymentRepository,
      useClass: PaymentRepositoryImpl
    }
  ]
})
export class AccountsModule { }
