from rest_framework import serializers
from .models import Favorits


class FavoritSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorits
        fields = ['favorits']