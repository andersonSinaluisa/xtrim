/*{
    "account": [
        {
            "address": "Av publica",
            "balance": "0.22",
            "city": "Guayaquil",
            "created_at": null,
            "deleted_at": null,
            "id": 88,
            "secuencial": "793572",
            "state": "Guayas",
            "updated_at": null,
            "user_id": 31
        },
        {
            "address": "Av publica",
            "balance": "0.22",
            "city": "Guayaquil",
            "created_at": null,
            "deleted_at": null,
            "id": 89,
            "secuencial": "793573",
            "state": "Guayas",
            "updated_at": null,
            "user_id": 31
        }
    ],
    "user": {
        "created_at": "Thu, 15 Feb 2024 04:30:14 GMT",
        "deleted_at": null,
        "email": "andersonsinaluisa@gmail.com",
        "first_name": "Anderson",
        "id": 31,
        "last_name": "Sinaluisa",
        "password": "$2b$12$vsfBU.G2n/dELopPH7yzFOvL/N1..Yv3JHezTazpmU3NlGb1MG3Je",
        "updated_at": null
    }
}*/

export class Account {
    constructor(
        public address: string,
        public balance: string,
        public city: string,
        public created_at: string,
        public deleted_at: string,
        public id: number,
        public secuencial: string,
        public state: string,
        public updated_at: string,
        public user_id: number
    ){}
}

class User {
    constructor(
        public created_at: string,
        public deleted_at: string,
        public email: string,
        public first_name: string,
        public id: number,
        public last_name: string,
        public password: string,
        public updated_at: string
    ){}
}


export class AccountData {
    constructor(
        public accounts: Account[],
        public user: User
    ){}
}