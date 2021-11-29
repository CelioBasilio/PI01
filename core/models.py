from django.db import models


# Create your models here.

class Empresa(models.Model):
    username = models.CharField(max_length=30, null=True)
    password = models.Value
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome da Empresa')
    representante = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome do Representante')
    sobrenomerepre = models.CharField(max_length=50, null=False, blank=False, verbose_name='Sobrenome do Representante')
    telefone = models.CharField(max_length=11, null=True, blank=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.representante, self.email)


class Projeto(models.Model):

    STATUS_CHOICES = (
        ("P", "Projeto postado"),
        ("F", "Em andamento"),
        ("E", "Realizados"),
    )

    titulo = models.CharField(max_length=50, null=False, verbose_name='Titulo do Projeto')
    dataInicio = models.DateTimeField(auto_now_add=True, verbose_name='Data Inicial')
    atualiza = models.DateTimeField(auto_now=True)
    dataLimite = models.DateField(null=False, blank=False, verbose_name='Data Limite')
    descreva = models.TextField(null=False, blank=False, verbose_name='Descreva o Projeto')
    username = models.OneToOneField(Empresa, on_delete=models.CASCADE, related_name='Empresa')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return "{} {} ({})".format(self.titulo, self.dataInicio, self.descreva)


class Aluno(models.Model):
    username = models.CharField(max_length=30, null=True)
    password = models.Value
    nome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nome do Aluno')
    sobrenome = models.CharField(max_length=50, null=False, blank=False, verbose_name='Sobrenome')
    telefone = models.CharField(max_length=11, null=True, blank=True, verbose_name='Telefone')
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)

    Projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='requisita')

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.telefone, self.email)
