from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

# Standartinis Django user-io modelis
User = get_user_model()


# Pagrindinė informacija apie lankomą šalį
class Country(models.Model):
    name = models.CharField(_('name'), max_length=255)
    main_info = models.TextField(_('main_info'), blank=True, null=True)

    def __str__(self) -> str:
        return self.name


# Pagrindinė informacija apie lankomą/pravažiuojamą miestą
class City(models.Model):
    name = models.CharField(_('name'), max_length=255)
    history = models.CharField(_('history'), max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, 
        verbose_name=_('country'),
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='cities'
    )

    def __str__(self) -> str:
        return self.name


# Kaupsime informaciją apie konkrečius lankomus objektus mieste
class Sight(models.Model):
    name = models.CharField(_('name'), max_length=50)
    facts = models.TextField(_('facts'))
    photo = models.ImageField(_('photo'), upload_to='media', blank=True, null=True)
    street = models.CharField(_('street'), max_length=255)
    google_link = models.URLField(_('coordinates'), max_length=200, null=True)
    city = models.ForeignKey(
        City,
        verbose_name=_('city'),
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='sights',
    )

    def __str__(self) -> str:
        return self.name
    
    def get_google_link(self):
        return format_html('<a href="{link}">{link}</a>', link=self.google_link)


# Kelionės pradžios, pabaigos ir tarpiniai taškai
class Route(models.Model):
    name = models.CharField(_('name'),
        help_text=_('if travel route stop, then write rout with main stop names, if excursion, then write only city name'),
        max_length=255)

    def __str__(self) -> str:
        return self.name


class RouteSight(models.Model):
    route = models.ForeignKey(
        Route,
        verbose_name=_('route'),
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='sights',
    )
    sight = models.ForeignKey(
        Sight,
        verbose_name=_('sight'),
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='routes'
    )

    def __str__(self) -> str:
        return f"Stop on route {self.route}"
        # return f"Stop {self.sight} on route {self.route}"

# Prisijungiantiems asmenims
class TourGuide(models.Model):
    phone = models.CharField(_('phone'), max_length=20)
    user = models.OneToOneField(
        User,
        verbose_name=_('user_id'),
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='tour_guide'
    )

    def __str__(self) -> str:
        return self.user
