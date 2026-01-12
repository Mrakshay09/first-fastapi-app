from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas
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
