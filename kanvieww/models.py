from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    documento = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    edad = models.IntegerField()
    
class Empleado(models.Model):
    documento = models.CharField(max_length=40)
    nombre = models.CharField(max_length=100)
    #tapiceros, costura, gerente, secretario
    cargos = (
        ("costr","Costurero"),
        ("tapcr", "Tapicero"),
        ("gerente","Gerente"),
        ("secre", "Secretario")
    )
    cargo = models.CharField(choices=cargos, max_length=10, default="tapcr")
    celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    salario = models.DecimalField(decimal_places=2, max_digits=10)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    tareas_realizadas = models.IntegerField()
    
class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    documento = models.CharField(max_length=50)
    
class AnalisisFinanciero(models.Model):
    gastos = models.DecimalField(decimal_places=2, max_digits=12)
    fuentes_ingresos = models.DecimalField(decimal_places=2, max_digits=12)
    productos_vendidos = models.IntegerField()
    id_administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.DecimalField(decimal_places=2, max_digits=12)
    descripcion = models.CharField(max_length=1000)
    codigo_producto = models.CharField(max_length=6)
    
class Inventario(models.Model):
    cantidad = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
class Catalogo(models.Model):
    categorias = models.CharField(max_length=100)
    id_inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
class Pedido(models.Model):
    codigo_pedido = models.CharField(max_length=6)
    fecha_creacion = models.DateField()
    hora_creacion = models.DateTimeField()
    est = (
        ("activo","Activo"),
        ("inactivo","Inactivo")
    )
    estado = models.CharField(choices=est, max_length=10, default="activo")
    evidencias = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=1000)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    
estkan = (
        ("pendiente","Pendiente"),
        ("en progreso","En progreso"),
        ("completado","Completado")
    )
class TareasPedido(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(choices=estkan, max_length=20, default="pendiente")
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    
class Actividades(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(choices=estkan, max_length=20, default="pendiente")
    id_tarea = models.ForeignKey(TareasPedido, on_delete=models.CASCADE)
    

class Historial(models.Model):
    hora_creacion = models.TimeField()
    fecha_creacion = models.DateField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    

class Calendario(models.Model):
    fecha = models.DateField()
    año = models.IntegerField()
    mes = models.IntegerField()
    nombre_mes = models.CharField(max_length=20)
    dia = models.IntegerField()
    nombre_dia = models.CharField(max_length=20)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    

    
    
    

    
    
    
