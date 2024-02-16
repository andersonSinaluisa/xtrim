from dataclasses import dataclass
from datetime import datetime


@dataclass
class Account:
    id: str
    user_id: int
    balance: float
    secuencial: str
    city: str
    state: str
    address: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    
    
    def as_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "balance": self.balance,
            "secuencial": self.secuencial,
            "city": self.city,
            "state": self.state,
            "address": self.address,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at
        }
    def to_save(self):
        return {
            "user_id": self.user_id,
            "balance": self.balance,
            "secuencial": self.secuencial,
            "city": self.city,
            "state": self.state,
            "address": self.address,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at
        }
    
    
    @staticmethod
    def from_dict(row):
        return Account(**row)
def account_factory(**kwargs):
    return Account(
        id=kwargs.get("id") if kwargs.get("id") else None,
        user_id=kwargs.get("user_id"),
        balance=kwargs.get("balance"),
        secuencial=kwargs.get("secuencial"),
        city=kwargs.get("city"),
        state=kwargs.get("state"),
        address=kwargs.get("address"),
        created_at=kwargs.get("created_at"),
        updated_at=kwargs.get("updated_at"),
        deleted_at=kwargs.get("deleted_at")
    )