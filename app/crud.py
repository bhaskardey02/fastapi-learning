from sqlalchemy.orm import Session
from app.models import CreditCardTransaction, User
from sqlalchemy import func, asc, desc
from app.auth import hash_password, verify_password


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

def get_transaction_by_id(db: Session, transaction_id: int):
    return (
        db.query(CreditCardTransaction)
        .filter(CreditCardTransaction.id == transaction_id)
        .first()
    )


def get_transactions(
    db: Session,
    skip: int = 0,
    limit: int = 20,
    transaction_class: int | None = None,
    hour: int | None = None,
    high_value: int | None = None,
    sort_by: str = "id",
    order: str = "asc"
):
    query = db.query(CreditCardTransaction)

    # Filters
    if transaction_class is not None:
        query = query.filter(CreditCardTransaction.Class == transaction_class)

    if hour is not None:
        query = query.filter(CreditCardTransaction.Hour == hour)

    if high_value is not None:
        query = query.filter(CreditCardTransaction.HighValue == high_value)

    # Allowed columns
    columns = {
        "id": CreditCardTransaction.id,
        "Amount": CreditCardTransaction.Amount,
        "Hour": CreditCardTransaction.Hour,
        "Class": CreditCardTransaction.Class,
    }

    sort_column = columns.get(sort_by, CreditCardTransaction.id)

    if order.lower() == "desc":
        query = query.order_by(desc(sort_column))
    else:
        query = query.order_by(asc(sort_column))

    return query.offset(skip).limit(limit).all()

def create_user(db: Session, user):
    hashed_password = hash_password(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_username(db:Session, username: str):
    return (db.query(User).filter(User.username == username).first())


def get_user_by_email(db: Session, email: str):
    return (db.query(User).filter(User.email == email).first())


def authenticate_user(db: Session, username: str, password: str):
    user = (db.query(User)
            .filter(User.username == username)
            .first()
    )
    if not user:
        return None
    
    if not verify_password(
        password,
        user.hashed_password
    ):
        return None

    return user
