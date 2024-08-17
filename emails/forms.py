from django import forms, forms
from django.http import HttpResponse
from .models import EmailMessage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)



class EmailMessageForm(forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = ['name', 'email', 'phone', 'message']
    
    