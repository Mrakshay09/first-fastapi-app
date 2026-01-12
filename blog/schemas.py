from typing import List, Optional

from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str

class UserInBlog(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str # fields to be shown in response
    body: str
    creator: Optional[UserInBlog] = None
    class Config:
        orm_mode = True

class User(BaseModel):
    username: str
    password: str
    email: str

class ShowUser(BaseModel):
    username: str
    email: str
    blogs: List[ShowBlog] = []
    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class TokenInfo(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None