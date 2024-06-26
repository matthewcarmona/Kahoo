# Generated by Django 5.0.2 on 2024-02-18 07:14

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_alter_documenttype_options_alter_medic_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='full_name',
            field=models.CharField(max_length=250, null=True, verbose_name='Nombre Completo'),
        ),
        migrations.AlterField(
            model_name='medic',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Inicio de Sesión'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateTimeField(verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cellphone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Ingrese solo números.', regex='^[0-9]+$')], verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_patients', to=settings.AUTH_USER_MODEL, verbose_name='Creado Por'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_created',
            field=models.DateTimeField(verbose_name='Fecha Creación'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_update',
            field=models.DateTimeField(verbose_name='Fecha Actualización'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=150, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=60, verbose_name='Primer Nombre'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='identity_card',
            field=models.CharField(max_length=20, verbose_name='Número de Identificación'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='second_name',
            field=models.CharField(max_length=60, verbose_name='Segundo Nombre'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='second_surname',
            field=models.CharField(max_length=60, verbose_name='Segundo Apellido'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='surname',
            field=models.CharField(max_length=60, verbose_name='Primer Apellido'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='type',
            field=models.CharField(choices=[('POL', 'Póliza de Salud'), ('PBS', 'Plan de Beneficios en Salud'), ('PAR', 'Particular')], default='PBS', max_length=3, verbose_name='Tipo Paciente'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='updated_patients', to=settings.AUTH_USER_MODEL, verbose_name='Actualizado Por'),
        ),
    ]
