from django.urls import path
from .views import register, message, custom_login_view

urlpatterns = [
    path('application/', message, name='message'),
    path('register/', register, name='register'),
    path('login/', custom_login_view, name='login'),
]