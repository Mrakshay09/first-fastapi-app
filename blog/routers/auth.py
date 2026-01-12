from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm

from blog import schemas
from blog.database import get_db
from sqlalchemy.orm import Session
from ..repository import user as user_repository 
from ..auth import jwt_util

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), db: Session = Depends(get_db)):
    user = user_repository.get_user_by_username(request.username,request.password, db)
    # generate jwt token 
    access_token_expires = timedelta(minutes=jwt_util.ACCESS_TOKEN_EXPIRE_MINUTES)
    roles = ["editor"] 
    data={
            "sub": user.username,
            "roles": roles
        }
    access_token = jwt_util.create_access_token(
        data, expires_delta=access_token_expires
    )
    return schemas.TokenInfo(access_token=access_token, token_type="bearer")