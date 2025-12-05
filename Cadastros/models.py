from django.db import models

# Create your models here.

class Dono(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.EmailField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome





