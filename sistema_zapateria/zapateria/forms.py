from django import forms
from zapateria.models import Clientes,Zapato,Venta, Factura

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"

class ZapatoForm(forms.ModelForm):
    class Meta:
        model = Zapato
        fields = "__all__"

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = "__all__"

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = "__all__"


