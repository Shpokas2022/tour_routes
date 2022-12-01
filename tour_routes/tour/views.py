from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = ["Apie svetainę", "Pridėti straipsnį", "Komentarai", "Įeiti"]

# menu = [{'title': "Apie svetainę", 'url_name': 'about'},
#         {'title': "Pridėti straipsnį", 'url_name': 'add_page'},
#         {'title': "Komentarai", 'url_name': 'comments'},
#         {'title': "Įeiti", 'url_name': 'login'},
# ]

def index(request):
    sights = Sight.objects.all()
    return render(request, 'tour/index.html', {'sights': sights, 'menu':menu, 'title':'Apie svetainę'})

def about(request):
    return render(request, 'tour/about.html', {'menu':menu, 'title':'Kelionių vadovų puslapis'})


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

