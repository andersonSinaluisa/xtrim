import { ICreateOrderRequest } from "ngx-paypal";
import { ItemsPayment } from "../models/paymen.model";



export class PaymentMapper {
    static fromDomainToDto(items: ItemsPayment[], total: number) {
        return {
            currency: 'USD',
            clientId: 'sb',
            createOrderOnClient: () => <ICreateOrderRequest>{
                intent: 'CAPTURE',
                purchase_units: [
                    {
                        amount: {
                            currency_code: 'USD',
                            value: total.toString(),
                            breakdown: {
                                item_total: {
                                    currency_code: 'USD',
                                    value: total.toString(),
                                }
                            }
                        },
                        items: [
                            ...items.map(item => {
                                return {
                                    name: item.name,
                                    quantity: item.quantity.toString(),
                                    category: item.category,
                                    unit_amount: {
                                        currency_code: item.currency_code,
                                        value: item.price.toString(),
                                    },
                                    sku: item.id,
                                }
                            }
                            )
                        ]
                    }
                ]
            }
        }
    }
}