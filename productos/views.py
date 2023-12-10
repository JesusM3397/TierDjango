from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import Inventario, Solicitud, Envio, PlasticParts, ElectronicParts
from .forms import InventarioForm, PlasticPartsForm, ElectronicPartsForm, EnvioForm
from django.contrib import messages
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
import traceback
from django.http import JsonResponse


def index(request):
    return render(request, "index.html")


def warehouse(request):
    inventario = Inventario.objects.all()
    if request.method == "POST":
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("warehouse")
    else:
        form = InventarioForm()
        return render(request, "warehouse.html", {"inventario": inventario})


def delete_material(request, material_id):
    material = get_object_or_404(Inventario, pk=material_id)

    if request.method == "POST":
        material.delete()
        return redirect(
            "warehouse"
        )  # Ajusta con el nombre real de tu vista 'warehouse'
    else:
        return redirect("warehouse")


def editar_material(request, material_id):
    material = get_object_or_404(Inventario, pk=material_id)
    print("Nombre del material:", material.nombre)  # Agrega estas líneas
    print("Descripción del material:", material.descripcion)  # Agrega estas líneas
    if request.method == "POST":
        form = InventarioForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect("warehouse")
    else:
        form = InventarioForm(instance=material)
    return render(request, "editar_material.html", {"form": form, "material": material})

@csrf_exempt
def client_request(request):
    solicitudes = Solicitud.objects.all()
    context = {"datos": solicitudes}

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            carcasa_color_azul = data.get("carcasa_color_azul")
            carcasa_color_verde = data.get("carcasa_color_verde")
            carcasa_color_amarillo = data.get("carcasa_color_amarillo")
            carcasa_color_morado = data.get("carcasa_color_morado")
            carcasa_color_rosa = data.get("carcasa_color_rosa")
            carcasa_color_cyan = data.get("carcasa_color_cyan")

            # Guardar la nueva información en el modelo Solicitud
            solicitud_nueva = Solicitud.objects.create(
                carcasa_color_azul=carcasa_color_azul,
                carcasa_color_verde=carcasa_color_verde,
                carcasa_color_amarillo=carcasa_color_amarillo,
                carcasa_color_morado=carcasa_color_morado,
                carcasa_color_rosa=carcasa_color_rosa,
                carcasa_color_cyan=carcasa_color_cyan,
            )

            # Realizar operaciones en el modelo Inventario según tus instrucciones
            multiplicacion_x3 = 3  # Define el valor para multiplicación x3
            multiplicacion_x2 = 2  # Define el valor para multiplicación x2
            total_nativo = (
                carcasa_color_azul
                + carcasa_color_verde
                + carcasa_color_amarillo
                + carcasa_color_morado
                + carcasa_color_rosa
                + carcasa_color_cyan
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

            inventario_3.stock = F("stock") - total_nativo
            inventario_3.save()

            inventario_4.stock = F("stock") - total_nativo
            inventario_4.save()

            inventario_5.stock = F("stock") - total_nativo
            inventario_5.save()

            inventario_6.stock = F("stock") - total_nativo
            inventario_6.save()

            inventario_8.stock = F("stock") - total_nativo
            inventario_8.save()

            inventario_9.stock = F("stock") - total_nativo
            inventario_9.save()

            inventario_12.stock = F("stock") - total_nativo
            inventario_12.save()

            inventario_13.stock = F("stock") - total_nativo
            inventario_13.save()

            inventario_14.stock = F("stock") - total_nativo
            inventario_14.save()

            inventario_15.stock = F("stock") - total_nativo
            inventario_15.save()

            inventario_16.stock = F("stock") - total_nativo
            inventario_16.save()

            inventario_17.stock = F("stock") - total_nativo
            inventario_17.save()

            inventario_1 = Inventario.objects.get(id=1)
            inventario_2 = Inventario.objects.get(id=2)
            inventario_7 = Inventario.objects.get(id=7)
            inventario_10 = Inventario.objects.get(id=10)
            inventario_11 = Inventario.objects.get(id=11)

            inventario_1.stock = F("stock") - (total_nativo * multiplicacion_x3)
            inventario_1.save()

            inventario_2.stock = F("stock") - (total_nativo * multiplicacion_x2)
            inventario_2.save()

            inventario_7.stock = F("stock") - (total_nativo * multiplicacion_x2)
            inventario_7.save()

            inventario_10.stock = F("stock") - (total_nativo * multiplicacion_x2)
            inventario_10.save()

            inventario_11.stock = F("stock") - (total_nativo * multiplicacion_x2)
            inventario_11.save()

            # Devuelve una respuesta JSON al cliente con algún mensaje o datos adicionales
            response_data = {"message": "Solictud en Preparacion",}
            return JsonResponse(response_data, status=200)

        except json.JSONDecodeError as e:
            return HttpResponse("Error decoding JSON data", status=400)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

    return render(request, "clientrequest.html", context)


def client_ship(request):
    return render(request, "clientship.html")


def get_exchange_rates(base_currency):
    print(f"Obteniendo tasas de cambio para {base_currency}")
    api_key = "b6e563dc2f7b076896414eff4f6cb603"
    url = f"https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        rates = {
            "USD": data["rates"]["USD"],
            "EUR": data["rates"]["EUR"],
            "MXN": data["rates"]["MXN"],
            # Agrega más monedas según sea necesario
        }
        return rates
    except Exception as e:
        print(f"Error al obtener las tasas de cambio: {e}")
        return {
            "USD": 1.0,
            "EUR": 1.0,
            "MXN": 1.0,
        }  # En caso de error, usar tasas de cambio predeterminadas de 1.0


