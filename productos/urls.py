from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('warehouse/', views.warehouse, name='warehouse'),
    path('clientrequest/', views.client_request, name='client_request'),
    path('clientship/', views.client_ship, name='client_ship'),
    path('clientsell/', views.client_sell, name='client_sell'),
    path('t2pesell/', views.t2pe_sell, name='t2pe_sell'),
    path('t2pcsell/', views.t2pc_sell, name='t2pc_sell'),
    path('logship/', views.log_ship, name='log_ship'),
    path('delete-material/<int:material_id>/', views.delete_material, name='delete-material'),
    path('editar-material/<int:material_id>/', views.editar_material, name='editar-material'),
    path('entryexit/', views.entryexit, name='entryexit'),
    path('contar-solicitudes/', views.alexa_contar_solicitudes, name='alexa-contar-solicitudes'),
    path('consulta-inventario/', views.alexa_consulta_inventario, name='alexa-consulta-inventario'),
    path('obtener-datos-desde-ciudad/<str:ciudad_origen>/', views.obtener_datos_envios_desde_ciudad, name='obtener-datos-envios'),
]
