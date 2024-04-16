from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("<h1> Hello world </h1>")
    return render(request, "home.html", {'name' : 'Girish'})

def add(request):
    val1 = request.GET['num1']
    val2 = request.GET['num2']
    res = int(val1) + int(val2)
    return render(request, 'result.html', {'result':res})


