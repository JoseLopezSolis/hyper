from django.db import models

# Create your models here.
class CrudUser(models.Model):
  nombre = models.CharField(max_length=50, null=True)
  apellido = models.TextField(max_length=100, null=True)
  edad = models.IntegerField(null=True)
  fecha_de_creacion = models.DateField(auto_now=True)

  #
  def __str__(self):
    return self.nombre
  
