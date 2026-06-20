from sqlalchemy.orm import Session
from app.models import CreditCardTransaction
from sqlalchemy import func


def get_transaction_count(db: Session):
    return db.query(CreditCardTransaction).count()

def get_fraud_count(db: Session):
    return (
        db.query(CreditCardTransaction)
        .filter(CreditCardTransaction.Class == 1)
        .count()
    )

def get_fraud_percentage(db: Session):
    total_transactions = (
        db.query(CreditCardTransaction).count()
    )
    
    fraud_transactions = (
        db.query(CreditCardTransaction).filter(CreditCardTransaction.Class == 1).count()

    )

    return round(
        (fraud_transactions / total_transactions) * 100, 4
    )
    
def get_top_frauds(db: Session):
    return (
        db.query(CreditCardTransaction)
        .filter(CreditCardTransaction.Class == 1)
        .order_by(CreditCardTransaction.Amount.desc())
        .limit(10)
        .all()
    )

def get_high_risk_hours(db: Session):
    return (
        db.query(
            CreditCardTransaction.Hour,
            func.count().label("fraud_count")
        )
        .filter(CreditCardTransaction.Class == 1)
        .group_by(CreditCardTransaction.Hour)
        .order_by(func.count().desc())
        .limit(10)
        .all()
    )

def get_fraud_stats(db: Session):
    
    total_transactions = (
        db.query(CreditCardTransaction).count()
    )

    fraud_transactions = (
        db.query(CreditCardTransaction).filter(CreditCardTransaction.Class == 1).count()
        
    )

    fraud_percentage = round(
        (fraud_transactions / total_transactions) * 100,4
        )
    
    return {
        "total_transactions": total_transactions,
        "fraud_transactions": fraud_transactions,
        "fraud_percentage": fraud_percentage
    }