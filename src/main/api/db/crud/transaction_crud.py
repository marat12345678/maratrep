

from sqlalchemy.orm import Session

from src.main.api.db.models.transaction_table import Transaction


class TransactionCrud:
    @staticmethod
    def get_by_from_account_id(db: Session, from_account_id: int, to_account_id:int, amount:int) -> Transaction|None:
        return db.query(Transaction).filter_by(from_account_id=from_account_id, to_account_id=to_account_id, amount = amount).first()
