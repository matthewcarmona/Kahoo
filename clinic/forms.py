# Creacion de formularios

from django import forms

from .models import Medic, Patient


class MedicForm(forms.ModelForm):
    class Meta:
        model = Medic
        fields = [
            'document_type', 'identity_card', 'first_name',
            'second_name', 'surname', 'second_surname', 'cellphone',
            'professional_card'
        ]
        labels = {
            'document_type': 'Tipo Documento',
            'identity_card': 'Nro. Identificación',
            'first_name': 'Primer Nombre',
            'second_name': 'Segundo Nombre',
            'surname': 'Primer Apellido',
            'second_surname': 'Segundo Apellido',
            'cellphone': 'Nro. Celular',
            'professional_card': 'Nro. T. Profesional',
        }
        widgets = {
            'document_type': forms.Select(
                attrs = {
                    'class': 'form-select'
                }
            ),
            'identity_card': forms.NumberInput(
                attrs = {
                    'id': 'identity',
                    'class': 'form-control',
                    'placeholder': '1234567',
                }
            ),
            'first_name': forms.TextInput(
                attrs = {
                    'id': 'first.name',
                    'class': 'form-control',
                    'placeholder': 'Joe',
                }
            ),
            'second_name': forms.TextInput(
                attrs = {
                    'id': 'second.name',
                    'class': 'form-control',
                    'placeholder': 'Adam',
                }
            ),
            'surname': forms.TextInput(
                attrs = {
                    'id': 'surname',
                    'class': 'form-control',
                    'placeholder': 'Smith',
                }
            ),
            'second_surname': forms.TextInput(
                attrs = {
                    'id': 'second.surname',
                    'class': 'form-control',
                }
            ),
            'cellphone': forms.NumberInput(
                attrs = {
                    'id': 'cell',
                    'class': 'form-control',
                }
            )
            ,
            'professional_card': forms.NumberInput(
                attrs = {
                    'id': 'cell',
                    'class': 'form-control',
                }
            )
        }


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'document_type', 'identity_card', 'first_name',
            'second_name', 'surname', 'second_surname', 'full_name', 'birth_date', 'cellphone',
            'email', 'type'
        ]
        labels = {
            'document_type': 'Tipo Documento',
            'identity_card': 'Nro. Identificación',
            'first_name': 'Primer Nombre',
            'second_name': 'Segundo Nombre',
            'surname': 'Primer Apellido',
            'second_surname': 'Segundo Apellido',
            'birth_date': 'Fecha Nacimiento',
            'cellphone': 'Nro. Celular',
            'email': 'Email',
            'type': 'Tipo Paciente',
        }
        widgets = {
            'document_type': forms.Select(
                attrs = {
                    'class': 'form-select'
                }
            ),
            'identity_card': forms.TextInput(
                attrs = {
                    'id': 'identity',
                    'class': 'form-control',
                    'placeholder': '1234567',
                    'autocomplete': 'off'
                }
            ),
            'first_name': forms.TextInput(
                attrs = {
                    'id': 'first.name',
                    'class': 'form-control',
                    'placeholder': 'Joe',
                    'autocomplete': 'off'
                }
            ),
            'second_name': forms.TextInput(
                attrs = {
                    'id': 'second.name',
                    'class': 'form-control',
                    'placeholder': 'Adam',
                    'autocomplete': 'off'
                }
            ),
            'surname': forms.TextInput(
                attrs = {
                    'id': 'surname',
                    'class': 'form-control',
                    'placeholder': 'Smith',
                    'autocomplete': 'off'
                }
            ),
            'second_surname': forms.TextInput(
                attrs = {
                    'id': 'second.surname',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'birth_date': forms.DateTimeInput(
                attrs = {
                    'id': 'birth.date',
                    'class': 'form-control',
                    'format': '%Y-%m-%d',
                    'type': 'date'
                }
            ),
            'cellphone': forms.NumberInput(
                attrs = {
                    'id': 'cell',
                    'class': 'form-control',
                    'autocomplete': 'off'
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'id': 'email',
                    'autocomplete': 'off',
                    'class': 'form-control',
                }
            ),
            'type': forms.Select(
                attrs = {
                    'class': 'form-select'
                }
            ),
        }


class SearchPatient(forms.Form):
    filter = forms.CharField(label = "Filtrar por:")
