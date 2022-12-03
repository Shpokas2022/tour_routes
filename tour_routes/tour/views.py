from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView
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

    
class SightListView(ListView):
    model = Sight
    template_name = 'tour/sight_list.html'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["sight_count"] = self.get_queryset().count()
    return context


class SightDetailView(DetailView):
    model = Sight
    template_name = 'tour/sight_detail'

