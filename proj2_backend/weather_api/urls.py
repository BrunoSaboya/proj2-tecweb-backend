from django.urls import path, include
from rest_framework import urlpatterns
from weather_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('descriptions', views.DescriptionViewSet)


urlpatterns = [
    path('', include(router.urls))
]