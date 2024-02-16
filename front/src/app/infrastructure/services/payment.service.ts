import { Injectable } from "@angular/core";
import { PaymentMapper } from "../../core/mappers/payment.mapper";
import { ItemsPayment } from "../../core/models/paymen.model";
import { IClientAuthorizeCallbackData, IPayPalConfig } from "ngx-paypal";

@Injectable({
    providedIn: 'root'
})

export class PaymentService{
    
    constructor() { }


    pay(items: ItemsPayment[], total: number, onAction:(type:string,message:string,data:IClientAuthorizeCallbackData|null)=>void):IPayPalConfig {
        return {
           ...PaymentMapper.fromDomainToDto(items, total),
            advanced: {
              commit: 'true'
            },
            style: {
              label: 'paypal',
              layout: 'vertical'
            },
            onApprove: (data, actions) => {
              actions.order.get().then((details:any) => {
                onAction(
                    'onApprove',
                    'La transacción fue aprobada, pero no autorizada',
                    null
                )
              });
            },
            onClientAuthorization: (data) => {
                console.log('onClientAuthorization',data);
                onAction(
                    'onClientAuthorization',
                    'Valores de transacción completados en este punto',
                    data
                )
            },
            onCancel: (data, actions) => {
                onAction(
                    'onCancel',
                    'Transacción cancelada',
                    null
                )
            },
            onError: err => {
                onAction(
                    'onError',
                    'Error en la transacción',
                    null
                )
            },
            onClick: (data, actions) => {
                onAction(
                    'onClick',
                    'Transacción en proceso',
                    null
                )
            },
          };
    }
    
}