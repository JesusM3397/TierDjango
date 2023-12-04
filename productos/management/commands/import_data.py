from django.core.management.base import BaseCommand
from productos.models import Inventario

class Command(BaseCommand):
    help = 'Carga datos iniciales en la base de datos'

    def handle(self, *args, **options):
        datos = [
            ('Cameras', 'Cameras for iPhone', 100, 150, 50, 120, 10),
            ('Biometric Sensor', 'Biometric Sensor for iPhone 3rd Gen', 200, 250, 100, 200, 20),
            ('Baseband', 'Baseband for iPhone 1aa', 150, 200, 80, 180, 15),
            ('Power Management', 'Power Management for iPhone', 100, 120, 30, 100, 5),
            ('Processor', 'Processor Apple A14 Bionic', 150, 180, 60, 150, 10),
            ('NAND', 'NAND 128 gb 3rd gen', 200, 250, 100, 220, 20),
            ('DRAM', 'DRAM 1 gb', 150, 200, 80, 180, 15),
            ('Accelerometer', 'Gyroscope 6-axis for iPhone', 100, 150, 50, 120, 10),
            ('Battery', 'Battery 1000 mAh', 150, 200, 80, 180, 15),
            ('Microphone', 'Microphone for iPhone', 150, 180, 60, 150, 10),
            ('Speakers', 'Speakers mono iPhone', 150, 180, 60, 150, 10),
            ('Carcasa Azul', 'Carcasa color Azul', 150, 180, 60, 150, 10),
            ('Carcasa Verde', 'Carcasa color Verde', 150, 180, 60, 150, 10),
            ('Carcasa Amarillo', 'Carcasa color Amarillo', 150, 180, 60, 150, 10),
            ('Carcasa Morado', 'Carcasa color Morado', 150, 180, 60, 150, 10),
            ('Carcasa Rosa', 'Carcasa color Rosa', 150, 180, 60, 150, 10),
            ('Carcasa Cyan', 'Carcasa color Cyan', 150, 180, 60, 150, 10),
        ]

        for dato in datos:
            Inventario.objects.create(
                nombre=dato[0],
                descripcion=dato[1],
                stock=dato[2],
                cantidad_maxima=dato[3],
                cantidad_minima=dato[4],
                venta_maxima=dato[5],
                venta_minima=dato[6]
            )

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))
