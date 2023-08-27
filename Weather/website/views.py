import requests
from django.http import HttpResponseBadRequest, JsonResponse
from django.views import View

# Change fahrenheit to celsius

def celsius(fahrenheit):
    return "{:.2f}".format(fahrenheit - 273.15)

# Create your views here.
def get_weather(request):
    
    location = request.GET.get('location')
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=359b6593d177e661de9289afe8696705"
    try:
        response = requests.get(url)
        response_data = response.json()
        
        print(response_data)
        
        weather_data = {"condition":response_data["weather"][0]["main"], "temp":celsius(response_data["main"]["temp"]), "feelslike": celsius(response_data["main"]["feels_like"]), "humidity":response_data["main"]["humidity"], "city":response_data["name"], "country":response_data["sys"]["country"]}

        return JsonResponse(weather_data)
    except Exception as e:
        # return JsonResponse({"error": response["error"]["message"]}, status=500)
        return JsonResponse({"error": response_data["message"]}, status=500)