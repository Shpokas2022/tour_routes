from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Country(models.Model):
    name = models.CharField(_('name'), max_length=255)
    main_info = models.TextField(_('main_info'))

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(_('name'), max_length=255)
    history = models.CharField(_('history'), max_length=255)
    country_id = models.ForeignKey(Country, 
    verbose_name=_('country'),
    on_delete=models.SET_NULL, null=True, blank=True,
    related_name='route'
    )

    def __str__(self) -> str:
        return self.name


class Sight(models.Model):
    name = models.CharField(_('name'), max_length=50)
    facts = models.TextField(_('facts'))
    photo = models.ImageField(_('photo'), blank=True, null=True)
    street = models.CharField(_('street'), max_length=255)
    google_link = models.URLField(_('coordinates'), max_length=200, null=True)
    city_id = models.ForeignKey(
        City,
        verbose_name=_('city'),
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='city',
    )

    def __str__(self) -> str:
        return self.name



class Route(models.Model):
    name = models.CharField(_('name'), max_length=255)

    def __str__(self) -> str:
        return self.name


class RouteSight(models.Model):
    route_id = models.ForeignKey(
        Route,
        verbose_name=_('route'),
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='route',
    )
    sight_id = models.ForeignKey(
        Sight,
        verbose_name=_('sight'),
        on_delete=models.SET_NULL, null=True, blank=True,
    )


class TourGuide(models.Model):
    phone = models.CharField(_('phone'), max_length=20)
    user_id = models.ForeignKey(
        User,
        verbose_name=_('user_id'),
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='user_id'
    )


