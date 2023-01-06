from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm




def index(request):
    appid = 'e9f5629d2a4a8df67639c8958b5b079a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.POST.get('_delete'):
        object.delete()

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()


    form = CityForm

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info={
            'city':city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]['icon']
        }
        all_cities.append(city_info)


    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(request, 'weather/index.html', context)

def maps(request):
    appid = 'e9f5629d2a4a8df67639c8958b5b079a'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    city = 'Gomel'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]['icon'],
        'pressure': res['main']['pressure'],
        'humidity': res['main']['humidity'],
        'speed': res['wind']['speed'],
        'cloudsall': res['clouds']['all']
    }

    textinfo = {
        'info': city_info
    }
    return render(request,'weather/maps.html', textinfo)
