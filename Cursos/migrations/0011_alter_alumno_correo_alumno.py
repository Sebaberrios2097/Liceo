# Generated by Django 4.0.4 on 2022-05-19 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0010_alter_curso_options_alter_curso_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='correo_alumno',
            field=models.CharField(max_length=50),
        ),
    ]
