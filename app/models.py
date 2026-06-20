from sqlalchemy import Column, Integer, Float
from app.database import Base


class CreditCardTransaction(Base):
    __tablename__ = "creditcard_transactions"

    Time = Column(Float, primary_key=True)

    Amount = Column(Float, index=True)
    Class = Column(Integer, index=True)
    Hour = Column(Integer, index=True)
    HighValue = Column(Integer, index=True)