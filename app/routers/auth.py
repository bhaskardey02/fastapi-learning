from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database import get_db
from app import crud, schemas
from app.auth import create_access_token



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
    )

@router.post("/register",
             response_model=schemas.UserResponse)
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    if crud.get_user_by_username(db, user.username):
        raise HTTPException(
            status_code=400, 
            detail="Username already registered"
        )
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    return crud.create_user(db, user)


@router.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    
    db: Session = Depends(get_db)
):
    db_user = crud.authenticate_user(db, form_data.username, form_data.password)
    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    token = create_access_token(
        data ={
            "sub": db_user.username
            }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }