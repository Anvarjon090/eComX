from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from celery import shared_task


@shared_task
def send_email(subject, intro_text, email, token, template, password=None):
    subject = subject
    to_email = email
    context = {
        "subject": subject,
        "intro_text": intro_text,
        "token": token,
        "password": password,
        "frontend_url": "voocommerce.com",
    }
    html_content = render_to_string(template, context)
    email = EmailMessage(subject, html_content, to=[to_email])
    email.content_subtype = "html"
    email.send()
