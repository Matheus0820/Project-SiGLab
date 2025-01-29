from django.db import models
from datetime import datetime
from pytz import timezone
from django.contrib.auth.models import User

class Bolsista(models.Model):
    GraisEscolares = [
        ('None', 'Selecionar'),
        ('TIM', 'Técnico Integrado ao Médio'), 
        ('TS', 'Técnico Subsequente'),
        ('ES', 'Ensino Superior'),
        ('PG', 'Pós-Graduação'),
        ('DT', 'Doutorado'),
    ]

    TiposBolsa = [
        ('None', 'Selecionar'),
        ('VLT', 'Voluntária - 10h'),
        ('RMN1', 'Remunerada - 12h a 20h'),
        ('RMN2', 'Remunerada - 30h'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_bolsista")
    matricula = models.CharField(max_length=12, default="")
    cpf = models.CharField(max_length=14, default="")
    curso = models.CharField(max_length=255, default="")
    grauEscolar = models.CharField(max_length=255, default="", choices=GraisEscolares)
    tipoDeBolsa = models.CharField(max_length=255, default="", choices=TiposBolsa)

class Horario(models.Model):
    DIAS_SEMANA = [
        ('None', 'Selecionar'),
        ('seg', 'Segunda'),
        ('ter', 'Terça'),
        ('qua', 'Quarta'),
        ('qui', 'Quinta'),
        ('sex', 'Sexta'),
        ('sab', 'Sábado'),
    ]

    HORARIOS = [
        ('None', 'Selecionar'),
        ('m1', 'M1: 7:00 - 7:50'),
        ('m2', 'M2: 7:50 - 8:40'),
        ('m3', 'M3: 8:50 - 9:40'),
        ('m4', 'M4: 9:40 - 10:30'),
        ('m5', 'M5: 10:40 - 11:30'),
        ('m6', 'M6: 11:30 - 12:20'),
        ('am', 'AM: 12:00 - 12:50'),
        ('t1', 'T1: 13:00 - 13:50'),
        ('t2', 'T2: 13:50 - 14:40'),
        ('t3', 'T3: 14:50 - 15:40'),
        ('t4', 'T4: 15:40 - 16:30'),
        ('t5', 'T5: 16:40 - 17:30'),
        ('t6', 'T6: 17:30 - 18:20'),
        ('n1', 'N1: 18:40 - 19:30'),
        ('n2', 'N2: 19:30 - 20:20'),
        ('n3', 'N3: 20:30 - 21:20'),
        ('n4', 'N4: 21:20 - 22:10'),
    ]

    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE, related_name="bolsista_horario")
    diaSemana = models.CharField(max_length=255, default="", choices=DIAS_SEMANA)
    horarioInicio = models.CharField(max_length=255, default="", choices=HORARIOS)
    horarioFim = models.TimeField(max_length=255, default="", choices=HORARIOS)

class Presenca(models.Model):
    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE, related_name="bolsista_presenca")
    data = models.DateField(default=datetime.now().astimezone(timezone('America/Recife')))
    horaEntrada = models.DateTimeField(default=datetime.now().astimezone(timezone('America/Recife')))
    horaSaida = models.DateTimeField(default="")
    
