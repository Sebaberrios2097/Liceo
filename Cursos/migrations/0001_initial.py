# Generated by Django 4.0.4 on 2022-05-24 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id_alumno', models.AutoField(primary_key=True, serialize=False)),
                ('run_alumno', models.IntegerField()),
                ('dv_alumno', models.CharField(max_length=1)),
                ('prim_nom_alumno', models.CharField(max_length=15)),
                ('seg_nom_alumno', models.CharField(max_length=15)),
                ('ap_pat_alumno', models.CharField(max_length=15)),
                ('ap_mat_alumno', models.CharField(max_length=15)),
                ('fec_nac_alumno', models.DateField()),
                ('correo_alumno', models.CharField(max_length=50)),
                ('motivo_matricula', models.CharField(max_length=250)),
                ('nombres_apoderado', models.CharField(max_length=25)),
                ('apellidos_apoderado', models.CharField(max_length=25)),
                ('correo_apoderado', models.CharField(max_length=30)),
                ('ingresado', models.BooleanField(blank=True, null=True)),
                ('imagen_alumno', models.ImageField(blank=True, default='Fotos/static/images/no-img.jpg', upload_to='media')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
                'db_table': 'Alumno',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False)),
                ('nro_curso', models.IntegerField()),
                ('anno_curso', models.IntegerField()),
                ('letra', models.CharField(max_length=1)),
                ('cant_alumnos', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'db_table': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_profesor', models.AutoField(primary_key=True, serialize=False)),
                ('run_profesor', models.IntegerField()),
                ('dv_profesor', models.CharField(max_length=1)),
                ('prim_nom_prof', models.CharField(max_length=15)),
                ('seg_nom_prof', models.CharField(max_length=15, null=True)),
                ('ap_pat_prof', models.CharField(max_length=15)),
                ('ap_mat_prof', models.CharField(max_length=15)),
                ('fec_nac_prof', models.DateField()),
                ('correo_profesor', models.CharField(max_length=50)),
                ('imagen_profesor', models.ImageField(blank=True, default='Fotos/static/images/no-img.jpg', upload_to='media')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
                'db_table': 'Profesor',
            },
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id_suscripcion', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Suscripción',
                'verbose_name_plural': 'Suscripciones',
                'db_table': 'Suscripcion',
            },
        ),
        migrations.CreateModel(
            name='TipoAlmuerzo',
            fields=[
                ('id_tipo_almuerzo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_almuerzo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.AutoField(primary_key=True, serialize=False)),
                ('nomusuario', models.CharField(max_length=20)),
                ('contrausuario', models.CharField(max_length=20)),
                ('profesor', models.BooleanField()),
                ('id_alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cursos.alumno')),
                ('id_profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cursos.profesor')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuario',
            },
        ),
        migrations.CreateModel(
            name='CursoProfesor',
            fields=[
                ('id_cursoprofesor', models.AutoField(primary_key=True, serialize=False)),
                ('prof_jefe', models.BooleanField(null=True)),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.curso')),
                ('id_profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.profesor')),
            ],
            options={
                'verbose_name': 'Curso x Profesor',
                'verbose_name_plural': 'Curso x Profesor',
                'db_table': 'CursoProfesor',
            },
        ),
        migrations.CreateModel(
            name='CursoAlumno',
            fields=[
                ('id_cursoalumno', models.AutoField(primary_key=True, serialize=False)),
                ('id_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.alumno')),
                ('id_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.curso')),
            ],
            options={
                'verbose_name': 'Curso x Alumno',
                'verbose_name_plural': 'Curso x Alumno',
                'db_table': 'CursoAlumno',
            },
        ),
        migrations.CreateModel(
            name='Almuerzo',
            fields=[
                ('id_almuerzo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_almuerzo', models.CharField(max_length=100)),
                ('descripcion_almuerzo', models.CharField(max_length=500)),
                ('id_tipo_almuerzo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.tipoalmuerzo')),
            ],
            options={
                'verbose_name': 'Almuerzo',
                'verbose_name_plural': 'Almuerzos',
                'db_table': 'Almuerzo',
            },
        ),
    ]
