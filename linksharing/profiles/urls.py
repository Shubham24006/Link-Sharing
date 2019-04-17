from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('userlogin/', user_login, name='user_login'),
    path('register/', Register.as_view(), name='register'),
    path('userlogout/', user_logout, name='user_logout'),
]