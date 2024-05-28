# Generated by Django 4.2.10 on 2024-02-18 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_alter_patient_created_by_alter_patient_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateTimeField(blank=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cellphone',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Ingrese solo números.', regex='^[0-9]+$')], verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha Actualización'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=150, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='second_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Segundo Nombre'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='second_surname',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Segundo Apellido'),
        ),
    ]