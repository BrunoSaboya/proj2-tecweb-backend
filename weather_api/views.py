import urllib.request
import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Favorits
from .serializers import FavoritSerializer


def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&lang=pt_br&units=metric&appid=7d285bda711c15f2ae5129ca5137943b').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)

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