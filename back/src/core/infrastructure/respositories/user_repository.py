from core.domain.models.user import User
from core.domain.repositories.user_repository_interface import UserRepositoryInterface
from core.infrastructure.database import user_table
from core.infrastructure.respositories.base_repository import BaseRepository


class UserRepository(BaseRepository, UserRepositoryInterface):

    def create(self, user: User):
        transaction = None
        try:
            transaction  = self.db_connection

            result = self.db_connection.execute(
                user_table.insert(),
                user.to_save()
            )
            
            inserted_id = result.lastrowid
            
            row = self.db_connection.execute(
                user_table.select().where(user_table.c.id == inserted_id)
            ).fetchone()
            transaction.commit()
            
            return User.from_dict({
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "password": row[4],
                "created_at": row[5],
                "updated_at": row[6],
                "deleted_at": row[7]
            })
        except Exception as e:
            if transaction:
                transaction.rollback()
            raise e
            
            
            
    def get_user_by_email(self, email):
        result = self.db_connection.execute(
            user_table.select().where(user_table.c.email == email)
        ).fetchone()
        if result:
            return User.from_dict({
                "id": result[0],
                "first_name": result[1],
                "last_name": result[2],
                "email": result[3],
                "password": result[4],
                "created_at": result[5],
                "updated_at": result[6],
                "deleted_at": result[7]
            
            })
        return None
    
    
    
    def get_user_by_id(self, user_id):
        result = self.db_connection.execute(
            user_table.select().where(user_table.c.id == user_id)
        ).fetchone()
        if result:
            return User.from_dict({
                "id": result[0],
                "first_name": result[1],
                "last_name": result[2],
                "email": result[3],
                "password": result[4],
                "created_at": result[5],
                "updated_at": result[6],
                "deleted_at": result[7]
            })
        return None
    
    
    
    def validate_credentials(self, email, password):
        data = self.db_connection.execute(
            user_table.select().where(
                user_table.c.email == email
            ) 
        ).fetchone()
        
        
        pass_db = data[4]
        return User.check_password(pass_db, password)
        