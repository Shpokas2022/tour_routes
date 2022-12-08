# Generated by Django 4.1.3 on 2022-12-07 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tour', '0005_alter_routesight_route_alter_routesight_sight'),
    ]

    operations = [
        migrations.CreateModel(
            name='SightReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('content', models.TextField(max_length=10000, verbose_name='content')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sight_reviews', to=settings.AUTH_USER_MODEL, verbose_name='reader')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='tour.sight', verbose_name='sight')),
            ],
        ),
    ]
