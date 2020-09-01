from django import forms
from .models import Reserva
from canchas.views import listar_canchas

""" def retornarFecha(modelo):
    fechas = modelo.objects.all()
    lista = []
    for fecha in fechas:
        lista.append(fecha.fecha_consulta)
    return  lista
#a = FechaConsulta.objects.all() """
#fechas = [i.fecha_consulta for i in FechaConsulta.objects.all()]


class ReservaForm(forms.ModelForm):

    cancha = forms.CharField(label='Cancha',required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'placeholder': "Cancha"}))
    cliente = forms.CharField(label='Cliente',required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'placeholder': "Cliente"}))
    empleado = forms.CharField(label='Empleado',required=True, widget=forms.TextInput(
        attrs={'class':"form-control", 'placeholder': "Empleado"}))
    fecha_turno = forms.DateField(label= 'Fecha', widget=forms.SelectDateWidget(years = range(2020,2021),
        attrs={'class':"form-control", 'placeholder': "Fecha"}))
    hora_turno = forms.TimeField(label='Hora Reserva', widget=forms.TextInput(
        attrs={'class':"form-control", 'placeholder': "HH:MM:SS"}))

    
    class Meta:

        model = Reserva
        fields = ['cancha', 'cliente','empleado','fecha_turno','hora_turno']