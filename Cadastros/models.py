from django.db import models

# Create your models here.

class Dono(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateField(null=True)

    def __str__(self):
        return self.nome

class Pet(models.Model):
    petnome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    idade = models.IntegerField()
    dono = models.ForeignKey(Dono, on_delete=models.CASCADE)

    def __str__(self):
        return self.petnome





