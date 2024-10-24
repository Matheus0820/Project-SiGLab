from django.db import models
from datetime import datetime
from pytz import timezone

class Bolsista(models.Model):
    nome = models.CharField(max_length=255, default="")
    matricula = models.CharField(max_length=12, default="")
    curso = models.CharField(max_length=100, default="")
    grauEscolar = models.CharField(max_length=255, default="")
    tipoDeBolsa = models.CharField(max_length=255, default="")

class Horario(models.Model):
    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE, related_name="bolsista_horario")
    diaSemana = models.CharField(max_length=255, default="")
    horarioInicio = models.CharField(max_length=255, default="")
    horarioFim = models.TimeField(max_length=255, default="")

class Presenca(models.Model):
    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE, related_name="bolsista_presenca")
    data = models.DateField(default=datetime.now().astimezone(timezone('America/Recife')))
    horaEntrada = models.DateTimeField(default=datetime.now().astimezone(timezone('America/Recife')))
    horaSaida = models.DateTimeField(default="")
    
