from django.contrib.auth.models import User

from django.core.mail import send_mail

from django.shortcuts import render

from .models import Info

from django.conf import settings


# Create your views here.

def send_message(request):
    
    myinfo = Info.objects.first()

    if request.method == 'POST':

        subject= request.POST['subject']
        email = request.user.email
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
        print(subject)
        print(email)
        print(message)

    return render(request,'contact/contact.html',{'myinfo':myinfo})