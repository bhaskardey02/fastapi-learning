from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas
from app.auth import get_current_user

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


@router.get("/transactions/{transaction_id}",
    response_model=schemas.TransactionDetail
)
def tranaction_by_id(transaction_id: int, db: Session = Depends(get_db)):
    transaction = crud.get_transaction_by_id(db, transaction_id)
    if transaction is None:
        raise HTTPException(
    status_code=404,
    detail="Transaction not found"
)
    
    return transaction


@router.get(
    "/transactions",
    response_model=list[schemas.TransactionSummary]
)
def transactions(
    skip: int = 0,
    limit: int = 20,
    transaction_class: int | None = None,
    hour: int | None = None,
    high_value: int | None = None,
    sort_by: str = "id",
    order: str = "asc",
    db: Session = Depends(get_db)
):
    return crud.get_transactions(
        db=db,
        skip=skip,
        limit=limit,
        transaction_class=transaction_class,
        hour=hour,
        high_value=high_value,
        sort_by=sort_by,
        order=order,
    )


@router.get(
    "/stats",
    response_model=schemas.FraudStats
)
def fraud_stats(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
    
    ):
    return crud.get_fraud_stats(db)