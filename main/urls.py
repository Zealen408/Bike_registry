
from .views import *
from django.urls import path

app_name = 'main'

urlpatterns = [
     path('', index, name='home'),
]
