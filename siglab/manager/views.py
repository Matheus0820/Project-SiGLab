from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth import authenticate

from .models import *
from .forms import *

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def list_bolsistas(request):
    if request.method == 'GET':
        bolsistas = Bolsista.objects.all()

        context = {
            'bolsistas': bolsistas
        }
        return render(request, 'pages/list_bolsistas.html', context)

def add_bolsista(request):
    if request.method == 'GET':
        formUser = FormUser()
        formBolsista = FormBolsista()

        context = {
            'formUser': formUser,
            'formBolsista': formBolsista,
        }
        return render(request, 'forms/add_bolsista.html', context)

    elif request.method == 'POST':
        formUser = FormUser(request.POST)
        formBolsista = FormBolsista(request.POST)

        if formUser.is_valid():
            bolsista_user = formUser.save()

            bolsista = formBolsista.save(commit=False)
            bolsista.user = bolsista_user
            bolsista.save()

            messages.success(request, "Bolsista adicionado com sucesso!")
            return redirect(list_bolsistas)

        else:
            context = { 
                'formUser': formUser,
                'formBolsista': formBolsista,
            }

            messages.error(request, "Algum dado foi insirido de forma errada ou não foi fornecido!")
            return render(request, 'forms/add_bolsista.html', context)





def edit_bolsista(request, id):
    bolsista = Bolsista.objects.get(id=id)
    user_bolsista = bolsista.user

    if request.method == 'GET':
        formBolsista = FormBolsista(instance=bolsista)
        formUser = FormEditUser(instance=user_bolsista)
        context = {
            'id': bolsista.id,
            'formBolsista': formBolsista,
            'formUser': formUser,
        }

        return render(request, 'forms/edit_bolsista.html', context)

    elif request.method == 'POST':
        formBolsista = FormBolsista(request.POST, instance=bolsista)
        formUser = FormEditUser(request.POST, instance=user_bolsista)

        if formUser.is_valid() and formBolsista.is_valid():
            formUser.save()
            formBolsista.save()

            messages.success(request, "Dados do bolsista editados com sucesso!")
            return redirect(list_bolsistas)

        else:
            context = {
                'id': bolsista.id,
                'formBolsista': formBolsista,
                'formUser': formUser,
            }
            messages.error(request, "O Formulário possui alguma inconsistência!")
            return render(request, 'forms/edit_bolsista.html', context)


def remove_bolsista(request, id):
    bolsista_user = User.objects.get(id=id)
    bolsista_user.delete()

    messages.success(request, "Bolsista removido do SigLab com sucesso")
    return redirect(list_bolsistas)

def view_horario(request, id):
    bolsista = Bolsista.objects.get(id=id)
    horarios = Horario.objects.filter(bolsista=bolsista)

    context = {
        'horarios': horarios, 
        'id': id,
        'bolsista': bolsista,
    }
    return render(request, 'pages/view_horarios_bolsistas.html', context)

def list_horarios(request, id):
    bolsista = Bolsista.objects.get(id=id)
    horarios = Horario.objects.filter(bolsista=bolsista)

    context = {
        'horarios': horarios, 
        'id': id, 
        'bolsista': bolsista,
    }
    return render(request, 'pages/list_horarios.html', context)

def add_horario(request, id):
    bolsista = Bolsista.objects.get(id=id)
    if request.method == 'GET':
        form = FormHorario()

        context = {
            'form': form,
            'id': id,
            'bolsista': bolsista,
        }
        return render(request, 'forms/add_horario.html', context)

    elif request.method == 'POST':
        form = FormHorario(request.POST)

        horario = form.save(commit=False)
        horario.bolsista = bolsista
        horario.save()

        messages.success(request, 'Horário adicionado com sucesso.')
        list_horarios_url = reverse('list_horarios', args=[id])
        return redirect(list_horarios_url)        

def edit_horario(request, id):
    horario = Horario.objects.get(id=id)
    if request.method == 'GET':
        form = FormHorario(instance= horario)

        context = {
            'form': form,
            'id': id,
        }

        return render(request, 'forms/edit_horario.html', context)
    
    elif request.method == 'POST':
        form = FormHorario(request.POST, instance=horario)
        bolsista_id = horario.bolsista.id
        

        if form.is_valid():
            form.save()
            
            messages.success(request, 'Horário editado com sucesso.')
            list_horarios_url = reverse('list_horarios', args=[bolsista_id])
            return redirect(list_horarios_url)
        
        else:
            context = {
                'form': form,
                'id': id,
            }

            messages.error('Algum dado foi preenchido incorretamente.')
            return render(request, 'forms/edit_horario.html', context)
            

def remove_horario(request, id):
    horario = Horario.objects.get(id=id)
    bolsista_id = horario.bolsista.id

    list_horarios_url = reverse('list_horarios', args=[bolsista_id])

    try:
        horario.delete()
        messages.success(request, "Horário removido com sucesso.")
        return redirect(list_horarios_url)
    
    except Exception as e:
        messages.error(request, e)
        return redirect(list_horarios_url)
