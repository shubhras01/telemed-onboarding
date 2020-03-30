from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def sendmail(subject, message, email_list):
    
    send_mail(
        subject,
        message,
        'from@example.com',
        email_list,
        fail_silently=False,
    )