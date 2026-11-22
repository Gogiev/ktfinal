from celery import Celery
from app.config import settings

celery_app = Celery(
    "ktfinal", 
    broker=settings.CELERY_BROKER_URL, 
    backend=settings.CELERY_RESULT_BACKEND
)


celery_app.conf.broker_connection_retry_on_startup = True 

@celery_app.task
def send_welcome_email(email: str):
    print(f"Письмо отправлено на {email}")
    return f"Sent to {email}"