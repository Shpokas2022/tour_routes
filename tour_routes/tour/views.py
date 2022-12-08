from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView
from . models import Country, City, Sight, Route, RouteSight, TourGuide
from django.views.generic.edit import FormMixin
from django.core.paginator import Paginator
from . import models

def index(request):
    city_count = City.objects.count()
    route_count = Route.objects.count()
    sight_count = Sight.objects.count()
    visits_count = request.session.get('visits_count', 1)
    request.session['visits_count'] = visits_count + 1

    context = {
        'city_count': city_count,
        'route_count': route_count,
        'sight_count': sight_count,
        'visits_count': visits_count,
    }
    return render(request, 'tour/index.html', context)

def cities(request):
    cities = City.objects.all()
    search = request.GET.get('search')
    if search:
        cities = cities.filter(cities_facts__incontains=search)
    paginator = Paginator(cities, 10)
    page_number = request.GET.get('page')
    paged_cities = paginator.get_page(page_number)
    # return render(request, 'tour/cities.html', {'cities':City.objects.all()})
    return render(request, 'tour/cities.html', {'cities':paged_cities})

def city(request, city_id):
    # paginator2 = Paginator(City.objects.all(), 5)
    # page_number = request.GET.get('page')
    # paged_city = paginator2.get_page(page_number)
    return render(request, 'tour/city.html',{'city':get_object_or_404(City, id=city_id)})

def routes(request):
    search = request.GET.get('search')
    if search:
        routes = routes.filter(sight_facts__icontains=search)
    paginator = Paginator(Route.objects.all(), 10)
    page_number = request.GET.get('page')
    paged_routes = paginator.get_page(page_number)
    return render(request, 'tour/routes.html', {'routes':paged_routes})

def route(request, route_id):
    return render(request, 'tour/route.html', {'route':get_object_or_404(Route, id=route_id)})

def route_view(request, route_id):
    return render(request, 'tour/route.html', {'route':get_object_or_404(Route, id=route_id)})
    
class SightListView(ListView):
    model = Sight
    template_name = 'tour/sight_list.html'


class SightDetailView(DetailView):
    model = Sight
    template_name = 'tour/sight_detail'

