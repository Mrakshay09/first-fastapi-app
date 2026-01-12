

from fastapi import HTTPException, status

from blog import models
from blog.hashing import Hash


def create(request, db):
    # hashed_password = password_hash.hash(request.password)
    # by using hashing.py
    hashed_password = Hash.bcrypt_password(request.password)
    new_user = models.User(username=request.username, password=hashed_password, email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def user(user_id: int, db):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User with the id {} not found".format(user_id))
    return user

def get_user_by_username(username: str,password:str, db):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Credentials")
    if not Hash.verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect Password")
    
    return user

    