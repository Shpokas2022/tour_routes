# Generated by Django 4.1.3 on 2022-12-05 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0004_alter_route_name_alter_routesight_sight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routesight',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sights', to='tour.route', verbose_name='route'),
        ),
        migrations.AlterField(
            model_name='routesight',
            name='sight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='routes', to='tour.sight', verbose_name='sight'),
        ),
    ]
