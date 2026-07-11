from sqlalchemy import Column, Integer, Float, String
from app.database import Base


class CreditCardTransaction(Base):
    __tablename__ = "creditcard_transactions"

    id = Column(Integer, primary_key=True, index=True)

    Time = Column(Float)
    Amount = Column(Float, index=True)
    Class = Column(Integer, index=True)
    Hour = Column(Integer, index=True)
    HighValue = Column(Integer, index=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, index=True)
    email = Column(String(150), unique=True, index=True)

    hashed_password = Column(String(255))