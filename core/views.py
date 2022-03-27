from django.shortcuts import render
from core.models import *

def home(request):
    queryset = Publish.objects.all()
    print(len(queryset))
    return render(request,'home.html',{'data':queryset})
