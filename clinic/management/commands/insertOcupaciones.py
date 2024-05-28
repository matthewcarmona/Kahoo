import csv
from django.core.management.base import BaseCommand
from clinic.models import Ocupaciones

class Command(BaseCommand):
    help = 'Inserta los datos de Ocupaciones'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        print("file_path :", file_path)
        with open(file_path, 'r', encoding='latin1') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=';')
            for row in csv_reader:
                print("valor :", row['Código'])
                Ocupaciones.objects.create(
                    codigo=row['Código'],
                    descripcion=row['Descripción'],
                    padre=row['Padre']
                )
        self.stdout.write(self.style.SUCCESS('Data de Municipio insertada'))