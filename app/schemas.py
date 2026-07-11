from pydantic import BaseModel, EmailStr


class Transaction(BaseModel):
    
    Amount: float
    Hour: int
    HighValue: int

    class Config:
        from_attributes = True


class HighRiskHour(BaseModel):
    Hour: int
    fraud_count: int

    class config:
        from_attributes = True

class FraudStats(BaseModel):
    total_transactions: int
    fraud_transactions: int
    fraud_percentage: float

    class config:
        from_attributes = True
    
class TransactionDetail(BaseModel):
    id: int
    Time: float
    Amount: float
    Class: int
    Hour: int
    HighValue: int

    class Config:
        from_attributes = True

class TransactionSummary(BaseModel):
    id: int
    Amount: float
    Class: int
    Hour: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str