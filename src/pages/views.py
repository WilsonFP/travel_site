from django.shortcuts import render
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
from .LocationProxy import LocationProxy
from .FoodProxy import FoodProxy
from .WeatherProxy import WeatherProxy

# Create your views here.
def home_view(request, *args, **kwargs): #Python specific
    context = {
        'failed_search': False
    }
    return render(request, "home.html", context)

def query_result_view(request, *args, **kwargs): #Python specific
    my_new_search = request.POST.get('destination')
    location = LocationProxy(my_new_search)
    data = location.run()
    request.session['location_data'] = data

    #print("!!!!!!!!!!!")
    #print(data["_embedded"]["city:search-results"][1]["matching_full_name"])
    if len(data["_embedded"]["city:search-results"]) < 1:
        return render(request, "home.html", {'failed_search': True})

    #Need to account for no result
    result_list = []
    for x in data["_embedded"]["city:search-results"]:
            result_list.append(x["matching_full_name"])
            #print(context[temp])
    context = {
        "result_list": result_list
    }
    return render(request, "query_result.html", context)

def destination_info_view(request):
    data = request.session.get('location_data', None)
    #request.session['shared_location'].set_data(request.POST.get('city'))
    location = LocationProxy(" ")
    location.set_data(data, request.POST.get('city'))
    food = FoodProxy()
    food_data = food.run()
    weather = WeatherProxy()
    weather_data = weather.run()


    #Organize Food Data
    popularity_rating = "-"
    night_life_rating = "-"
    cuisine_list = []
    best_restaurant_list = []

    if type(food_data) is str:
        pass
    else:
        popularity_rating = food_data["popularity"]
        night_life_rating = food_data["nightlife_index"]
        for x in food_data["top_cuisines"]:
            cuisine_list.append(x)
        for x in food_data["best_rated_restaurant"]:
            best_restaurant_list.append(x["restaurant"]["name"] + "\n\t" + x["restaurant"]["location"]["address"])

    #Organize Weather Data
    current_weather = ""
    week_weather = ""
    t = u"\u00b0"

    current_weather += weather_data["currently"]["summary"] + " & " + str(weather_data["currently"]["temperature"]) + t + "F"

    week_weather += weather_data["daily"]["summary"]

    city_name = request.POST.get('city')
    city_name = city_name[city_name.index(' '):]


    context = {
        "city_name" : city_name,
        "popularity_rating" : popularity_rating,
        "night_life_rating" : night_life_rating,
        "cuisine_list" : cuisine_list,
        "best_restaurant_list" : best_restaurant_list,
        "current_weather" : current_weather,
        "week_weather" : week_weather


    }



    return render(request, "destination_info.html", context)
