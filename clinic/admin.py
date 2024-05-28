from django.utils import timezone
from django.contrib import admin
from .models import Medic, DocumentType


# Añadir las aplicaciones al panel de administración


class MedicAdmin(admin.ModelAdmin):
    list_display = (
        'document_type', 'identity_card', 'professional_card', 'first_name', 'second_name', 'surname',
        'second_surname', 'cellphone',
        'created_by', 'date_created', 'updated_by', 'date_update')
    list_filter = ('identity_card', 'professional_card', 'first_name', 'second_name', 'surname', 'second_surname')
    search_fields = ['identity_card', 'professional_card', 'first_name']
    readonly_fields = ('date_created', 'created_by', 'date_update', 'updated_by')
    fields = (
        'document_type', 'identity_card', 'first_name', 'second_name', 'surname', 'second_surname', 'professional_card',
        'cellphone')
    ordering = ['document_type', 'identity_card', 'professional_card', 'first_name', 'second_name', 'surname',
                'second_surname']

    # Sobrescribe el método save_model para agregar la fecha de creación y el usuario logueado
    def save_model(self, request, obj, form, change):
        if not change:
            obj.date_created = timezone.now()
            obj.created_by = request.user
        obj.date_update = timezone.now()
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'description')
    ordering = ['code']


admin.site.register(Medic, MedicAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
