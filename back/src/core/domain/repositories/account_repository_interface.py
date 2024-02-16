from abc import (
    ABCMeta,
    abstractmethod
)

from core.domain.models.account import Account

class AccountRepositoryInterface:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def create(self, account):
        raise NotImplementedError
    
    
    @abstractmethod
    def get_account_by_user_id(self, user_id):
        raise NotImplementedError
    
    @abstractmethod
    def generate_account_number(self):
        raise NotImplementedError
    
    
    @abstractmethod
    def get_account_by_id(self, account_id):
        raise NotImplementedError
    
    @abstractmethod
    def pay(self, account:Account, amount):
        raise NotImplementedError