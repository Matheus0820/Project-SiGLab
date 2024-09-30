from django.db import models

class Bolsista(models.Model):
    nome = 0
    matricula = 0
    curso = 0
    grauEscolar = 0
    tipoDeBolsa = 0

class Horario(models.Model):
    diaSemana = 0
    horarioDia = 0

class Presenca(models.Model):
    bolsista = 0
    data = 0
    horaEntrada = 0
    horaSaida = 0
