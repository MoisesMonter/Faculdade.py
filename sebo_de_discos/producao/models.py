from django.db import models


class Question(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    selo_fonogafico = models.CharField(max_length=200)
    ano = models.IntegerField()
    pais = models.CharField(max_length=200)
    genero = models.CharField(max_length=1)
    quantidade = models.IntegerField()