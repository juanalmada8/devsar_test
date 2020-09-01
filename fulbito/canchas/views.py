from django.shortcuts import render
from .models import Cancha

# Create your views here.

def listar_canchas(request):
    lista_cancha = Cancha.objects.all()
    return render(request, 'canchas/canchas.html', {'cancha': lista_cancha})