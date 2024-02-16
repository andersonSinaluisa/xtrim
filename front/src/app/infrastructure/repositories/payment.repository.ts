import { Injectable } from "@angular/core";
import { PaymentRepository } from "../../core/repositories/payment.repository";
import { PaymentService } from "../services/payment.service";
import { ItemsPayment } from "src/app/core/models/paymen.model";
import { IClientAuthorizeCallbackData, IPayPalConfig } from "ngx-paypal";

@Injectable({
    providedIn: 'root',
})

export class PaymentRepositoryImpl implements PaymentRepository {
    constructor(private service: PaymentService) { }
    pay(items: ItemsPayment[], total: number, onAction:(type:string,message:string,data:IClientAuthorizeCallbackData|null)=>void): IPayPalConfig {
        return this.service.pay(items, total, onAction);
    }
}