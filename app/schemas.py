from pydantic import BaseModel


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