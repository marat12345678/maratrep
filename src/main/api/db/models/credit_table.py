from src.main.api.db.base import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float

class Credit(Base):
    __tablename__ = 'credit'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    term_months = Column(Integer, nullable=False)
    balance = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)


    def __repr__(self):
        return f'<Credit {self.account_id}>, term_month{self.term_months}, balance{self.balance}>'