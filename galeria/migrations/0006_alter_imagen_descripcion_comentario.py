# Generated by Django 4.2.11 on 2024-03-31 17:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_imagen_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='descripcion',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(blank=True, null=True)),
                ('fecha_carga', models.DateField(default=django.utils.timezone.now)),
                ('galeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='galeria.galeria')),
            ],
        ),
    ]
