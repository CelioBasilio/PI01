from django.db import models
from django.urls import reverse


# Create your models here.

class Empresa(models.Model):
    empresa_id: models.AutoField(primary_key=True, blank=False)
    nome = models.CharField(max_length=50, null=False, blank=False)
    documento = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    Projeto_id = models.IntegerField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('cadastro-empresa')


class Aluno(models.Model):
    aluno_id: models.AutoField(primary_key=True, blank=False)
    nome = models.CharField(max_length=50, null=False, blank=False)
    sobrenome = models.CharField(max_length=50, null=False, blank=False)
    telefone = models.CharField(max_length=11, null=True, blank=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)

    Projeto = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Projeto(models.Model):

    Projeto_id: models.AutoField(primary_key=True, blank=False)
    nomeProjeto = models.CharField(max_length=50, null=False, verbose_name='Nome do Projeto')
    dataInicio = models.DateTimeField(auto_now_add=True)
    atualiza = models.DateTimeField(auto_now=True)
    dataLimite = models.DateField(null=True, blank=True, verbose_name='Data Limite')
    descreva = models.TextField(null=True, blank=True)

    projeto = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeProjeto
