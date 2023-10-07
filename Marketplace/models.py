from django.db import models

class Pessoa(models.Model):
  nome = models.CharField(max_length=100, help_text='Entre o nome')
  login = models.CharField(max_length=100, help_text='Entre o login')
  senha = models.CharField(max_length=16, help_text='Entre a senha')
  tipoUsuario = models.CharField(max_length=9)

  def __str__(self):
    return self.nome
  
class Mercadoria(models.Model):
  nome = models.CharField(max_length=100, help_text='Entre o nome')
  categoria = models.CharField(max_length=100, help_text='Entre a categoria')
  fabricação = models.DateField(help_text='Fabricação no formato DD/MM/AAAA', verbose_name='Data de fabricação')
  validade = models.DateField(help_text='Validade no formato DD/MM/AAAA', verbose_name='Data de validade')
  preco = models.DecimalField(max_digits=7, decimal_places=2, help_text='Preço no formato xxxxx,xx', verbose_name='Preço')

  def __str__(self):
    return self.nome 