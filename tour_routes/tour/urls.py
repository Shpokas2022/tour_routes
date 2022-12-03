from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("cities/", views.cities, name='cities'),
    path("city/<int:city_id>/", views.city, name='city'),
    path("sights/", views.SightListView.as_view(), name='sights'),
    path("sight/<int:pk/", views.SightDetailView.as_view, name='sight')
]

