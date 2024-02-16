import json
import os
import bcrypt
import random
def read_json_file():
    #"/back/src/core/controller/app.py"
    #"/back/src/data/mock.json"
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    with open(os.path.join(path, 'data/mock.json')) as file:
        data = file.read()
    
    return json.loads(data)


def generate_account_number(account_table,db_engine):
    query = account_table.select().order_by(account_table.c.id.desc()).limit(1)
    result = db_engine.execute(query)
    account = result.fetchone()
    if not account:
        return random.randint(100000, 999999)
    return int(account[3]) + 1

def mock_data(user_table,account_table,db_engine):
    mock = read_json_file()
    for account in mock:
        
        result = db_engine.execute(
            user_table.insert().values(
            first_name=account['first_name'],
            last_name=account['last_name'],
            email=account['email'],
            password=bcrypt.hashpw(account['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        ))
        
        print(result)
        inserted_id = result.lastrowid

        
        
        
        for c in account['accounts']:
        
            db_engine.execute(account_table.insert().values(
                user_id=inserted_id,
                balance=c['balance'],
                secuencial=generate_account_number(account_table,db_engine),
                city=c['city'],
                state=c['state'],
                address=c['address']
            ))