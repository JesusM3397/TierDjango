from django.core.management.base import BaseCommand
from productos.models import Inventario  # Reemplaza 'your_app' con el nombre real de tu aplicación Django

class Command(BaseCommand):
    help = 'Populate Inventario model with initial data'

    def handle(self, *args, **options):
        datos = [
            ('Cameras', 'Cameras for iPhone', 100, 150, 50, 120, 10, 7, 8, 9, 1),
            ('Biometric Sensor', 'Biometric Sensor for iPhone 3rd Gen', 200, 250, 100, 200, 20, 7, 8, 9, 1),
            ('Baseband', 'Baseband for iPhone 1aa', 150, 200, 80, 180, 15, 5, 6, 7, 2),
            ('Power Management', 'Power Management for iPhone', 100, 120, 30, 100, 5, 2, 3, 4, 1),
            ('Processor', 'Processor Apple A14 Bionic', 150, 180, 60, 150, 10, 4, 5, 6, 2),
            ('NAND', 'NAND 128 gb 3rd gen', 200, 250, 100, 220, 20, 8, 9, 10, 1),
            ('DRAM', 'DRAM 1 gb', 150, 200, 80, 180, 15, 3, 4, 5, 2),
            ('Accelerometer', 'Gyroscope 6-axis for iPhone', 100, 150, 50, 120, 10, 1, 2, 3, 1),
            ('Battery', 'Battery 1000 mAh', 150, 200, 80, 180, 15, 6, 7, 8, 2),
            ('Microphone', 'Microphone for iPhone', 150, 180, 60, 150, 10, 9, 10, 1, 1),
            ('Speakers', 'Speakers mono iPhone', 150, 180, 60, 150, 10, 10, 1, 2, 2),
            ('Carcasa Azul', 'Carcasa color Azul', 150, 180, 60, 150, 10, 5, 6, 7, 1),
            ('Carcasa Verde', 'Carcasa color Verde', 150, 180, 60, 150, 10, 6, 7, 8, 2),
            ('Carcasa Amarillo', 'Carcasa color Amarillo', 150, 180, 60, 150, 10, 7, 8, 9, 1),
            ('Carcasa Morado', 'Carcasa color Morado', 150, 180, 60, 150, 10, 8, 9, 10, 2),
            ('Carcasa Rosa', 'Carcasa color Rosa', 150, 180, 60, 150, 10, 9, 10, 1, 1),
            ('Carcasa Cyan', 'Carcasa color Cyan', 150, 180, 60, 150, 10, 10, 1, 2, 2),
            ('iPhone  Azul', 'iPhone 15 Azul', 150, 180, 60, 150, 10, 5, 6, 7, 1),
            ('iPhone  Verde', 'iPhone 15 Verde', 150, 180, 60, 150, 10, 6, 7, 8, 2),
            ('iPhone  Amarillo', 'iPhone 15 Amarillo', 150, 180, 60, 150, 10, 7, 8, 9, 1),
            ('iPhone  Morado', 'iPhone 15 Morado', 150, 180, 60, 150, 10, 8, 9, 10, 2),
            ('iPhone  Rosa', 'iPhone 15 Rosa', 150, 180, 60, 150, 10, 9, 10, 1, 1),
            ('iPhone  Cyan', 'iPhone 15 Cyan', 150, 180, 60, 150, 10, 10, 1, 2, 2),
        ]

        for dato in datos:
            Inventario.objects.create(
                nombre=dato[0],
                descripcion=dato[1],
                stock=dato[2],
                stockl=dato[3],
                stockr=dato[4],
                cantidad_maxima=dato[5],
                cantidad_minima=dato[6],
                venta_maxima=dato[7],
                venta_minima=dato[8],
                BoM=dato[9],
                status=dato[10],
            )

        self.stdout.write(self.style.SUCCESS('Data added successfully'))
