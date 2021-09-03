from django.shortcuts import render
from .models import Place 

# Create your views here.
def index(request):
    return render(request, 'map/hy.html',{
        'places': Place.objects.all()
    })