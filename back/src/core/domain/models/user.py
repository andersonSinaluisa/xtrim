from dataclasses import dataclass
from datetime import datetime
import  bcrypt

@dataclass
class User:
    id:str
    first_name: str
    last_name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    
    
    
    
    def to_save(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
        }
    
    def as_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at
        }

    @staticmethod
    def from_dict(dict):
        return user_factory(
            id=dict["id"],
            first_name=dict["first_name"],
            last_name=dict["last_name"],
            email=dict["email"],
            password=dict["password"],
            created_at=dict["created_at"],
            updated_at=dict["updated_at"],
            deleted_at=dict["deleted_at"]
        )
        
        
    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    @staticmethod
    def check_password(passdb, password):
        return bcrypt.checkpw(password.encode('utf-8'), passdb.encode('utf-8'))
    

def user_factory(**kwargs):
    
    
    return User(
        id=kwargs.get("id") if kwargs.get("id") else None,
        first_name=kwargs.get("first_name"),
        last_name=kwargs.get("last_name"),
        email=kwargs.get("email"),
        password=kwargs.get("password"),
        created_at=kwargs.get("created_at") if kwargs.get("created_at") else datetime.now(),
        updated_at=kwargs.get("updated_at") if kwargs.get("updated_at") else None,
        deleted_at=kwargs.get("deleted_at") if kwargs.get("deleted_at") else None
    )