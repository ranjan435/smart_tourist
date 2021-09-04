from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Place 
from .forms import SearchForm
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'map/home.html',{
        'places': Place.objects.all()[:20]
    })

def recommend(request):
    return render(request, 'map/recommend.html',{
        'places': Place.objects.all()
    })

def detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    context = {
        'place': place
    }
    return render(request, 'map/detail.html', context)

def search_recommend(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = request.POST['search']
            place = Place.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)).distinct()
            return render(request, 'map/recommend.html',{
                'places': place
            })
    else:
        form = SearchForm()
    return render(request, 'map/search.html', {'form': form})
        