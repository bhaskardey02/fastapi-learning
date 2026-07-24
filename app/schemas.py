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

class PredictionRequest(BaseModel):
    Time: float

    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float

    Amount: float
    Hour: int
    HighValue: int