# Generated by Django 4.2.11 on 2024-04-01 00:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0025_galeria_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes_subidas', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
