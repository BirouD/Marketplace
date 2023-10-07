from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from Marketplace.models import *
from Marketplace.forms import *

# Create your views here.

def home(request):           #TELA LOGIN/SIGN
  return render(request, 'Marketplace/home.html')

def vendedor(request):       #TELA VEDENDOR
  return render(request, 'Marketplace/vendedor.html')

def comprador(request):      #TELA COMPRADOR
  return render(request, 'Marketplace/comprador.html')

def cadastro(request):       #TELA cadastro que direciona para o Home/Login
  return render(request, 'Marketplace/cadastro.html')

def novaMercadoria(request): #TELA de cadastro de mercadorias
  return render(request, 'Marketplace/novaMercadoria.html')

#Pessoa
class MpPessoaCreateView(View):
  def get(self, request, *args, **kwargs):
    pessoas = Pessoa.objects.all()
    context = { 'formulario':MpPessoaModel2Form, }
    return render(request, 'Marketplace/cadastro.html', context)
  
  def post(self, request, *args, **kwargs):
    formulario = MpPessoaModel2Form(request.POST)
    if formulario.is_valid():
      pessoa = formulario.save()
      pessoa.save()
      return HttpResponseRedirect(reverse_lazy("marketplace:cadastro"))

class MpPessoaUpdateView(View):
  def get(self, request, pk, *args, **kwargs):
    pessoas = Pessoa.objects.all()
    context = { 'pessoas':pessoas, }
    return render(request, 'Marketplace/home.html', context)
  
  def post(self, request, pk, *args, **kwargs):
    formulario = MpPessoaModel2Form(request.POST)
    if formulario.is_valid():
      pessoa = formulario.save()
      pessoa.save()
      return HttpResponseRedirect(reverse_lazy("marketplace:cadastro"))
    
    else:
      contexto = { 'pessoa': formulario, }
      return render(request, 'Marketplace/cadastro.html')
  
#Mercadoria
class MpMercadoriaListView(View):
  def get(self, request, *args, **kwargs):
    mercadorias = Mercadoria.objects.all()
    contexto = { 'mercadoria':mercadorias, }
    return render(request, 'Marketplace/comprador.html', contexto)
  
class MpMercadoriaCreateView(View):
  def get(self, request, *args, **kwargs):
    mercadorias = Mercadoria.objects.all()
    context = { 'formulario':MpPessoaModel2Form, }
    return render(request, 'Marketplace/novaMercadoria.html', context)
  
  def post(self, request, *args, **kwargs):
    formulario = MpMercadoriaModel2Form(request.POST)
    if formulario.is_valid():
      mercadoria = formulario.save()
      mercadoria.save()
      return HttpResponseRedirect(reverse_lazy("marketplace:novaMercadoria"))

class MpMercadoriaUpdateView(View):
  def get(self, request, pk, *args, **kwargs):
    mercadorias = Mercadoria.objects.all()
    context = { 'mercadoria':mercadorias }
    return render(request, 'Marketplace/comprador.html', context)
  
  def post(self, request, pk, *args, **kwargs):
    formulario = MpMercadoriaModel2Form(request.POST)
    if formulario.is_valid():
      mercadoria = formulario.save()
      mercadoria.save()
      return HttpResponseRedirect(reverse_lazy("marketplace:novaMercadoria"))
    
    else:
      contexto = { 'mercadoria': formulario, }
      return render(request, 'Marketplace/novaMercadoria.html')