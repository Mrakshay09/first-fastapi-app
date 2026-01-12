
from fastapi import HTTPException,status
from blog import models
from sqlalchemy.orm import Session


def get_all_blogs(db: Session):
    blogs= db.query(models.Blog).all()
    return blogs

def create(request: models.Blog, db: Session):
    new_blog = models.Blog(title=request.title,body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def update(blog_id: int, request: models.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog with the id {} not found".format(blog_id))
    blog.title = request.title
    blog.body = request.body
    db.add(blog)
    db.commit()
    db.refresh(blog)

def delete(blog_id: int, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog with the id {} not found".format(blog_id))
    db.delete(blog)
    db.commit()

def get_blog(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog with the id {} not found".format(blog_id))
    return blog