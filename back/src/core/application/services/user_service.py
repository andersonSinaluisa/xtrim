from core.domain.models.user import User, user_factory
from core.domain.repositories.user_repository_interface import UserRepositoryInterface
from core.infrastructure.respositories.user_repository import UserRepository 
import bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

class UserService:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, user_data):
        # Aquí podrías tener lógica adicional si es necesario antes de guardar el usuario
        if 'first_name' not in user_data:
            raise ValueError('El nombre es requerido "first_name"')
        if 'last_name' not in user_data:
            raise ValueError('El apellido es requerido "last_name"')
        if 'email' not in user_data:
            raise ValueError('El email es requerido "email"')
        if 'password' not in user_data:
            raise ValueError('La contraseña es requerida "password"')
        
        is_exist = self.user_repository.get_user_by_email(user_data['email'])
        if is_exist:
            raise ValueError('El email ya existe')
        password = user_data['password']
        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user_data['password'] = password.decode('utf-8')
        new_user = user_factory(**user_data)
        return self.user_repository.create(new_user)
        # Otra lógica después de guardar el usuario, si es necesario
        
        
        
    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)




    def login(self, data):
        
        if 'email' not in data:
            raise ValueError('El email es requerido "email"')
        
        if 'password' not in data:
            raise ValueError('La contraseña es requerida "password"')
        
        email = data['email']
        password = data['password']
        validate = self.user_repository.validate_credentials(email, password)
        user = self.user_repository.get_user_by_email(email)
        if validate:
            access_token = create_access_token(identity=user.id)
            
            return {
                "access_token": access_token,
                'email': email
            }
            
        raise ValueError('Usuario o contraseña incorrectos')
        