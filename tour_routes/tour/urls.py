from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("cities/", views.cities, name='cities'),
    path("city/<int:city_id>/", views.city, name='city'),
    path("sights/", views.sights, name='sights'),
    path("sight/<int:sight_id>/", views.sight, name='sight'),
    # path("sights/", views.SightListView.as_view(), name='sights'),
]

