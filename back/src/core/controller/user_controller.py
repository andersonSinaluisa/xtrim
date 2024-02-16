



from flask import jsonify, request
from sqlalchemy import Connection
from core.application.services.account_service import AccountService
from core.application.services.user_service import UserService
from core.infrastructure.respositories.account_repository import AccountRepository

from core.infrastructure.respositories.user_repository import UserRepository
from flask_jwt_extended import jwt_required, get_jwt_identity

class UserController:
    
    def __init__(self, conection:Connection) -> None:
        self.user_repository = UserRepository(conection)
        self.account_repository = AccountRepository(conection)
        
        
    
    def create_account(self):
        try:
            data = request.json
            user = UserService(user_repository=self.user_repository).create_user(data)
            
            data['user_id'] = user.id
            accounts = data.get('accounts', [])
            result_accounts = []
            
            for account in accounts:
                account['user_id'] = user.id
                account_row = AccountService(
                    account_repository=self.account_repository
                ).create_account(account)
                result_accounts.append(account_row)
            
            
            return jsonify({
                'user': user,
                'account': result_accounts
            }), 201
            
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    
    @jwt_required()
    def get_by_user_id(self):
        user_id = get_jwt_identity()
        accounts = AccountService(
            account_repository=self.account_repository
        ).get_by_user_id(user_id)
        user = UserService(
            user_repository=self.user_repository
        ).get_user_by_id(user_id)
        
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        if not accounts:
            accounts = []
        
        return jsonify({
            'accounts': [account.as_dict() for account in accounts],
            'user': user.as_dict()
        }), 200
        
        
    def login(self):
        data = request.json
        
        try:
            result = UserService(
                user_repository=self.user_repository
            ).login(data)
            return jsonify(result), 200
        
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': 'Usuario o contraseña incorrecta'}), 401