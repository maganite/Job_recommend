from rest_framework import serializers
from .models import JobProfile


class JobsSerializers(serializers.ModelSerializer):
    class Meta:
        model = JobProfile
        fields = '__all__'
