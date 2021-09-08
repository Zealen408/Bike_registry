from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('api-bike/', bikeViewAPI.as_view(), name='bike_list'),
]