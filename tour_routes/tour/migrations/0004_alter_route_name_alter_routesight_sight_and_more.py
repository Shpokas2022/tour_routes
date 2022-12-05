# Generated by Django 4.1.3 on 2022-12-04 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_rename_route_id_routesight_route_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(help_text='if travel route stop, then write rout with main stop names, if excursion, then write only city name', max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='routesight',
            name='sight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sight', to='tour.sight', verbose_name='sight'),
        ),
        migrations.AlterField(
            model_name='sight',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='photo'),
        ),
    ]