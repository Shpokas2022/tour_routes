from django.contrib import admin
from . import models


class SightAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'city', 'get_google_link')
    list_display_links = ('name',)
    readonly_fields = ('get_google_link',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

class RouteAdmin(admin.ModelAdmin):
    list_display=('name',)


admin.site.register(models.City, CityAdmin)
admin.site.register(models.Country)
admin.site.register(models.Route, RouteAdmin)
admin.site.register(models.RouteSight)
admin.site.register(models.TourGuide)
admin.site.register(models.Sight, SightAdmin)