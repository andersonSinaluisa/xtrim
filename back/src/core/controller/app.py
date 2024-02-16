import os
from flask import (
    Flask,
    g,
    jsonify,
    request
)
from core.controller.account_controller import AccountController
from core.controller.user_controller import UserController
from core.infrastructure.respositories.account_repository import AccountRepository
from core.application.services.account_service import AccountService
from core.infrastructure.respositories.user_repository import UserRepository
from core.application.services.user_service import UserService
from core.infrastructure.database import (
    close_db_connection,
    init_db_engine,
    db_connect
)
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') or 'jwt-secret-string'
CORS(app)
jwt = JWTManager(app)

def get_db_connection(app):
    if 'db_con' not in g:
        db_engine = app.config.get('DB_ENGINE', None) or init_db_engine()
        g.db_con = db_connect(db_engine)
    return g.db_con


@app.teardown_appcontext
def teardown_db(exception=None):
    db_con = g.pop('db_con', None)
    if db_con is not None:
        close_db_connection(db_con)



        

        

if __name__ == '__main__':
    
    
    with app.app_context():
            
        user = UserController(conection=get_db_connection(app))
        account = AccountController(conection=get_db_connection(app))
        
        app.add_url_rule(
            '/login',
            view_func=user.login,
            methods=['POST']
        )
        app.add_url_rule(
            '/account/create',
            view_func=user.create_account,
            methods=['POST']
        )

        app.add_url_rule(
            '/account/get_by_user_id',
            view_func=user.get_by_user_id,
            methods=['GET']
        )
        
        
        app.add_url_rule(
            '/account/pay',
            view_func=account.pay,
            methods=['POST']
        )
        
        
        app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
