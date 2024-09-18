# Generated by Django 5.0.7 on 2024-08-31 18:39

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_commande_est_livre_alter_commande_date_heure'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicament',
            name='marque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='client.fabricant'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='date_heure',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 31, 18, 39, 49, 272473, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='medicament',
            name='fabricant',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
