import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from './components/navbar/navbar.component';
import { BannerComponent } from './components/banner/banner.component';
import { CardAccountComponent } from './components/card-account/card-account.component';
import { CardInfoComponent } from './components/card-info/card-info.component';
import { CardAdsComponent } from './components/card-ads/card-ads.component';
import { CardContactComponent } from './components/card-contact/card-contact.component';
import { BannerHelloComponent } from './components/banner-hello/banner-hello.component';
import { NgIconsModule } from '@ng-icons/core';
import {  heroChevronRight, heroUserCircle, heroBell, heroArrowTopRightOnSquare } from '@ng-icons/heroicons/outline';
import { ModalComponent } from './components/modal/modal.component';



@NgModule({
  declarations: [
    NavbarComponent,
    BannerComponent,
    CardAccountComponent,
    CardInfoComponent,
    CardAdsComponent,
    CardContactComponent,
    BannerHelloComponent,
    ModalComponent
  ],
  imports: [
    CommonModule,
    NgIconsModule.withIcons({ heroChevronRight, heroBell, heroUserCircle, heroArrowTopRightOnSquare }),

  ],
  exports: [
    NavbarComponent,
    BannerComponent,
    CardAccountComponent,
    CardInfoComponent,
    CardAdsComponent,
    CardContactComponent,
    BannerHelloComponent,
    ModalComponent
  ]
})
export class SharedModule { }
