from django.urls import path
from weather_api import views
from . import views


urlpatterns = [
    path('api/notes/<str:favoritId>/', views.api_get_fav),
    path('api/notes', views.api_post_fav)
]