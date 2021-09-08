
from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
     path('register', register_request, name='register'),
     path('login', login_request, name='login'),
     path('logout', logout_request, name='logout'),
     path('user-profile', user_update_request, name='profile'),
]
