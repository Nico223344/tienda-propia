from django.shortcuts import render ,get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'Principal.html')

def index_admin(request):
    return render(request, 'administrador/index.html')



#USUARIO
def index_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        password = request.POST.get('pass')

        usuario = Usuario(nombre=nombre, password=password, email=correo)
        usuario.save()

    usuarios = Usuario.objects.all()
    context = { 'usuarios' : usuarios }
    return render(request, 'administrador/usuario/index.html', context)

def create_usuario(request):
     return render(request, 'administrador/usuario/create.html')

def edit_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        password = request.POST.get('pass')

        usuario.nombre = nombre
        usuario.email = correo
        usuario.password = password
        usuario.save()
    
    context = {'usuario': usuario}

    return render(request, 'administrador/usuario/edit.html', context)

def delete_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return render(request, 'administrador/usuario/index.html')




#PRODUCTO
def index_producto(request):
    if request.method == 'POST':
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')

        producto = Producto(precio=precio, descripcion=descripcion,)
        producto.save()

    productos = Producto.objects.all()
    context = { 'productos' : productos }
    return render(request, 'administrador/producto/index.html', context)

def create_producto(request):
     return render(request, 'administrador/producto/create.html')

def edit_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        

        producto.precio = precio
        producto.descripcion = descripcion
        producto.save()
    
    context = {'producto': producto}

    return render(request, 'administrador/producto/edit.html', context)

def producto_delete(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return render(request, 'administrador/producto/index.html')

#TIENDA
def index_tienda(request):
    return render(request, 'masterbikes/index.html')