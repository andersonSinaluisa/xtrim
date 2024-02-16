import { Component, Input } from '@angular/core';
import { AccountData } from 'src/app/core/models/account.model';

@Component({
  selector: 'app-card-account',
  templateUrl: './card-account.component.html',
  styleUrls: ['./card-account.component.css']
})
export class CardAccountComponent {

  @Input()
  accounts: AccountData['accounts'] =[]



}