def client_sell(request, currency="USD"):
    solicitudes = Solicitud.objects.all()
    exchange_rates = get_exchange_rates(currency)  # Utiliza la moneda seleccionada

    # Obtener la tasa de cambio específica para la moneda seleccionada
    conversion_rate = exchange_rates.get(currency, 1.0)

    # Calcular el total y multiplicarlo por 1000
    total_sum = (
        sum(
            solicitud.carcasa_color_azul
            + solicitud.carcasa_color_verde
            + solicitud.carcasa_color_amarillo
            + solicitud.carcasa_color_morado
            + solicitud.carcasa_color_rosa
            + solicitud.carcasa_color_cyan
            for solicitud in solicitudes
        )
        * 1000
    )

    # Multiplicar el total por las tasas de cambio
    total_in_selected_currency = (
        total_sum * conversion_rate
    )  # Total en la moneda seleccionada

    # Calcular el total en otras monedas
    total_in_usd = total_sum * exchange_rates["USD"]
    total_in_eur = total_sum * exchange_rates["EUR"]
    total_in_mxn = total_sum * exchange_rates["MXN"]
    # Agrega más monedas según sea necesario

    context = {
        "datos": solicitudes,
        "total_sum": total_sum,
        "total_in_selected_currency": total_in_selected_currency,
        "total_in_usd": total_in_usd,
        "total_in_eur": total_in_eur,
        "total_in_mxn": total_in_mxn,
        "selected_currency": currency,
        "exchange_rates": exchange_rates,
    }
    return render(request, "clientsell.html", context)


