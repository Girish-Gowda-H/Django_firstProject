from django.shortcuts import render
from django.http import HttpResponse
from .models import car

# Create your views here.
def index(request):
    # return HttpResponse("<h1> Hello world </h1>")
    # brands = [
    #     {'id':1 ,'name' :'a' , 'img':'br1.png'},
    #     {'id':2 ,'name' :'b' , 'img':'br2.png'},
    #     {'id':3 ,'name' :'c' , 'img':'br3.png'},
    #     {'id':4 ,'name' :'d' , 'img':'br4.png'},
    # ]
    # car1 = car()
    # car1.id = 1
    # car1.name = 'a'
    # car1.img = 'br1.png'

    # car2 = car()
    # car2.id = 2
    # car2.name = 'b'
    # car2.img = 'br2.png'
    
    # car3 = car()
    # car3.id = 3
    # car3.name = 'c'
    # car3.img = 'br3.png'
    
    # cars = [car1,car2,car3]
    cars = car.objects.all()

    return render(request, "index.html" , {'cars' : cars})



