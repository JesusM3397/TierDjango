from django.db import models

class Inventario(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    stock = models.IntegerField()
    cantidad_maxima = models.IntegerField()
    cantidad_minima = models.IntegerField()
    venta_maxima = models.IntegerField()
    venta_minima = models.IntegerField()

    def __str__(self):
        return self.nombre
class Solicitud(models.Model):
    carcasa_color_azul = models.IntegerField()
    carcasa_color_verde = models.IntegerField()
    carcasa_color_amarillo = models.IntegerField()
    carcasa_color_morado = models.IntegerField()
    carcasa_color_rosa = models.IntegerField()
    carcasa_color_cyan = models.IntegerField()

    def __str__(self):
        return f'Solicitud {self.id}'
class Envio(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE,default=None)
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    fecha = models.DateField()
    peso = models.IntegerField()

    def __str__(self):
        return f"Envío de {self.origen} a {self.destino} con fecha {self.fecha} y peso {self.peso} kg"