from rest_framework import serializers
from bikes.models import bike
from accounts.models import myUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = ['email']


class bikeSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = bike
        fields = '__all__'
        read_only_fields = ['pk', 'owner']