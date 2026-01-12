from blog.config.email import send_email
from fastapi import APIRouter, Depends, HTTPException,status,BackgroundTasks
from email.message import EmailMessage

router = APIRouter(
   tags=["email"],
   prefix="/email"
)


@router.post("/trigger-email")
def trigger_email(
    email: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        send_email,
        email,
        "FastAPI Email Trigger",
        "This email was triggered via FastAPI 🚀"
    )
    return {"message": "Email triggered successfully"}