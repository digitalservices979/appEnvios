from django.db import models

# Create your models here.

class Mascarilla(models.Model):
	codigo = models.CharField(max_length=50)
	imagen = models.ImageField(upload_to='mascarilla',null=True,blank=True)
	stock = models.IntegerField(default=0)

	def __str__(self):
		return self.codigo

class Pedido(models.Model):
	nombre_negocio = models.CharField(max_length=150)
	nombre_propietario = models.CharField(max_length=250)
	dni = models.CharField(max_length=8)
	celular = models.CharField(max_length=9)
	correo = models.EmailField()
	tipo_mascarilla = models.ForeignKey(Mascarilla,on_delete=models.PROTECT)
	cantidad = models.IntegerField()
	departamento = models.CharField(max_length=100)
	distrito = models.CharField(max_length=100)
	calle = models.CharField(max_length=250)
	latitud = models.CharField(max_length=20)
	longitud = models.CharField(max_length=20)
	imei = models.CharField(max_length=40,null=True)
	def __str__(self):
		return self.nombre_negocio + ' - ' + self.nombre_propietario
