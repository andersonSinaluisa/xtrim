import { IClientAuthorizeCallbackData, IPayPalConfig } from "ngx-paypal";
import { ItemsPayment } from "../models/paymen.model";


export abstract class PaymentRepository{
    abstract pay(items: ItemsPayment[],total: number, onAction:(type:string,message:string,data:IClientAuthorizeCallbackData|null)=>void): IPayPalConfig;
}