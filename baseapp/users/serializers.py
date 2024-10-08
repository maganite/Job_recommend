from rest_framework import serializers
from .models import UserProfile


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
