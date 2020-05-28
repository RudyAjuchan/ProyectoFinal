from django.shortcuts import render,redirect
from zapateria.forms import ClientesForm, ZapatoForm, VentaForm, FacturaForm
from zapateria.models import Clientes, Zapato, Venta, Factura
from django.contrib import messages
from datetime import datetime
# Codigo para clientes
def index(request):
    return render(request, 'index.html')

def registro_clientes(request):
    if request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Dato Guardado con exito')
                return redirect('http://localhost:8000/mostrar_clientes/')
            except:
                pass
    else:
        form = ClientesForm()
    return render(request, 'registro_cliente.html', {'form':form})

def mostrar_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, "mostrar_clientes.html", {'clientes':clientes})

def eliminar_cliente(request, id):
    clientes = Clientes.objects.get(id=id)
    clientes.delete()
    messages.success(request, 'Dato eliminado')
    return redirect('http://localhost:8000/mostrar_clientes/')

def actualizar_cliente(request, id):
    clientes = Clientes.objects.get(id=id)
    form = ClientesForm(instance=clientes)

    if request.method=='POST':
        form = ClientesForm(request.POST,instance=clientes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dato actualizado')
            return redirect('http://localhost:8000/mostrar_clientes/')
    return render(request,'actualizar_cliente.html',{'clientes':clientes})

#codigo para zapatos*********************************
def registro_zapatos(request):
    if request.method == "POST":
        form = ZapatoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Dato Guardado con exito')
                return redirect('http://localhost:8000/mostrar_zapatos/')
            except:
                pass
    else:
        form = ZapatoForm()
    return render(request, 'registro_zapatos.html', {'form':form})

def mostrar_zapatos(request):
    zapatos = Zapato.objects.all()
    return render(request, "mostrar_zapatos.html", {'zapatos':zapatos})

def eliminar_zapato(request, id):
    zapatos = Zapato.objects.get(id=id)
    zapatos.delete()
    messages.success(request, 'Dato eliminado')
    return redirect('http://localhost:8000/mostrar_zapatos/')

def actualizar_zapato(request, id):
    zapatos = Zapato.objects.get(id=id)
    form = ZapatoForm(instance=zapatos)

    if request.method=='POST':
        form = ZapatoForm(request.POST,instance=zapatos)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dato actualizado')
            return redirect('http://localhost:8000/mostrar_zapatos/')
    return render(request,'actualizar_zapatos.html',{'zapatos':zapatos})

#codigo para inventarios********************
def mostrar_inventario(request):
    zapatos = Zapato.objects.all()
    return render(request, "mostrar_inventario.html", {'zapatos':zapatos})

def venta(request):
    id_Factura=obtener_id()
    zapatos = Zapato.objects.all()
    form = VentaForm()
    return render(request, "venta.html", {'zapatos':zapatos,'form':form,'id_Factura':id_Factura})

def obtener_id():
    contador=0
    factura=Factura.objects.all()
    for datos in factura:
        print(datos.id)
        contador=contador+1
    contador=contador+1
    return contador

def guardar_venta(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Producto agregado al carrito')
                return redirect('http://localhost:8000/mostrar_carrito/')
            except:
                pass
    else:
        form = ZapatoForm()
    return redirect('http://localhost:8000/mostrar_carrito/')

def guardar_venta2(request, id_zapato, precio):
    id_Factura=obtener_id()
    zapato=Zapato(id=id_zapato)
    datos= Venta()
    datos.Cantidad=1
    datos.Total=float(precio)
    datos.id_Factura=id_Factura
    datos.id_Zapato=zapato
    datos.save()
    messages.success(request, 'Producto agregado al carrito')
    return redirect('http://localhost:8000/mostrar_carrito/')

def mostrar_carrito(request):
    id_Factura=obtener_id()
    ventas = Venta.objects.filter(id_Factura=id_Factura)
    return render(request, "mostrar_carrito.html", {'ventas':ventas})

def eliminar_venta(request, id):
    ventas = Venta.objects.get(id=id)
    ventas.delete()
    messages.success(request, 'Dato eliminado')
    return redirect('http://localhost:8000/mostrar_carrito/')

def pagar(request):   
    id_Factura=obtener_id()
    Total_final=0
    ventas = Venta.objects.filter(id_Factura=id_Factura) 
    clientes=Clientes.objects.all()
    for datos in ventas:
        Total_final=Total_final+datos.Total
    if request.method == "POST":
        form = FacturaForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Producto agregado al carrito')
                return redirect('http://localhost:8000/factura/')
            except:
                pass
    else:
        form = FacturaForm()
    return render(request, "pagar.html", {'ventas':ventas,'form':form,'Total_final':Total_final,'clientes':clientes})

def factura(request):
    id_Factura=obtener_id()
    id_Factura=id_Factura-1
    Total_final=0
    fecha = datetime.now()
    ventas = Venta.objects.filter(id_Factura=id_Factura)
    facturas = Factura.objects.get(id=id_Factura)
    clientes=Clientes.objects.get(id=facturas.id_Cliente.id )
    for datos in ventas:
        Total_final=Total_final+datos.Total
    return render(request, "factura.html",{'id_Factura':id_Factura,'ventas':ventas,'Total_final':Total_final,'clientes':clientes,'fecha':fecha})

def filtro(request):
    form=ZapatoForm()
    return render(request, 'Filtro.html',{'form':form})

def Productos(request):
    form = ZapatoForm(request.POST)
    genero=form.data['Genero']
    tipo=form.data['Tipo']
    zapatos = Zapato.objects.filter(Genero=genero, Tipo=tipo)    
    return render(request, "productos.html", {'zapatos':zapatos})
