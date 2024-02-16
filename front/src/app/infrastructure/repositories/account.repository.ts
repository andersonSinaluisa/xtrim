import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AccountRepository } from '../../core/repositories/account.repository';
import { AccountData } from '../../core/models/account.model';
import { AccountService } from '../services/account.service';
import { AuthModel } from '../../core/models/auth.model';

@Injectable({
    providedIn: 'root',
})
export class AccountRepositoryImpl implements AccountRepository {
    constructor(private service: AccountService) { }
    get_by_id(): Observable<AccountData> {
        return this.service.get_by_user_id();
    }
    

    login(email: string, password: string): Observable<AuthModel> {
        return this.service.login(email, password);
    }


    calculate_balance(data: { account_id: string; amount: string; }[]): Promise<boolean> {
        return  this.service.calculate_balance(data);
    }

}