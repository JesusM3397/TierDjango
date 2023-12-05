from django import forms
from .models import Inventario,Envio,Solicitud

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
class EnvioForm(forms.ModelForm):
    solicitud = forms.ModelChoiceField(
        queryset=Solicitud.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    origen = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    destino = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    peso = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 1}))

    class Meta:
        model = Envio
        fields = ['solicitud', 'origen', 'destino', 'fecha', 'peso']

    def __init__(self, *args, **kwargs):
        super(EnvioForm, self).__init__(*args, **kwargs)
        
        # Excluir IDs de solicitudes ya existentes
        solicitudes_exist = Envio.objects.values_list('solicitud__id', flat=True).distinct()
        self.fields['solicitud'].queryset = Solicitud.objects.exclude(id__in=solicitudes_exist)
