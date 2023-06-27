from django.urls import path
from .views import index, index_admin, index_usuario, create_usuario, edit_usuario, delete_usuario, index_producto, create_producto, edit_producto, producto_delete, index_tienda
from .forms import *

urlpatterns = [
    path("", index, name="index"),
    path("administrador/", index_admin, name="admin_index"),
    path("administrador/usuarios", index_usuario, name="usuario_index"),
    path("administrador/usuarios/create", create_usuario, name="usuario_create"),
    path("administrador/usuarios/<int:id>/edit", edit_usuario, name="usuario_edit"),
    path("administrador/usuarios/<int:id>/delete", delete_usuario, name="usuario_delete"),
    path("administrador/productos", index_producto, name="producto_index"),
    path("administrador/productos/create", create_producto, name="producto_create"),
    path("administrador/productos/<int:id>/edit", edit_producto, name="producto_edit"),
    path("administrador/productos/<int:id>/delete", producto_delete, name="producto_delete"),
    path("MasterBikes/", index_tienda, name="tienda_index"),
]