from django.db import models
from datetime import datetime
from pytz import timezone
from django.contrib.auth.models import User

class Setor(models.Model):
    nome = models.CharField(max_length=255, default="")
    departamento = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.nome

class Laboratorio(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, related_name='laboratorios')
    nome = models.CharField(max_length=255, default="")
    localizacao = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.nome
    
    @classmethod
    def get_choices(cls):
        return [(laboratorio.id, laboratorio.nome) for laboratorio in cls.objects.all()]

class Bolsista(models.Model):
    GraisEscolares = [
        ('', 'Selecionar'),
        ('TIM', 'Técnico Integrado ao Médio'), 
        ('TS', 'Técnico Subsequente'),
        ('ES', 'Ensino Superior'),
        ('PG', 'Pós-Graduação'),
        ('DT', 'Doutorado'),
    ]

    TiposBolsa = [
        ('', 'Selecionar'),
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
    laboratorio = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.user

class HorarioBolsista(models.Model):
    DIAS_SEMANA = [
        ('', 'Selecionar'),
        ('Segunda', 'Segunda'),
        ('Terça', 'Terça'),
        ('Quarta', 'Quarta'),
        ('Quinta', 'Quinta'),
        ('Sexta', 'Sexta'),
        ('Sábado', 'Sábado'),
    ]

    HORARIOS = [
        ('', 'Selecionar'),
        ('M1: 7:00 - 7:50', 'M1: 7:00 - 7:50'),
        ('M2: 7:50 - 8:40', 'M2: 7:50 - 8:40'),
        ('M3: 8:50 - 9:40', 'M3: 8:50 - 9:40'),
        ('M4: 9:40 - 10:30', 'M4: 9:40 - 10:30'),
        ('M5: 10:40 - 11:30', 'M5: 10:40 - 11:30'),
        ('M6: 11:30 - 12:20', 'M6: 11:30 - 12:20'),
        ('Almoço: 12:00 - 12:50', 'Almoço: 12:00 - 12:50'),
        ('T1: 13:00 - 13:50', 'T1: 13:00 - 13:50'),
        ('T2: 13:50 - 14:40', 'T2: 13:50 - 14:40'),
        ('T3: 14:50 - 15:40', 'T3: 14:50 - 15:40'),
        ('T4: 15:40 - 16:30', 'T4: 15:40 - 16:30'),
        ('T5: 16:40 - 17:30', 'T5: 16:40 - 17:30'),
        ('T6: 17:30 - 18:20', 'T6: 17:30 - 18:20'),
        ('N1: 18:40 - 19:30', 'N1: 18:40 - 19:30'),
        ('N2: 19:30 - 20:20', 'N2: 19:30 - 20:20'),
        ('N3: 20:30 - 21:20', 'N3: 20:30 - 21:20'),
        ('N4: 21:20 - 22:10', 'N4: 21:20 - 22:10')
    ]

    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE, related_name="bolsista_horario")
    diaSemana = models.CharField(max_length=255, default="", choices=DIAS_SEMANA)
    horarioInicio = models.CharField(max_length=255, default="", choices=HORARIOS)
    horarioFim = models.CharField(max_length=255, default="", choices=HORARIOS)
<<<<<<< HEAD

    def __str__(self):
        return self.bolsista
=======
>>>>>>> 9b7947e1b71b797467139ec8189b18826e79fb23

class Presenca(models.Model):
    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE, related_name="bolsista_presenca")
    data = models.DateField(default=datetime.now().astimezone(timezone('America/Recife')))
    horaEntrada = models.DateTimeField(default=datetime.now().astimezone(timezone('America/Recife')))
    horaSaida = models.DateTimeField(default="")


