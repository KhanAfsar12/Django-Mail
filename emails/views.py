from datetime import timedelta
from .models import EmailMessage
from django.http import HttpResponse
from django.core.mail import send_mail
from email_timer import settings
from django.shortcuts import render
from .forms import CustomLoginForm, EmailMessageForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.utils import timezone
from django.contrib import messages

# Create your views here.


# Signup
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# Login
def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('message')  
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})


# Email message
def message(request):
    if request.method == 'POST':
        form = EmailMessageForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            user = request.user

            last_submission = EmailMessage.objects.filter(user=user, email=email).order_by('-submitted_at').first()
            if last_submission:
                time_since_last_submission = timezone.now() - last_submission.submitted_at
                if time_since_last_submission < timedelta(hours=24):
                    messages.warning(request, "You have already submitted an application in the last 24 hours.")
                    return redirect('message')

            email_message = form.save(commit=False)
            email_message.user = user
            email_message.save()
            mail(email)

            return HttpResponse("You are successfully submitted !")
        else:
            messages.warning(request, 'You have missing the field ')
            return redirect('message')
    else:
        form = EmailMessageForm()
    return render(request, 'index.html', {'form': form})



# message on email
def mail(email):
    subject = 'Greetings'
    msg = 'Congratulations, you have successfully send your application \n \n Our candidate will call you in 24 hours'
    to = email
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

    if(res==1):
        msg = "Mail sent successfully"
    else:
        msg = 'Mail could not sent'
    return HttpResponse(msg)