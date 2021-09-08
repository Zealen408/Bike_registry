
from .views import *
from django.urls import path

app_name = 'bikes'

urlpatterns = [
    path('create', bike_create, name='create'),
    path('delete/<int:pk>', BikeDelete.as_view(), name='delete'),
    path('<str:username>', bike_list, name='list'),
    path('<str:username>/<str:serial_number>', bike_detail, name='detail'),
    path('lost', lost_bikes, name='lost')
]
