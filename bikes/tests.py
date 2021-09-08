from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from.views import *

from django.contrib.auth import get_user_model
# User Model Test

User = get_user_model()

userEmail ='123@123.com'
userPass = 'OneTwo34*'


class test_bike_model(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email=userEmail,
            first_name='Kris',
            last_name='Orman',
            password=userPass,
        )

    def test_create_bike(self):
        self.obj_count = bike.objects.count()
        self.assertEqual(self.obj_count, 0)
        self.bike = bike.objects.create(
            owner=self.user,
            bike_serial_number=11111
        )
        self.obj_count = bike.objects.count()
        self.assertNotEqual(self.obj_count, 0)


class test_bike_views(TestCase):
    def setup(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email=userEmail,
            first_name='Kris',
            last_name='Orman',
            password=userPass,
        )
        self.bike = bike.objects.create(
            owner=self.user,
            bike_serial_number=42
        )

    def test_bike_list_view(self):
        self.client.login(
            email=userEmail,
            password=userPass
        )
        response = self.client.get(reverse('bikes:bike_list', kwargs={'username': userEmail}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bikes/bike_list.html')

    def test_bike_detail_view(self):
        self.client.login(email=userEmail, pasword=userPass)
        response = self.client.get(reverse('bikes:bike_detail', kwargs={'username': userEmail, 'serial_number': '42'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bikes/bike_detail.html')

    def test_bike_create_view(self):
        self.client.login(email=userEmail, pasword=userPass)
        response = self.client.get(reverse('bikes:bike_create'))
        self.assertTemplateUsed(response, 'bikes/bike_create.html')