

from core.domain.models.account import Account
from core.domain.repositories.account_repository_interface import AccountRepositoryInterface
from core.infrastructure.respositories.base_repository import BaseRepository
from core.infrastructure.database import account_table
import random

class AccountRepository(BaseRepository, AccountRepositoryInterface):
    
    
    def create(self, account):
        transaction = None
        try:
            transaction  = self.db_connection

            result = self.db_connection.execute(
                account_table.insert(),
                account.to_save()
            )
            
            inserted_id = result.lastrowid
            row = self.db_connection.execute(
                account_table.select().where(account_table.c.id == inserted_id)
            ).fetchone()
            transaction.commit()
            return account.from_dict(
                {
                    "id": row[0],
                    "user_id": row[1],
                    "balance": row[2],
                    "secuencial": row[3],
                    "city": row[4],
                    "state": row[5],
                    "address": row[6],
                    "created_at": row[7],
                    "updated_at": row[8],
                    "deleted_at": row[9]
                }
            )
        except Exception as e:
            if transaction:
                transaction.rollback()
            raise e
        
        
        
    
            
    def get_account_by_user_id(self, user_id):
        query = account_table.select().where(account_table.c.user_id == user_id)
        result = self.db_connection.execute(query)
        account = result.fetchall()
        if not account:
            return None
        for row in account:
            yield Account.from_dict(
                {
                    "id": row[0],
                    "user_id": row[1],
                    "balance": row[2],
                    "secuencial": row[3],
                    "city": row[4],
                    "state": row[5],
                    "address": row[6],
                    "created_at": row[7],
                    "updated_at": row[8],
                    "deleted_at": row[9]
                }
            )
    
    
    def generate_account_number(self):
        query = account_table.select().order_by(account_table.c.id.desc()).limit(1)
        result = self.db_connection.execute(query)
        account = result.fetchone()
        if not account:
            return random.randint(100000, 999999)
        return int(account[3]) + 1
    
    
    
    def get_account_by_id(self, account_id):
        query = account_table.select().where(account_table.c.id == account_id)
        result = self.db_connection.execute(query)
        account = result.fetchone()
        if not account:
            return None
        return Account.from_dict(
            {
                "id": account[0],
                "user_id": account[1],
                "balance": account[2],
                "secuencial": account[3],
                "city": account[4],
                "state": account[5],
                "address": account[6],
                "created_at": account[7],
                "updated_at": account[8],
                "deleted_at": account[9]
            }
        )
    def pay(self, account:Account, amount):
        transaction = None
        try:
            new_balance =  float(account.balance) - float(amount)
            if new_balance < 0:
                new_balance = 0
            query = account_table.update().where(account_table.c.id == account.id).values(balance=new_balance)
            self.db_connection.execute(query)
        except Exception as e:
            raise e
        return True
    
    