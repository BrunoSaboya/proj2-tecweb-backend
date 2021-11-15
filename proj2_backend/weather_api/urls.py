from django.urls import path
from weather_api import views
from . import views


urlpatterns = [
    path('api/favorits/<str:favoritId>/', views.api_get_fav),
    path('api/favorits/', views.api_post_fav)
]