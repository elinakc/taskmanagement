from django.shortcuts import render
from rest_framework import viewsets
from task.models import task
from task.serializers import taskSerializers

# Create your views here.

class taskViewset(viewsets.ModelViewSet):
  queryset = task.objects.all()
  serializer_class = taskSerializers
  # permissons_class =['IsAuthenticated']
  
  