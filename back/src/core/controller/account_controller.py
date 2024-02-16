from core.application.services.account_service import AccountService
from core.infrastructure.respositories.account_repository import AccountRepository
from sqlalchemy import Connection
from flask import jsonify, request


class AccountController:
    
    
    def __init__(self, conection:Connection) -> None:
        self.account_repository = AccountRepository(conection)



    def pay(self):
        try:
            data = request.json
            AccountService(
                account_repository=self.account_repository
            ).pay(data)
            return jsonify({'message': 'Pago exitoso'}), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    
    