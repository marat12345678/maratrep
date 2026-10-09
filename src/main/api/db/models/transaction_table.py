from src.main.api.db.base import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, String

class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    to_account_id = Column(Integer, ForeignKey('account.id'))
    from_account_id = Column(Integer, ForeignKey('account.id'))
    credit_id = Column(Integer, ForeignKey('credit.id'))
    amount = Column(Float, nullable=False)
    transaction_type = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)



