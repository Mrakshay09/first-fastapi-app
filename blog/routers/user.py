from datetime import timedelta
from fastapi import APIRouter, Depends

from blog.auth.jwt_util import ACCESS_TOKEN_EXPIRE_MINUTES
from .. import schemas
from sqlalchemy.orm import Session
from fastapi import Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user as user_repository


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("/", response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = user_repository.create(request, db)
    return new_user

@router.get("/{user_id}",response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def getUser(user_id:int ,db:Session= Depends(get_db)):
    user = user_repository.user(user_id,db)
    return user
