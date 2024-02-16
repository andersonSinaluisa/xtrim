

from core.domain.models.account import account_factory
from core.domain.repositories.account_repository_interface import AccountRepositoryInterface


class AccountService:
    def __init__(self, account_repository: AccountRepositoryInterface):
        self.account_repository = account_repository
        
    def create_account(self, account_data):
        
        if 'user_id' not in account_data:
            raise ValueError('El user_id es requerido "user_id"')
        
        if 'balance' not in account_data:
            raise ValueError('El balance es requerido "balance"')
        
        if 'city' not in account_data:
            raise ValueError('La ciudad es requerida "city"')
        
        if 'state' not in account_data:
            raise ValueError('El estado es requerido "state"')
        
        if 'address' not in account_data:
            raise ValueError('La dirección es requerida "address"')
        number_account = self.account_repository.generate_account_number()

        data = {
            "user_id": account_data['user_id'],
            "balance": account_data['balance'],
            "city": account_data['city'],
            "state": account_data['state'],
            "address": account_data['address'],
            "secuencial": f"{number_account}",
        
        }
        
        
        account = account_factory(**data)
        return self.account_repository.create(account)
        
        
    def get_by_user_id(self, user_id):
        return self.account_repository.get_account_by_user_id(user_id)
    
    
    
    def pay(self, data):
        
        input_data = data
        
        
        
        if not isinstance(input_data, list):
            raise ValueError('El account_id debe ser una lista')
        
        for account_id in input_data:
            if 'account_id' in account_id and 'amount' in account_id:
                account = self.account_repository.get_account_by_id(account_id.get('account_id'))
                if not account:
                    raise ValueError(f'La cuenta con el id {account_id.get("account_id")} no existe')
                
                self.account_repository.pay(account, account_id['amount'])
                
            