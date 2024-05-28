import logging

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from .forms import *

# Se define lo que se quiere enviar al navegador para ver en pantalla.

'''
1. dispatch(): valida la peticion y elige el metodo HTTP que se utilizo en la solicitud o petición
2. http_method_not_allowe: retorna un error cuando se utiliza un metodo HTTP no soportado o definido
3. options(): para el metodo HTTP Options si se esta usando
'''

'''
TemplateView: Ayuda renderizar un template y hereda de View
'''


# vista de clase general
class Index(TemplateView):
    """ Obtiene la pagina inicial del proyecto"""

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      {'title': 'Welcome !!!'})  # Renderizar la interfaz de inicio de sesión

    # función generica para identificar a que método pertenece el request de la petición
    # Luego de eso llama la petition
    # get put post delete


def CreatePatient(request):
    """Crea un nuevo paciente en el sistema"""

    if request.method == 'POST':
        patient_form = PatientForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('clinic:patients')
    else:
        patient_form = PatientForm()

    return render(request, 'patient/create.html', {
        'form': patient_form
    })


def EditPatient(request, uuid):
    patient_form = None
    error = None
    try:
        patient = Patient.objects.get(uuid = uuid)
        if request.method == 'GET':
            patient_form = PatientForm(instance = patient)
        else:
            patient_form = PatientForm(request.POST, instance = patient)
            if patient_form.is_valid():
                patient_form.save()
                return redirect('clinic:patients')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'patient/create.html', {
        'form': patient_form,
        'error': error
    })


def DeletePatient(request, uuid):
    """
    Elimina un paciente dado el uuid del mismo
    """

    patient = None
    error = None
    try:
        patient = Patient.objects.get(uuid = uuid)
        if request.method == 'POST':
            patient.delete()
            return redirect('clinic:patients')
    except ObjectDoesNotExist as e:
        error = 'El paciente que intenta eliminar no existe.'

    return render(request, 'patient/delete.html', {
        'patient': patient,
        'error': error
    })


def FilterPatients(request):
    """
    Carga el listado de pacientes.
    Si hay un filtro lo aplica y busca por el ID, el email o el número de celular.
    """
    error = None
    patients = None
    params = request.GET
    if not params:
        patients = list(Patient.objects.all())
    else:
        try:
            filter_by = params['filter']
            patients = list(Patient.objects.filter(
                Q(identity_card__icontains = filter_by) |
                Q(full_name = filter_by) |
                Q(email__icontains = filter_by) |
                Q(cellphone__icontains = filter_by)
            ))
        except Exception as e:
            logging.exception("Ocurrió una excepción: %s", e)
            error = "Se ha presentado un error al consultar los pacientes"

    if patients:
        paginator = Paginator(patients, 10)
        page = request.GET.get('page')
        patients = paginator.get_page(page)

    return render(request, 'patient/index.html', {
        'form': SearchPatient(),
        'patients': patients,
        "error": error
    })


# Lista basada en view
class MedicList(ListView):
    template_name = 'medic/index.html'
    context_object_name = 'medics'  # nombre del objeto que le voy a dar para ser enviado al template
    queryset = Medic.objects.filter(status = True)  # Siempre va a ser esta consulta por defecto a no ser que se cambie


class CreateMedic(CreateView):
    model = Medic
    form_class = MedicForm
    template_name = 'medic/create.html'
    success_url = reverse_lazy('clinic:medics')  # Al finalizar la petición redireccionar

    def form_valid(self, form):
        # Asigna el usuario actual al campo de usuario del modelo
        form.instance.full_name = f'{form.instance.first_name}  {form.instance.second_name} {form.instance.surname} {form.instance.second_surname}'.strip()
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class UpdateMedic(UpdateView):
    model = Medic
    template_name = 'medic/view.html'
    form_class = MedicForm

    # success_url = reverse_lazy('clinic:medics')  # Al finalizar la petición redireccionar

    def form_valid(self, form):
        form.instance.full_name = f'{form.instance.first_name} {form.instance.second_name} {form.instance.surname} {form.instance.second_surname}'.strip()
        form.instance.updated_by = self.request.user
        print(form)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance = self.get_object())
        if form.is_valid():
            variables = [getattr(form.instance, attr) if getattr(form.instance, attr) is not None else ''
                         for attr in ['first_name', 'second_name', 'surname', 'second_surname']]

            full_name = ' '.join(variables)
            form.instance.full_name = full_name.strip()
            form.instance.updated_by = self.request.user
            form.save()

        return redirect('clinic:medics')


class DeleteMedic(DeleteView):
    model = Medic
    template_name = 'medic/medic_confirm_delete.html'
    success_url = reverse_lazy('clinic:medics')  # Al finalizar la petición redireccionar

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance = self.get_object())
        form.instance.status = False
        form.instance.updated_by = self.request.user
        form.save()
        return redirect('clinic:medics')
