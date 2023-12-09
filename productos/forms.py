from django import forms
from .models import Inventario,Envio,Solicitud,PlasticParts,ElectronicParts, CITY_ORIGIN, CITY_DESTINY

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre', 'descripcion',  'stockl', 'stockr', 'cantidad_maxima', 'cantidad_minima', 'venta_maxima', 'venta_minima', 'BoM', 'status']
class PlasticPartsForm(forms.ModelForm):
    class Meta:
        model = PlasticParts
        fields = '__all__'
        widgets = {
            'carcasa_color_azul': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'carcasa_color_verde': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'carcasa_color_amarillo': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'carcasa_color_morado': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'carcasa_color_rosa': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'carcasa_color_cyan': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
        }

class ElectronicPartsForm(forms.ModelForm):
    class Meta:
        model = ElectronicParts
        fields = '__all__'
        widgets = {
            'cameras': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'biometric_sensors': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'baseband': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'power_management': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'processor': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'nand': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'dram': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'accelerometer': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'battery': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'microphone': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
            'speakers': forms.NumberInput(attrs={'class': 'form-control', 'min': 200, 'max': 1000}),
        }
class EnvioForm(forms.ModelForm):
    solicitud = forms.ModelChoiceField(
        queryset=Solicitud.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    origen = forms.ChoiceField(choices=CITY_ORIGIN, widget=forms.Select(attrs={'class': 'form-control'}))
    destino = forms.ChoiceField(choices=CITY_DESTINY, widget=forms.Select(attrs={'class': 'form-control'}))
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
