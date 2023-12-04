from django import forms
from .models import Inventario

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre', 'descripcion', 'stock', 'cantidad_maxima', 'cantidad_minima', 'venta_maxima', 'venta_minima']
class PlasticPartsForm(forms.Form):
    carcasa_color_azul = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    carcasa_color_verde = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    carcasa_color_amarillo = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    carcasa_color_morado = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    carcasa_color_rosa = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    carcasa_color_cyan = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))

class ElectronicPartsForm(forms.Form):
    cameras = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    biometric_sensors = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    baseband = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    power_management = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    processor = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    nand = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    dram = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    accelerometer = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    battery = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    microphone = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))
    speakers = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}))