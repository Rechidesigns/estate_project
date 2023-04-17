from django.contrib.auth import get_user_model

from django.core.mail import send_mail

# from config import celery_app
# from celery import shared_task
# from config.celery import celery_app


user = get_user_model()


# @celery_app.task()
def send_otp_email_func( email, otp_pin ):
    """sending email notification"""
    send_mail(
        'OTP Verification',
        f'this is your otp pin for email verification, pin :: {otp_pin}',
        f'{email}',
        ['to@example.com'],
        fail_silently= False,
    )

    return "Done"


