from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden
from .models import Inventario, Solicitud,Envio
from .forms import InventarioForm,PlasticPartsForm,ElectronicPartsForm,EnvioForm
from django.contrib import messages
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
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


from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Solicitud, Inventario

from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Solicitud, Inventario

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

            # Guardar la nueva información en el modelo Solicitud
            solicitud_nueva = Solicitud.objects.create(
                carcasa_color_azul=carcasa_color_azul,
                carcasa_color_verde=carcasa_color_verde,
                carcasa_color_amarillo=carcasa_color_amarillo,
                carcasa_color_morado=carcasa_color_morado,
                carcasa_color_rosa=carcasa_color_rosa,
                carcasa_color_cyan=carcasa_color_cyan
            )

            # Realizar operaciones en el modelo Inventario según tus instrucciones
            multiplicacion_x3 = 3  # Define el valor para multiplicación x3
            multiplicacion_x2 = 2  # Define el valor para multiplicación x2
            total_nativo = (
                carcasa_color_azul + carcasa_color_verde +
                carcasa_color_amarillo + carcasa_color_morado +
                carcasa_color_rosa + carcasa_color_cyan
            )

            inventario_3 = Inventario.objects.get(id=3)
            inventario_4 = Inventario.objects.get(id=4)
            inventario_5 = Inventario.objects.get(id=5)
            inventario_6 = Inventario.objects.get(id=6)
            inventario_8 = Inventario.objects.get(id=8)
            inventario_9 = Inventario.objects.get(id=9)
            inventario_12 = Inventario.objects.get(id=12)
            inventario_13 = Inventario.objects.get(id=13)
            inventario_14 = Inventario.objects.get(id=14)
            inventario_15 = Inventario.objects.get(id=15)
            inventario_16 = Inventario.objects.get(id=16)
            inventario_17 = Inventario.objects.get(id=17)

            inventario_3.stock = F('stock') - total_nativo
            inventario_3.save()

            inventario_4.stock = F('stock') - total_nativo
            inventario_4.save()

            inventario_5.stock = F('stock') - total_nativo
            inventario_5.save()

            inventario_6.stock = F('stock') - total_nativo
            inventario_6.save()

            inventario_8.stock = F('stock') - total_nativo
            inventario_8.save()

            inventario_9.stock = F('stock') - total_nativo
            inventario_9.save()

            inventario_12.stock = F('stock') - total_nativo
            inventario_12.save()

            inventario_13.stock = F('stock') - total_nativo
            inventario_13.save()

            inventario_14.stock = F('stock') - total_nativo
            inventario_14.save()

            inventario_15.stock = F('stock') - total_nativo
            inventario_15.save()

            inventario_16.stock = F('stock') - total_nativo
            inventario_16.save()

            inventario_17.stock = F('stock') - total_nativo
            inventario_17.save()

            inventario_1 = Inventario.objects.get(id=1)
            inventario_2 = Inventario.objects.get(id=2)
            inventario_7 = Inventario.objects.get(id=7)
            inventario_10 = Inventario.objects.get(id=10)
            inventario_11 = Inventario.objects.get(id=11)

            inventario_1.stock = F('stock') - (total_nativo * multiplicacion_x3)
            inventario_1.save()

            inventario_2.stock = F('stock') - (total_nativo * multiplicacion_x2)
            inventario_2.save()

            inventario_7.stock = F('stock') - (total_nativo * multiplicacion_x2)
            inventario_7.save()

            inventario_10.stock = F('stock') - (total_nativo * multiplicacion_x2)
            inventario_10.save()

            inventario_11.stock = F('stock') - (total_nativo * multiplicacion_x2)
            inventario_11.save()

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
            # Obtener los datos del formulario
            cameras = form.cleaned_data['cameras']
            biometric_sensors = form.cleaned_data['biometric_sensors']
            baseband = form.cleaned_data['baseband']
            power_management = form.cleaned_data['power_management']
            processor = form.cleaned_data['processor']
            nand = form.cleaned_data['nand']
            dram = form.cleaned_data['dram']
            accelerometer = form.cleaned_data['accelerometer']
            battery = form.cleaned_data['battery']
            microphone = form.cleaned_data['microphone']
            speakers = form.cleaned_data['speakers']

            # Actualizar registros en Inventario para IDs del 1 al 11
            Inventario.objects.filter(id=1).update(stock=F('stock') + cameras)
            Inventario.objects.filter(id=2).update(stock=F('stock') + biometric_sensors)
            Inventario.objects.filter(id=3).update(stock=F('stock') + baseband)
            Inventario.objects.filter(id=4).update(stock=F('stock') + power_management)
            Inventario.objects.filter(id=5).update(stock=F('stock') + processor)
            Inventario.objects.filter(id=6).update(stock=F('stock') + nand)
            Inventario.objects.filter(id=7).update(stock=F('stock') + dram)
            Inventario.objects.filter(id=8).update(stock=F('stock') + accelerometer)
            Inventario.objects.filter(id=9).update(stock=F('stock') + battery)
            Inventario.objects.filter(id=10).update(stock=F('stock') + microphone)
            Inventario.objects.filter(id=11).update(stock=F('stock') + speakers)

            # Datos para enviar a FastAPI
            data = {
                "cameras": cameras,
                "biometric_sensors": biometric_sensors,
                "baseband": baseband,
                "power_management": power_management,
                "processor": processor,
                "nand": nand,
                "dram": dram,
                "accelerometer": accelerometer,
                "battery": battery,
                "microphone": microphone,
                "speakers": speakers,
            }

            # Enviar datos a FastAPI
            main_api_url = "http://localhost:8001/update-quantities"
            response = requests.post(main_api_url, json=data)

            if response.status_code == 200:
                message = "Solicitud exitosa"
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
            # Obtener los datos del formulario
            carcasa_color_azul = form.cleaned_data['carcasa_color_azul']
            carcasa_color_verde = form.cleaned_data['carcasa_color_verde']
            carcasa_color_amarillo = form.cleaned_data['carcasa_color_amarillo']
            carcasa_color_morado = form.cleaned_data['carcasa_color_morado']
            carcasa_color_rosa = form.cleaned_data['carcasa_color_rosa']
            carcasa_color_cyan = form.cleaned_data['carcasa_color_cyan']

            # Actualizar registros en Inventario para IDs del 12 al 17
            Inventario.objects.filter(id=12).update(stock=F('stock') + carcasa_color_azul)
            Inventario.objects.filter(id=13).update(stock=F('stock') + carcasa_color_verde)
            Inventario.objects.filter(id=14).update(stock=F('stock') + carcasa_color_amarillo)
            Inventario.objects.filter(id=15).update(stock=F('stock') + carcasa_color_morado)
            Inventario.objects.filter(id=16).update(stock=F('stock') + carcasa_color_rosa)
            Inventario.objects.filter(id=17).update(stock=F('stock') + carcasa_color_cyan)

            # Datos para enviar a FastAPI
            data = {
                "carcasa_color_azul": carcasa_color_azul,
                "carcasa_color_verde": carcasa_color_verde,
                "carcasa_color_amarillo": carcasa_color_amarillo,
                "carcasa_color_morado": carcasa_color_morado,
                "carcasa_color_rosa": carcasa_color_rosa,
                "carcasa_color_cyan": carcasa_color_cyan,
                # Agrega más campos según sea necesario
            }

            # Enviar datos a FastAPI
            main_api_url = "http://localhost:8002/update-plastic-parts"
            response = requests.post(main_api_url, json=data)

            if response.status_code == 200:
                message = "Venta exitosa"
            else:
                message = "Error al enviar datos a FastAPI"
        else:
            message = "Formulario inválido"  
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