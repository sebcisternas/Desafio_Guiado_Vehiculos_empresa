from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=10)
    marca = models.CharField(max_length=20,null=False,blank=False)
    activo = models.BooleanField(default=False)
    modelo = models.CharField(max_length=20,null=False,blank=False)
    year = models.IntegerField(null=False)
    
class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    activo = models.BooleanField(default=True)
    creacion_registro= models.DateTimeField(auto_now_add=True)
    vehiculo = models.OneToOneField(Vehiculo,related_name='chofer',blank=True,null=True,on_delete=models.PROTECT)

    
class RegistroContabilidad(models.Model):
    fecha_compra = models.DateTimeField(auto_now_add=True)
    valor = models.FloatField()
    vehiculo = models.OneToOneField(Vehiculo, related_name='contabilidad', null=False, blank=False, on_delete=models.PROTECT)
    