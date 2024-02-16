import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map } from 'rxjs';
import { environment } from 'src/environments/environment';
import { AccountData } from '../../core/models/account.model';
import { AuthModel } from '../../core/models/auth.model';

@Injectable({
    providedIn: 'root'
})
export class AccountService {
    private readonly compareUrl = environment.API_URL + '/account/get_by_user_id';

    constructor(private http: HttpClient) { }


    get_by_user_id(): Observable<AccountData> {
        return this.http.get<AccountData>(this.compareUrl, {

            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('token')
            }
        })
    }


    login(email: string, password: string): Observable<AuthModel> {
        return this.http.post<AuthModel>(environment.API_URL + '/login', {
            email: email,
            password: password
        })
    }

    async calculate_balance(data: { account_id: string; amount: string; }[]) {
        try {
            let res = await this.http.post<{ message: string }>(environment.API_URL + '/account/pay', data, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('token')
                }
            }).toPromise();
            return true;
        } catch (e) {
            return false;
        }
    }


    isLogged(): boolean {
        return localStorage.getItem('token') !== null;
    }
}
