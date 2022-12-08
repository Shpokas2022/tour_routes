from django.contrib import admin
from . import models


class SightAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'city', 'photo', 'get_google_link')
    list_display_links = ('name',)
    readonly_fields = ('get_google_link',)
    search_fields = ('name', 'city__name', )
    list_filter = ('name', 'city')
    
    fieldsets = (
        ('General', {'fields': ('name', 'street', 'city')}),
        ('Information', {'fields': ('facts', 'photo', 'google_link')}),
    )


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


class RouteAdmin(admin.ModelAdmin):
    list_display=('name',)


class RouteSightAdmin(admin.ModelAdmin):
    list_display = ('sight', 'route', )
    list_filter = ('route',)
    search_fields = ('route__name',)


class SightReviewAdmin(admin.ModelAdmin):
    list_display = ('sight', 'reader', 'created_at')


admin.site.register(models.City, CityAdmin)
admin.site.register(models.Country)
admin.site.register(models.Route, RouteAdmin)
admin.site.register(models.RouteSight, RouteSightAdmin)
admin.site.register(models.TourGuide)
admin.site.register(models.Sight, SightAdmin)
admin.site.register(models.SightReview, SightReviewAdmin)