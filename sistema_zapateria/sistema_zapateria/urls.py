"""sistema_zapateria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from zapateria import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('registro_clientes/',views.registro_clientes),
    path('mostrar_clientes/',views.mostrar_clientes),
    path('eliminar_cliente/<int:id>',views.eliminar_cliente),
    path('editar_cliente/<int:id>',views.actualizar_cliente),
    path('registro_zapatos/',views.registro_zapatos),
    path('mostrar_zapatos/',views.mostrar_zapatos),
    path('eliminar_zapato/<int:id>',views.eliminar_zapato),
    path('editar_zapato/<int:id>',views.actualizar_zapato),
    path('mostrar_inventario/',views.mostrar_inventario),
    path('venta/',views.venta),
    path('guardar_venta/',views.guardar_venta),
    path('mostrar_carrito/',views.mostrar_carrito),
    path('eliminar_venta/<int:id>',views.eliminar_venta),
    path('pagar/',views.pagar),
    path('factura/',views.factura),
    path('Productos/',views.Productos),
    path('filtro/',views.filtro),
    path('guardar_venta2/<int:id_zapato>/<str:precio>',views.guardar_venta2),
]

urlpatterns += staticfiles_urlpatterns()
