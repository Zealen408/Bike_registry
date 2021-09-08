from django import forms
from .models import bike


class BikeForm(forms.ModelForm):
    class Meta:
        model = bike
        fields = [
            'owner',
            'bike_brand',
            'bike_model',
            'bike_serial_number',
            'bike_stolen',
            'bike_image1',
            'bike_image2',
            'bike_image3',
        ]
        # widgets = {'owner': forms.TextInput(attrs={'disabled': True, 'hidden': True})}
        widgets = {'owner': forms.HiddenInput()}
        # widgets = {'owner': forms.TextInput()}


