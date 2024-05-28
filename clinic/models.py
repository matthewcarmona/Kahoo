# Permite interactuar con la Base de Datos con el ORM de Django
# Las clases se convierten en tablas en la DB.
# Al modificar el código hay que hacer la migración para actualizar la DB.

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
import uuid


class DocumentType(models.Model):
    code = models.CharField(verbose_name = "Código", max_length = 3, primary_key = True)
    description = models.CharField(verbose_name = "Descripción", max_length = 50, unique = True, null = False)

    class Meta:
        db_table = 'document_type'
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'

    def __str__(self):
        return f'{self.code} - {self.description}'


class Patient(models.Model):
    TYPE = [
        ('POL', 'Póliza de Salud'),
        ('PBS', 'Plan de Beneficios en Salud'),
        ('PAR', 'Particular'),
    ]

    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    document_type = models.ForeignKey(DocumentType, verbose_name = "Tipo de Documento", on_delete = models.PROTECT)
    identity_card = models.CharField(verbose_name = 'Número de Identificación', max_length = 20)
    full_name = models.CharField(verbose_name = 'Nombre Completo', max_length = 250, null = True)
    first_name = models.CharField('Primer Nombre', max_length = 60, null = False, blank = False)
    second_name = models.CharField('Segundo Nombre', max_length = 60, null = True, blank = True)
    surname = models.CharField('Primer Apellido', max_length = 60, null = False, blank = False)
    second_surname = models.CharField('Segundo Apellido', max_length = 60, null = True, blank = True)
    birth_date = models.DateTimeField('Fecha de Nacimiento', null = False, blank = True)
    cellphone = models.CharField('Celular', max_length = 15, null = False, blank = True,
                                 validators = [RegexValidator(regex = '^[0-9]+$', message = 'Ingrese solo números.')])
    email = models.EmailField('Email', max_length = 150, null = False, blank = True)
    type = models.CharField('Tipo Paciente', max_length = 3, choices = TYPE, default = 'PBS')
    date_created = models.DateTimeField('Fecha Creación', auto_now = True, auto_now_add = False)
    created_by = models.ForeignKey(User, verbose_name = 'Creado Por', null = True, on_delete = models.PROTECT,
                                   related_name = 'created_patients')
    date_update = models.DateTimeField('Fecha Actualización', auto_now = False, auto_now_add = True)
    updated_by = models.ForeignKey(User, verbose_name = 'Actualizado Por', null = True, on_delete = models.PROTECT,
                                   related_name = 'updated_patients')

    class Meta:
        db_table = 'patient'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
        constraints = [
            models.UniqueConstraint(fields = ['document_type', 'identity_card'],
                                    name = 'UQ_DOCUMENT_TYPE_IDENTITY_CARD'),
        ]

    def __str__(self):
        return f'{self.document_type} - {self.identity_card} - {self.date_created}- {self.date_update}'.strip


class Medic(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    document_type = models.ForeignKey(DocumentType, verbose_name = "Tipo de Documento", on_delete = models.PROTECT)
    identity_card = models.CharField('Número de Identificación', max_length = 20, null = False, blank = False)
    full_name = models.CharField(verbose_name = 'Nombre Completo', max_length = 250, null = True, blank = False)
    first_name = models.CharField('Primer Nombre', max_length = 60, null = False, blank = False)
    second_name = models.CharField('Segundo Nombre', max_length = 60, null = True, blank = True)
    surname = models.CharField('Primer Apellido', max_length = 60, null = False, blank = False)
    second_surname = models.CharField('Segundo Apellido', max_length = 60, null = True, blank = True)
    cellphone = models.CharField('Celular', max_length = 15, null = True, blank = True,
                                 validators = [RegexValidator(regex = '^[0-9]+$', message = 'Ingrese solo números.')])
    professional_card = models.CharField('Tarjeta Profesional', max_length = 20, null = False)
    date_created = models.DateTimeField('Fecha Creación', auto_now = True, auto_now_add = False)
    created_by = models.ForeignKey(User, verbose_name = 'Creado Por', null = False, on_delete = models.PROTECT,
                                   related_name = 'created_medics')
    date_update = models.DateTimeField('Fecha Actualización', auto_now = True, auto_now_add = False)
    updated_by = models.ForeignKey(User, verbose_name = 'Actualizado Por', null = False, on_delete = models.PROTECT,
                                   related_name = 'updated_medics')
    status = models.BooleanField('Estado', default = True )
    class Meta:
        db_table = 'medic'
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
        constraints = [
            models.UniqueConstraint(fields = ['document_type', 'identity_card'],
                                    name = 'UQ_DOCUMENT_TYPE_IDENTITY_CARD_MEDIC'),
        ]

    def second_surname_display(self):
        return self.second_surname if self.second_surname is not None else ''

    def second_name_display(self):
        return self.second_name if self.second_name is not None else ''

    def __str__(self):
        return f'{self.first_name} {self.second_name_display()} {self.surname} {self.second_surname_display()}'.strip()

class Municipio(models.Model):
    codigo_depto = models.CharField(max_length=100)
    nombre_depto = models.CharField(max_length=100)
    codigo_ciudad = models.CharField(max_length=100)
    nombre_ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)


class Diagnostico(models.Model):
    codigo_3 = models.CharField(max_length=100)
    descripcion_3 = models.CharField(max_length=1000)
    codigo_4 = models.CharField(max_length=100)
    descripcion_4 = models.CharField(max_length=1000)


class Ocupaciones(models.Model):
    codigo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    padre = models.CharField(max_length=100)