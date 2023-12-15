from django.db import models

# Create your models here.


class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=100, help_text='Nome da Empresa')

    def __str__(self):
        return self.nome_empresa