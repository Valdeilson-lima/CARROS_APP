from django.shortcuts import render
from cars.models import car
#from django.http import HttpResponse

def cars_view(request):
    
    
    print(request.GET)
    cars = car.objects.filter(model__contains='C')
   
    return  render(
        request,
        'cars.html', 
        {'cars':cars } 
    )
