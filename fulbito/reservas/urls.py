from django.urls import path
from reservas import views

urlpatterns = [
    path('', views.crear_reserva, name="reservas"),
    path('eliminar/', views.eliminar, name="eliminar"),
    path('modificar/', views.modificar, name="modificar"),

]