

export class ItemsPayment{

    constructor(
        public name: string,
        public quantity: number,
        public category: string,
        public price: number,
        public currency_code: string,
        public id: string
    ){}
}