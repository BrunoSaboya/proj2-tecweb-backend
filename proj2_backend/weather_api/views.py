from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Favorits
from .serializers import FavoritSerializer

@api_view(['GET'])
def api_get_fav(request,favoritId):
    try:
        favorite = Favorits.objects.get(favorits=favoritId)
    except Favorits.DoesNotExist:
        raise Http404()
    
    serialized_note = FavoritSerializer(favorite)
    return Response(serialized_note.data)

@api_view(['POST'])
def api_post_fav(request):

    if request.method == 'POST':
        note = Favorits()
        new_note_data = request.data
        note.favorits = new_note_data['favorits']
        note.save()
    serialized_note = FavoritSerializer(note)
    return Response(serialized_note.data)