def t2pe_sell(request):
    message = None

    if request.method == "POST":
        form = ElectronicPartsForm(request.POST)

        if form.is_valid():
            electronic_parts = form.save()

            # Datos para enviar a FastAPI
            data = {
                "cameras": electronic_parts.cameras,
                "biometric_sensors": electronic_parts.biometric_sensors,
                "baseband": electronic_parts.baseband,
                "power_management": electronic_parts.power_management,
                "processor": electronic_parts.processor,
                "nand": electronic_parts.nand,
                "dram": electronic_parts.dram,
                "accelerometer": electronic_parts.accelerometer,
                "battery": electronic_parts.battery,
                "microphone": electronic_parts.microphone,
                "speakers": electronic_parts.speakers,
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

    return render(request, "t2pesell.html", {"form": form, "message": message})


def t2pc_sell(request):
    message = None

    if request.method == "POST":
        form = PlasticPartsForm(request.POST)

        if form.is_valid():
            plastic_parts_data = form.save()
            data = {
                "carcasa_color_azul": plastic_parts_data.carcasa_color_azul,
                "carcasa_color_verde": plastic_parts_data.carcasa_color_verde,
                "carcasa_color_amarillo": plastic_parts_data.carcasa_color_amarillo,
                "carcasa_color_morado": plastic_parts_data.carcasa_color_morado,
                "carcasa_color_rosa": plastic_parts_data.carcasa_color_rosa,
                "carcasa_color_cyan": plastic_parts_data.carcasa_color_cyan,
            }

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

    return render(request, "t2pcsell.html", {"form": form, "message": message})


def log_ship(request):
    message = None

    if request.method == "POST":
        form = EnvioForm(request.POST)
        if form.is_valid():
            nuevo_envio = form.save()
            data = {
                "origen": nuevo_envio.origen,
                "destino": nuevo_envio.destino,
                "fecha": nuevo_envio.fecha.strftime("%Y-%m-%d"),
                "peso": nuevo_envio.peso,
            }
            main_api_url = "http://localhost:8002/update-envios"
            response = requests.post(
                main_api_url, json=data, headers={"Content-Type": "application/json"}
            )
            if response.status_code == 200:
                message = "Envío registrado exitosamente"
            else:
                message = "Error al enviar datos a FastAPI"
        else:
            message = "Formulario inválido"
    else:
        form = EnvioForm()

    envios = Envio.objects.all()
    return render(
        request, "logship.html", {"form": form, "envios": envios, "message": message}
    )


def entryexit(request):
    solicitudes = Solicitud.objects.all()
    total_solicitudes = sum(
        [
            solicitud.carcasa_color_azul
            + solicitud.carcasa_color_verde
            + solicitud.carcasa_color_amarillo
            + solicitud.carcasa_color_morado
            + solicitud.carcasa_color_rosa
            + solicitud.carcasa_color_cyan
            for solicitud in solicitudes
        ]
    )
    plastic_parts_data = PlasticParts.objects.last()
    electronic_parts_data = ElectronicParts.objects.last()
    total_plastic_parts = (
        (
            plastic_parts_data.carcasa_color_azul
            + plastic_parts_data.carcasa_color_verde
            + plastic_parts_data.carcasa_color_amarillo
            + plastic_parts_data.carcasa_color_morado
            + plastic_parts_data.carcasa_color_rosa
            + plastic_parts_data.carcasa_color_cyan
        )
        if plastic_parts_data
        else 0
    )

    total_electronic_parts = (
        (
            electronic_parts_data.cameras
            + electronic_parts_data.biometric_sensors
            + electronic_parts_data.baseband
            + electronic_parts_data.power_management
            + electronic_parts_data.processor
            + electronic_parts_data.nand
            + electronic_parts_data.dram
            + electronic_parts_data.accelerometer
            + electronic_parts_data.battery
            + electronic_parts_data.microphone
            + electronic_parts_data.speakers
        )
        if electronic_parts_data
        else 0
    )

    return render(
        request,
        "entry.html",
        {
            "solicitudes": solicitudes,
            "total_solicitudes": total_solicitudes,
            "plastic_parts": PlasticParts.objects.all(),  # Obtén todos los registros de PlasticParts
            "electronic_parts": ElectronicParts.objects.all(),  # Obtén todos los registros de ElectronicParts
            "total_plastic_parts": total_plastic_parts,
            "total_electronic_parts": total_electronic_parts,
        },
    )
@csrf_exempt
def alexa_contar_solicitudes(request):
    if request.method == 'POST':
        try:
            # Puedes personalizar esto según la estructura específica de tu Intent
            data = json.loads(request.body)

            # Contar solicitudes y verificar el umbral
            cantidad_solicitudes = Solicitud.objects.count()
            umbral = 100

            if cantidad_solicitudes > umbral:
                response_text = f'¡Alerta! Hay más de {umbral} solicitudes pendientes.'
            else:
                response_text = f'Hay {cantidad_solicitudes} solicitudes en total.'

            # Construir la respuesta en el formato de respuesta de Alexa
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': response_text
                    },
                    'shouldEndSession': True
                }
            }

            return JsonResponse(response)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error decoding JSON data'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
@csrf_exempt
def alexa_consulta_inventario(request):
    if request.method == 'POST':
        try:
            # Puedes personalizar esto según la estructura específica de tu Intent
            data = json.loads(request.body)
            producto = data.get('slots', {}).get('Producto', {}).get('value')

            # Consulta el inventario para obtener la información del producto
            inventario_producto = Inventario.objects.get(nombre=producto)

            # Construir la respuesta en el formato de respuesta de Alexa
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': f'Hay {inventario_producto.stock} unidades de {producto} en stock.'
                    },
                    'shouldEndSession': True
                }
            }

            return JsonResponse(response)

        except Inventario.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado en el inventario'}, status=404)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error decoding JSON data'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
@csrf_exempt
def obtener_datos_envios_desde_ciudad(request, ciudad_origen):
    if request.method == 'GET':
        try:
            # Obtener información sobre los envíos desde la ciudad de origen
            envios_desde_ciudad = Envio.objects.filter(origen=ciudad_origen)
            cantidad_envios = envios_desde_ciudad.count()

            # Construir la respuesta en el formato de respuesta de Alexa
            response = {
                'version': '1.0',
                'response': {
                    'outputSpeech': {
                        'type': 'PlainText',
                        'text': f'Hay un total de {cantidad_envios} envíos realizados desde {ciudad_origen}.'
                    },
                    'shouldEndSession': True
                }
            }

            return JsonResponse(response)

        except Exception as e:
            return JsonResponse({'error': f'Error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)