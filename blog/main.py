from blog.routers import email
from fastapi import Depends, FastAPI, status, Response,HTTPException

from blog.hashing import Hash
from . import models, schemas, hashing
from .database import engine,get_db
from sqlalchemy.orm import Session
from typing import List
from pwdlib import PasswordHash
from .routers import blog, user, auth

app = FastAPI()
app.include_router(user.router)
app.include_router(blog.router)
app.include_router(auth.router)
app.include_router(email.router)

models.Base.metadata.create_all(bind=engine)
