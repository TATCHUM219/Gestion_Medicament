# Generated by Django 5.0.7 on 2024-08-29 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_commande_date_heure_alter_medicament_arte_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicament',
            name='description',
        ),
        migrations.RemoveField(
            model_name='medicament',
            name='exemple_lien_bout',
        ),
        migrations.RemoveField(
            model_name='medicament',
            name='info',
        ),
        migrations.RemoveField(
            model_name='medicament',
            name='zone_traitement',
        ),
        migrations.AddField(
            model_name='medicament',
            name='qte',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='commande',
            name='date_heure',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 29, 14, 37, 43, 9233, tzinfo=datetime.timezone.utc)),
        ),
    ]
