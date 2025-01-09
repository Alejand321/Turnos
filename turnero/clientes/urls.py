from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'), 
    path('registrar/', views.registrar_cliente, name='registrar_cliente'),  
    path('atender/<int:cliente_id>/', views.atender_cliente, name='atender_cliente'),  
    path('eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),  
]
