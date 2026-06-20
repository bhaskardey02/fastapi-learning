from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas

router = APIRouter()


@router.get("/transactions/count")
def transaction_count(db: Session = Depends(get_db)):
    return {
        "total_transactions": crud.get_transaction_count(db)
    }


@router.get("/frauds/count")
def fraud_count(db: Session = Depends(get_db)):
    return {
        "fraud_transactions": crud.get_fraud_count(db)
    }


@router.get("/fraud/percentage")
def fraud_percentage(db: Session = Depends(get_db)):
    return {
        "fraud_percentage": crud.get_fraud_percentage(db)
    }


@router.get(
    "/frauds/top10",
    response_model=list[schemas.Transaction]
)
def top_frauds(db: Session = Depends(get_db)):
    return crud.get_top_frauds(db)


@router.get(
    "/hours/high-risk",
    response_model=list[schemas.HighRiskHour]
)
def high_risk_hours(db: Session = Depends(get_db)):
    return crud.get_high_risk_hours(db)


@router.get(
    "/stats",
    response_model=schemas.FraudStats
)
def fraud_stats(db: Session = Depends(get_db)):
    return crud.get_fraud_stats(db)