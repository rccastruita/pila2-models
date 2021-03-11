from django.db import models

# Create your models here.

class Personaje(models.Model):
    nombre = models.CharField(max_length=30, default='Nombre')
    rol = models.CharField(max_length=20, default='Rol')
    descripcion = models.TextField(default='Descripción')
    image = models.ImageField(upload_to='models/personaje/images', null=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.rol} - {self.descripcion[:30]}..."