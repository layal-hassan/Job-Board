from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class AddJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('title' ,'job_type' ,'description', 'vacancy','salary','experience','category','address')