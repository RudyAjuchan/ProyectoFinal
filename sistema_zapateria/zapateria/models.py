from django.forms import ModelForm, Textarea
from django.db import models

class Clientes(models.Model):
    Nombre=models.CharField(max_length=100)
    Apellido=models.CharField(max_length=100)
    Direccion=models.CharField(max_length=100)
    Telefono=models.IntegerField()
    Nit=models.CharField(max_length=100)

class Zapato(models.Model):
    Estilo=models.CharField(max_length=100)
    Color=models.CharField(max_length=100)
    Talla=models.CharField(max_length=100)
    Marca=models.CharField(max_length=100)
    Proveedor=models.CharField(max_length=100)
    Genero=models.CharField(max_length=100)
    Tipo=models.CharField(max_length=100)
    Precio=models.FloatField()
    Stock=models.IntegerField()
    Fecha_entrada=models.DateField()

class Venta(models.Model):
    id_Zapato=models.ForeignKey(Zapato, on_delete=models.CASCADE)
    Cantidad=models.IntegerField()
    Total=models.FloatField()
    id_Factura=models.IntegerField()

class Factura(models.Model):
    id_Cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    Fecha=models.DateField()
    total=models.FloatField()

