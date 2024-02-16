from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    id: int
    account_id: int
    amount: float
    type: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    size_screen: str
    os: str
    browser: str
    device: str
    ip: str
    
    
    
    def to_save(self):
        return {
            "account_id": self.account_id,
            "amount": self.amount,
            "type": self.type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "size_screen": self.size_screen,
            "os": self.os,
            "browser": self.browser,
            "device": self.device,
            "ip": self.ip
        }
    
    
    def as_dict(self):
        return {
            "id": self.id,
            "account_id": self.account_id,
            "amount": self.amount,
            "type": self.type,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
            "size_screen": self.size_screen,
            "os": self.os,
            "browser": self.browser,
            "device": self.device,
            "ip": self.ip
        }
    
    
    @staticmethod
    def from_dict(dict):
        return Transaction(
            id = dict["id"],
            account_id = dict["account_id"],
            amount = dict["amount"],
            type = dict["type"],
            created_at = dict["created_at"],
            updated_at = dict["updated_at"],
            deleted_at = dict["deleted_at"],
            size_screen = dict["size_screen"],
            os = dict["os"],
            browser = dict["browser"],
            device = dict["device"],
            ip = dict["ip"]
        )
def transaction_factory(id, account_id, amount, type, created_at, updated_at, deleted_at, size_screen, os, browser, device, ip):
    return Transaction(id, account_id, amount, type, created_at, updated_at, deleted_at, size_screen, os, browser, device, ip)