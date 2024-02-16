import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-banner-hello',
  templateUrl: './banner-hello.component.html',
  styleUrls: ['./banner-hello.component.css']
})
export class BannerHelloComponent {


  @Input()
  welcome_message:string = 'Hello';
  @Input()
  date:string = '00/00/0000';

  @Input()
  hour:string = '00:00:00';
}
