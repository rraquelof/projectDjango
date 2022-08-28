from django.db import models

# Create your models here.
class Autor(models.Model):
    id = models.IntegerField(verbose_name="id",primary_key=True)
    nome = models.CharField(verbose_name="nome",max_length=150)
    sobrenome = models.CharField(verbose_name="sobrenome",max_length=150)
    foto = models.ImageField()

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    id = models.IntegerField(verbose_name="id",primary_key=True)
    nome = models.CharField(verbose_name="nome",max_length=150)
    username = models.CharField(verbose_name="username",max_length=150)
    email = models.CharField(verbose_name="email",max_length=150)
    senha = models.CharField(verbose_name="senha",max_length=150)

    def __str__(self):
        return self.nome

class Orientador(models.Model):
    id = models.IntegerField(verbose_name="id",primary_key=True)
    nome = models.CharField(verbose_name="nome",max_length=150)
    sobrenome = models.CharField(verbose_name="sobrenome",max_length=150)
    lattes = models.CharField(verbose_name="lattes",max_length=150)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    id = models.IntegerField(verbose_name="id",primary_key=True)
    nome = models.CharField(verbose_name="nome",max_length=150)
    modalidade = models.CharField(verbose_name="modalidade",max_length=150)

    def __str__(self):
        return self.nome

class Tcc(models.Model):
    id = models.IntegerField(verbose_name="id",primary_key=True)
    titulo = models.CharField(verbose_name="titulo",max_length=150)
    autor = models.ManyToManyField(Autor)
    orientador = models.ManyToManyField(Orientador)
    curso = models.CharField(verbose_name="Curso",max_length=150)
    ano = models.IntegerField(verbose_name="Ano")
    resumo = models.TextField(verbose_name="Resumo")
    arquivo = models.CharField(verbose_name="Arquivo",max_length=150)
    palavras_chave = models.TextField(verbose_name="Palavras chave")

    def __str__(self):
        return self.nome
