# Generated by Django 4.0.4 on 2022-05-14 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='tipousuario',
            new_name='profesor',
        ),
        migrations.AddField(
            model_name='alumno',
            name='imagen_alumno',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='profesor',
            name='imagen_profesor',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]