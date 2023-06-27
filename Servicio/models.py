from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre 

class Producto(models.Model):
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.precio
    
class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion
    
class Cliente(models.Model):
    rut = models.CharField(max_length=12, blank=False, null=False)
    nombre =models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class FormaPago(models.Model):
    numero_tarjeta= models.CharField( max_length=50)
    descripcion = models.CharField( max_length=100)
    valida = models.DateField(auto_now=False, auto_now_add=False)
    nombre_titular = models.CharField( max_length=100)

    
    def __str__(self):
        return self.numero_tarjeta

class Boleta(models.Model):
    FormaPago = models.ForeignKey( FormaPago, on_delete=models.CASCADE)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class DetalleBoleta(models.Model):
    Boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


    


        
    

