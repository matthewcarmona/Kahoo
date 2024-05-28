import csv
from django.core.management.base import BaseCommand
from clinic.models import Diagnostico

class Command(BaseCommand):
    help = 'Inserta los datos de Diagnostico'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        print("file_path :", file_path)
        with open(file_path, 'r', encoding='latin1') as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=';')
            for row in csv_reader:
                print("valor :", row['COD_3'])
                Diagnostico.objects.create(
                    codigo_3=row['COD_3'],
                    descripcion_3=row['DESCRIPCION_3'],
                    codigo_4=row['COD_4'],
                    descripcion_4=row['DESCRIPCION_4']
                )
        self.stdout.write(self.style.SUCCESS('Data de Diagnostico insertada'))