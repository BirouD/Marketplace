from django.db import models

class Pessoa(models.Model):
  nome = models.CharField(max_length=100, help_text='Entre o nome')
  login = models.CharField(max_length=100, help_text='Entre o login')
  senha = models.CharField(max_length=16, help_text='Entre a senha')
  tipoUsuario = models.CharField(max_length=9)

  def __str__(self):
    return self.nome