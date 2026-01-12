from fastapi import APIRouter, BackgroundTasks

from blog.config.email import send_email

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