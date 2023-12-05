from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden
from .models import Inventario, Solicitud,Envio
from .forms import InventarioForm,PlasticPartsForm,ElectronicPartsForm,EnvioForm
from django.contrib import messages
import json
import requests
from django.views.decorators.csrf import csrf_exempt
def index(request):
    return render(request, "index.html")


def warehouse(request):
    inventario = Inventario.objects.all()
    if request.method == "POST":
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "warehouse"
            ) 
    else:
        form = InventarioForm()
        return render(request, 'warehouse.html', {"inventario": inventario})


def delete_material(request, material_id):
    material = get_object_or_404(Inventario, pk=material_id)

    if request.method == "POST":
        material.delete()
        return redirect('warehouse')  # Ajusta con el nombre real de tu vista 'warehouse'
    else:
        return redirect('warehouse')


def editar_material(request, material_id):
    material = get_object_or_404(Inventario, pk=material_id)
    print("Nombre del material:", material.nombre)  # Agrega estas líneas
    print("Descripción del material:", material.descripcion)  # Agrega estas líneas
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('warehouse')
    else:
        form = InventarioForm(instance=material)
    return render(request, 'editar_material.html', {'form': form, 'material': material})



@csrf_exempt
def client_request(request):
    solicitudes = Solicitud.objects.all()
    context = {'datos': solicitudes}
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            carcasa_color_azul = data.get('carcasa_color_azul')
            carcasa_color_verde = data.get('carcasa_color_verde')
            carcasa_color_amarillo = data.get('carcasa_color_amarillo')
            carcasa_color_morado = data.get('carcasa_color_morado')
            carcasa_color_rosa = data.get('carcasa_color_rosa')
            carcasa_color_cyan = data.get('carcasa_color_cyan')
            Solicitud.objects.create(
                carcasa_color_azul=carcasa_color_azul,
                carcasa_color_verde=carcasa_color_verde,
                carcasa_color_amarillo=carcasa_color_amarillo,
                carcasa_color_morado=carcasa_color_morado,
                carcasa_color_rosa=carcasa_color_rosa,
                carcasa_color_cyan=carcasa_color_cyan
            )
            return HttpResponse(status=200)
        except json.JSONDecodeError as e:
            return HttpResponse("Error decoding JSON data", status=400)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)
    return render(request, "clientrequest.html", context)

def client_ship(request):
    return render(request, "clientship.html")


def client_sell(request):
    solicitudes = Solicitud.objects.all()
    total_sum = sum(
        solicitud.carcasa_color_azul +
        solicitud.carcasa_color_verde +
        solicitud.carcasa_color_amarillo +
        solicitud.carcasa_color_morado +
        solicitud.carcasa_color_rosa +
        solicitud.carcasa_color_cyan
        for solicitud in solicitudes
    ) * 1000
    formatted_total = f'${total_sum:,}'
    context = {'datos': solicitudes, 'total_sum': formatted_total}
    return render(request, "clientsell.html", context)

def t2pe_sell(request):
    message = None
    if request.method == 'POST':
        form = ElectronicPartsForm(request.POST)
        if form.is_valid():
            data = {
                "cameras": form.cleaned_data['cameras'],
                "biometric_sensors": form.cleaned_data['biometric_sensors'],
                "baseband": form.cleaned_data['baseband'],
                "power_management": form.cleaned_data['power_management'],
                "processor": form.cleaned_data['processor'],
                "nand": form.cleaned_data['nand'],
                "dram": form.cleaned_data['dram'],
                "accelerometer": form.cleaned_data['accelerometer'],
                "battery": form.cleaned_data['battery'],
                "microphone": form.cleaned_data['microphone'],
                "speakers": form.cleaned_data['speakers'],
            }
            main_api_url = "http://localhost:8001/update-quantities"
            response = requests.post(main_api_url, json=data)
            if response.status_code == 200:
                message = "Solicitud  exitosa"
            else:
                message = "Error al enviar datos a FastAPI"
        else:
            message = "Formulario inválido"  
    else:
        form = ElectronicPartsForm()
    return render(request, 't2pcsell.html', {'form': form, 'message': message})

def t2pc_sell(request):
    message = None
    if request.method == 'POST':
        form = PlasticPartsForm(request.POST)
        if form.is_valid():
            data = {
                "carcasa_color_azul": form.cleaned_data['carcasa_color_azul'],
                "carcasa_color_verde": form.cleaned_data['carcasa_color_verde'],
                "carcasa_color_amarillo": form.cleaned_data['carcasa_color_amarillo'],
                "carcasa_color_morado": form.cleaned_data['carcasa_color_morado'],
                "carcasa_color_rosa": form.cleaned_data['carcasa_color_rosa'],
                "carcasa_color_cyan": form.cleaned_data['carcasa_color_cyan'],
                # Agrega más campos según sea necesario
            }
            main_api_url = "http://localhost:8002/update-plastic-parts"
            response = requests.post(main_api_url, json=data)
            if response.status_code == 200:
                message = "Venta exitosa"
            else:
                message = "Error al enviar datos a FastAPI"
        else:
            message = "Formulario inválido"  # Agrega este mensaje en caso de que el formulario no sea válido
    else:
        form = PlasticPartsForm()
    return render(request, 't2pcsell.html', {'form': form, 'message': message})
                


def log_ship(request):
    message = None

    if request.method == 'POST':
        form = EnvioForm(request.POST)
        if form.is_valid():
            nuevo_envio = form.save()  # Guardar el formulario y obtener el objeto Envio
            data = {
                "origen": nuevo_envio.origen,
                "destino": nuevo_envio.destino,
                "fecha": nuevo_envio.fecha.strftime("%Y-%m-%d"),
                "peso": nuevo_envio.peso,
                # Agrega más campos según sea necesario
            }
            main_api_url = "http://localhost:8002/update-envios"
            response = requests.post(main_api_url, json=data, headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                message = "Envío registrado exitosamente"
            else:
                message = "Error al enviar datos a FastAPI"
        else:
            message = "Formulario inválido"
    else:
        form = EnvioForm()

    envios = Envio.objects.all()
    return render(request, 'logship.html', {'form': form, 'envios': envios, 'message': message})