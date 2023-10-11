from django import forms
from django.forms.widgets import SelectDateWidget
from django.forms.widgets import DateInput
from Marketplace.models import *

class MpPessoaModel2Form(forms.ModelForm):
  pNome = forms.CharField(label='Nome', max_length=100)
  pLogin = forms.CharField(label='Login', max_length=100)
  pSenha = forms.CharField(label='Senha', max_length=100)
  pTipo = forms.CharField(label='tipoUsuario', max_length=100)

  class Meta:
    model = Pessoa
    fields = ['nome',
              'login',
              'senha',
              'tipoUsuario',
    ]

class MpMercadoriaModel2Form(forms.ModelForm):
  mNome = forms.CharField(label='Nome', max_length=100)
  mFavricacao = forms.DateField(input_formats=['%d/%m/%Y'], label='Fabricação')
  mValidade = forms.DateField(input_formats=['%d/%m/%Y'], label='Validade')
  mPreco = forms.DecimalField(max_digits=7, decimal_places=2, label='Preço')
  mCategoria = forms.CharField(label='Categoria', max_length=100)

  class Meta:
    model = Mercadoria
    fields = ['nome',
              'fabricação',
              'validade',
              'preco',
              'categoria',
    ]