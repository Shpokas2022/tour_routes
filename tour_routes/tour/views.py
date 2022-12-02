from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView
# from .models import *
from . models import Country, City, Sight, Route, RouteSight, TourGuide


def index(request):
    city_count = City.objects.count()
    route_count = Route.objects.count()
    sight_count = Sight.objects.count()

    context = {
        'city_count': city_count,
        'route_count': route_count,
        'sight_count': sight_count,
    }

    return render(request, 'tour/index.html', context)

def cities(request):
    return render(request, 'tour/cities.html', {'cities':City.objects.all()})

def city(request, city_id):
    return render(request, 'tour/city.html',{'city':get_object_or_404(City, id=city_id)})

def sights(request):
    return render(request, 'tour/sights.html', {'sights':Sight.objects.all()})

def sight(request, sight_id):
    return render(request, 'tour/sight.html', {'sight':get_object_or_404(Sight, id=sight_id)})
    
# def SightListView(ListView):
#     model = Sight
#     template_name = 'tour/sight_list.html'


# PAGAL WOMAN
# menu = ["Apie svetainę", "Pridėti straipsnį", "Komentarai", "Įeiti"]

# # menu = [{'title': "Apie svetainę", 'url_name': 'about'},
# #         {'title': "Pridėti straipsnį", 'url_name': 'add_page'},
# #         {'title': "Komentarai", 'url_name': 'comments'},
# #         {'title': "Įeiti", 'url_name': 'login'},
# # ]

# def index(request):
#     sights = Sight.objects.all()
#     return render(request, 'tour/index.html', {'sights': sights, 'menu':menu, 'title':'Apie svetainę'})


# def add_page(request):
#     return HttpResponse(f"<h1>Pridėti straipsnį</h1>")

# def comments(request):
#     return HttpResponse(f"<h1>Komentarai</h1>")

# def login(request):
#     return HttpResponse(f"<h1>Įeiti</h1>")

# def pageNotFound(request, exeption):
#     return HttpResponseNotFound("<h1>PUSLAPIS NERASTAS</h1>")

# def index(request):
#     return HttpResponse("Pirma pradžia padaryta")

