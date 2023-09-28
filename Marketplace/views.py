from django.shortcuts import render
# Create your views here.

def home(request):      #TELA LOGIN/SIGN
  return render(request, 'Marketplace/home.html')

def vendedor(request):  #TELA VEDENDOR
  return render(request, 'Marketplace/vendedor.html')

def comprador(request): #TELA COMPRADOR
  return render(request, 'Marketplace/comprador.html')