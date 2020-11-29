from django.shortcuts import render, HttpResponse
from time import strftime, gmtime

def index(request):
    context = {
        "datetime_object": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

# Create your views here.
