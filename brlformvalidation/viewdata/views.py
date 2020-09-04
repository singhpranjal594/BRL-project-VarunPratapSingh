from django.shortcuts import render
from signup.models import information
from rest_framework import viewsets
from .serializers import informationserializer

class informationviewset(viewsets.ModelViewSet):
    queryset=information.objects.all()
    serializer_class=informationserializer

