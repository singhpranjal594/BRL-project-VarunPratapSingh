from rest_framework import serializers
from .models import information

class informationserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = information
        fields = '__all__'
        