# Generated by Django 5.1 on 2024-08-29 08:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
        ('itineraries', '0002_itinerary_collaborators'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ItineraryDay',
            fields=[
                ('day_id', models.AutoField(primary_key=True, serialize=False)),
                ('day_number', models.IntegerField()),
                ('day_description', models.TextField(blank=True, null=True)),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='itineraries.itinerary')),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryLocation',
            fields=[
                ('itin_loc_id', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.IntegerField()),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.attraction')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_locations', to='itineraries.itineraryday')),
            ],
        ),
    ]