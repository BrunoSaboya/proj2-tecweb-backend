from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/favorits/<str:favoritId>/', views.api_get_fav),
    path('api/favorits/', views.api_post_fav)
]