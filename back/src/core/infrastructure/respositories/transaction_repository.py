from core.domain.repositories.transaction_repository_interface import TransactionRepositoryInterface
from core.infrastructure.respositories.base_repository import BaseRepository
from core.infrastructure.database import transaction_table



class TransactionRepository(BaseRepository, TransactionRepositoryInterface):



    def create(self, transaction):
        transaction = None
        try:
            transaction  = self.db_connection

            result = self.db_connection.execute(
                transaction_table.insert(),
                transaction.to_save()
            )
            
            inserted_id = result.lastrowid
            row = self.db_connection.execute(
                transaction_table.select().where(transaction_table.c.id == inserted_id)
            ).fetchone()
            transaction.commit()
            return transaction.from_dict(
                {
                    "id": row[0],
                    "account_id": row[1],
                    "amount": row[2],
                    "transaction_type": row[3],
                    "created_at": row[4],
                    "updated_at": row[5],
                    "deleted_at": row[6]
                }
            )
        except Exception as e:
            if transaction:
                transaction.rollback()
            raise e