from django.db import models

class Cliente(models.Model):
    ESTADO_CHOICES = [
        ('EN_ESPERA', 'En Espera'),
        ('ATENDIDO', 'Atendido'),
        ('CANCELADO', 'Cancelado'),
    ]
    
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='EN_ESPERA')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.estado})"
