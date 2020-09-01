from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Reserva
from .forms import ReservaForm
# Create your views here.

def eliminar(request):
    return render(request, 'reservas/eliminar.html')

def modificar(request):
    return render(request, 'reservas/modificar.html')

def crear_reserva(request):
    if request.method == 'POST':
        reserva = ReservaForm(request.POST)
        if reserva.is_valid():
            reserva.save()
            return redirect(reverse('reservas')+"?ok")
    else:
        reserva = ReservaForm()

    return render(request, 'reservas/crear_reserva.html', {'reserva_form':reserva})

def listar_reserva(request):
    listar_reserva = Reserva.objects.all()
    return render(request, 'reservas/crear_reservas.html', {'reservas': listar_reserva})

def editar_reserva(request, id):
    reserva = Reserva.objects.get(id = id)
    if request.method=='GET':
        reserva= ReservaForm(instance = reserva)
    else:
        reserva = ReservaForm(request.POST, instance = reserva)
        if reserva.is_valid():
            reserva.save()
        redirect('reservas')
    return render(request, 'reservas/crear_reserva.html', {'reserva_form': reserva})