from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    #path('', index, name = "index"),
    path('', Index.as_view(), name = "index"),
    path('patient/', login_required(FilterPatients), name = 'patients'),
    path('patient/add', login_required(CreatePatient), name = 'create_patient'),
    path('patient/edit/<str:uuid>', login_required(EditPatient), name = 'edit_patient'),
    path('patient/delete/<str:uuid>', login_required(DeletePatient), name = 'delete_patient'),
    path('medic/', login_required(MedicList.as_view()), name = 'medics'),
    path('medic/add', login_required(CreateMedic.as_view()), name = 'create_medic'),
    path('medic/edit/<str:pk>', login_required(UpdateMedic.as_view()), name = 'update_medic'),
    path('medic/delete/<str:pk>', login_required(DeleteMedic.as_view()), name = 'delete_medic'),
]

