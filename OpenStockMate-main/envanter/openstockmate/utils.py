from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.signals import user_signed_up
from django.dispatch import receiver
from django.conf import settings
from models import CustomUserManager, CustomUser

@receiver(user_signed_up)
def send_welcome_email(sender, user, request, **kwargs):
    html_message = render_to_string('welcome_email.html', {'user': user})
    subject = 'Welcome! OpenStockMate!'
    from_email = 'noreply@openstockmate.org' 
    to_email = [user.email]  

    send_mail(subject, '', from_email, to_email, html_message=html_message)
