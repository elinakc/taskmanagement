from django.contrib import admin
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import taskViewset



router =DefaultRouter()
router.register(r'taskview', taskViewset)


urlpatterns = [
  
  path('', include(router.urls)),


  
]
