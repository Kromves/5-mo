from django.urls import path
from .views import register, confirm, login

urlpatterns = [
    path('register/', register, name='register'),
    path('confirm/', confirm, name='confirm'),
    path('login/', login, name='login'),
]