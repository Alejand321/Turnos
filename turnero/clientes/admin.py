from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado', 'creado_en')
    list_filter = ('estado', 'creado_en')
    search_fields = ('nombre', 'email')
