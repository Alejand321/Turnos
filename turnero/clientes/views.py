from django.shortcuts import render, redirect
from .models import Cliente
from django.http import HttpResponse


def lista_clientes(request):
    clientes = Cliente.objects.all()  
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def registrar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            Cliente.objects.create(nombre=nombre)
            return redirect('lista_clientes')
        else:
            return HttpResponse("El nombre es requerido", status=400)
    return redirect('lista_clientes')  


def atender_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.estado = 'ATENDIDO'
    cliente.save()
    return redirect('lista_clientes')


def eliminar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return redirect('lista_clientes')
