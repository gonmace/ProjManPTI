# Generated by Django 4.2.11 on 2024-03-29 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_avance_sitio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avance',
            name='empalmeE',
            field=models.DateField(blank=True, null=True, verbose_name='Ele.'),
        ),
        migrations.AlterField(
            model_name='avance',
            name='excavacion',
            field=models.DateField(blank=True, null=True, verbose_name='Exc.'),
        ),
        migrations.AlterField(
            model_name='avance',
            name='hormigonado',
            field=models.DateField(blank=True, null=True, verbose_name='Hor.'),
        ),
        migrations.AlterField(
            model_name='avance',
            name='montado',
            field=models.DateField(blank=True, null=True, verbose_name='Mon.'),
        ),
    ]
