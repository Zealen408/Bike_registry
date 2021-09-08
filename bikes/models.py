from django.conf import settings
from django.db import models
from django.shortcuts import reverse


def user_directory_path(instance, filename):
    return f'media/uploads/user_{instance.owner.id}/{filename}'


class bike(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    bike_brand = models.CharField(max_length=50, blank=True, null=True)
    bike_model = models.CharField(max_length=50, blank=True, null=True)
    bike_serial_number = models.CharField(max_length=20)
    bike_image1 = models.ImageField(upload_to='media/', blank=True, null=True, help_text='Suggested: image of the Serial Number')
    bike_image2 = models.ImageField(upload_to='media/', blank=True, null=True, help_text='Suggested: image of the bike from the side with owner')
    bike_image3 = models.ImageField(upload_to='media/', blank=True, null=True, help_text='Suggested: image highlighting any after market features')
    bike_stolen = models.BooleanField(default=False)
    
    def __str__(self):
        if self.bike_brand:
            return f'{self.bike_serial_number}, {self.bike_brand}'
        return self.bike_serial_number

    def get_absolute_url(self):
        return reverse('bikes:detail', kwargs={'username': self.owner.email, 'serial_number': self.bike_serial_number})