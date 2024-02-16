import { Observable } from "rxjs";


import { Account, AccountData } from "../models/account.model";
import { AuthModel } from "../models/auth.model";

export abstract class AccountRepository {
    abstract get_by_id(): Observable<AccountData>;

    abstract login(email: string, password: string): Observable<AuthModel>;


    abstract calculate_balance(data: {
        account_id: string;
        amount: string;
    }[]): Promise<boolean>;
}