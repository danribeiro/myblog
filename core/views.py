from django.shortcuts import render
from core.models import *

def home(request):
    queryset = Publish.objects.all()
    return render(request,'home.html',{'data':queryset})

def single(request, slug):
    return render(request, 'generic.html')
