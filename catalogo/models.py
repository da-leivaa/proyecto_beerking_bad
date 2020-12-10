from django.db import models



class Usuario(models.Model):
    id_usuario=models.CharField(max_length=30)
    nombre_usuario=models.CharField(max_length=30)
    apellido_usuario=models.CharField(max_length=30)
    edad_usuario=models.IntegerField(default=0)
    sexo_usuario=models.CharField(max_length=30)
    correo_usuario=models.EmailField(max_length=30)
    subscripcion_usuario=models.CharField(max_length=30)
    
    def __str__(self):
	    return f'{self.nombre_usuario}, {self.apellido_usuario}'

class Cerveza(models.Model):
    id_cerveza=models.CharField(max_length=20)
    nombre_cerveza=models.CharField(max_length=100)
    cantidad_cerveza=models.IntegerField(default=0)
    precio_cerveza=models.IntegerField(default=0)

    def __str__(self):
	    return self.nombre_cerveza

class Boleta(models.Model):
    nro_boleta=models.CharField(max_length=20)
    fecha_boleta=models.DateField()
    hora_boleta=models.TimeField()
    estado_boleta=models.CharField(max_length=100)

    def __str__(self):
	    return self.nro_boleta

class Compra(models.Model):
    id_compra=models.CharField(max_length=50)
    titular_compra=models.CharField(max_length=100)
    valor_compra=models.IntegerField(default=0)
    valor_cuota=models.IntegerField(default=0)
    cant_cuota=models.IntegerField(default=1)
    fecha_compra=models.DateField()
    hora_compra=models.TimeField()
    valor_despacho=models.IntegerField(default=0)
    tipo_tarjeta=models.CharField(max_length=20)

    def __str__(self):
        return self.id_compra

# Create your models here.
