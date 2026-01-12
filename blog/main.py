from fastapi import FastAPI

from blog.routers import email

from . import models
from .database import engine
from .routers import auth, blog, user

app = FastAPI()
app.include_router(user.router)
app.include_router(blog.router)
app.include_router(auth.router)
app.include_router(email.router)

models.Base.metadata.create_all(bind=engine)
