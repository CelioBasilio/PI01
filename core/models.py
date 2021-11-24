from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome da Empresa')
    representante = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome do Representante')
    sobrenomerepre = models.CharField(max_length=50, null=False, blank=False, verbose_name='Sobrenome do Representante')
    telefone = models.CharField(max_length=11, null=True, blank=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    usuarioEmpresa = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.representante, self.email)


class Projeto(models.Model):

    titulo = models.CharField(max_length=50, null=False, verbose_name='Nome do Projeto')
    dataInicio = models.DateTimeField(auto_now_add=True, verbose_name='Data Inicial')
    atualiza = models.DateTimeField(auto_now=True)
    dataLimite = models.DateField(null=False, blank=False, verbose_name='Data Limite')
    descreva = models.TextField(null=False, blank=False, verbose_name='Descreva o Projeto')
    usuarioEmpresa = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} ({})".format(self.titulo,self.dataInicio, self.usuarioEmpresa)


class Aluno(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome do Aluno')
    sobrenome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Sobrenome')
    telefone = models.CharField(max_length=11, null=True, blank=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    usuarioAluno = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.telefone, self.email)

