from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from .views import dashboard, list_bolsistas, add_bolsista, edit_bolsista, remove_bolsista, view_horario, list_horarios, add_horario, edit_horario, remove_horario, login
=======
from .views import dashboard, list_bolsistas, add_bolsista, edit_bolsista, remove_bolsista, view_horario, list_horarios, add_horario, edit_horario, remove_horario
>>>>>>> 9b7947e1b71b797467139ec8189b18826e79fb23

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', login, name="login"),

    path('bolsistas/', list_bolsistas, name="list_bolsistas"),
    path('bolsistas/adicionar/', add_bolsista, name="add_bolsista"),
    path('bolsistas/editar/<int:id>/', edit_bolsista, name="edit_bolsista"),
    path('bolsistas/remover/<int:id>/', remove_bolsista, name="remove_bolsista"),

    path('bolsistas/horarios/view/<int:id>/', view_horario, name='view_horario'),
    path('bolsistas/horarios/<int:id>/', list_horarios, name='list_horarios'),
    path('bolsistas/horarios/adicionar/<int:id>/', add_horario, name='add_horario'),
    path('bolsistas/horarios/editar/<int:id>/', edit_horario, name='edit_horario'),
    path('bolsistas/horarios/remover/<int:id>/', remove_horario, name='remove_horario'),
]
