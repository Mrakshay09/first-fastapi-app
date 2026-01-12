from fastapi import APIRouter, Depends
from typing import List

from blog.auth.oauth2 import get_current_user, require_roles
from .. import schemas, database
from sqlalchemy.orm import Session
from fastapi import Depends, status, Response
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..repository import blog as blog_repository


router = APIRouter(
   tags=["Blogs"],
   prefix="/blog"
)

# Get all blogs
# List[schemas.ShowBlog] means we are returning a list of ShowBlog schema
@router.get("/", response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session= Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog_repository.get_all_blogs(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    new_blog = blog_repository.create(request, db)
    return {"message": "New Blog created successfully. Title: {}, Body: {}, ID: {}".format(new_blog.title, new_blog.body, new_blog.id)}

@router.put("/{blog_id}",status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id:int,request: schemas.Blog, 
                db:Session= Depends(get_db), 
                # current_user: schemas.User = Depends(get_current_user)
                current_user = Depends(require_roles(["admin"]))
                ):
    blog_repository.update(blog_id, request, db)
    return {"message": "Blog with id {} updated successfully".format(blog_id)}

@router.delete("/{blog_id}", status_code=status.HTTP_200_OK)
def delete_blog(blog_id: int, db:Session= Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog_repository.delete(blog_id, db)
    return {"message": "Blog with id {} deleted successfully".format(blog_id)}


@router.get("/{blog_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog(blog_id: int,response : Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = blog_repository.get_blog(blog_id, db)
    return blog


