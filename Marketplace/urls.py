"""
URL configuration for Marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from Marketplace import views
from Marketplace.views import *
from . import views

app_name = "marketplace"

urlpatterns = [
  path('admin/', admin.site.urls),
  path("", views.home, name = "homepage"),
  path("vendedor/", views.vendedor, name = "vendedor"),
  path("comprador/", views.MpMercadoriaListView.as_view(), name = "comprador"),
  path("novaMercadoria/", views.MpMercadoriaCreateView.as_view(), name = "novaMercadoria"),
  path('seguranca/cadastro/', views.cadastro, name='cadastro'),
  path('seguranca/login/', LoginView.as_view(template_name='seguranca/login.html',), name='login'),
  path('seguranca/profile/', views.paginaSecreta, name='sec-paginaSecreta'),
  path('logout/', LogoutView.as_view(next_page=reverse_lazy('homepage'),), name='logout'),
  #path('seguranca/terminaRegistro/<int:pk>/', UpdateView.as_view(template_name='seguranca/user_form.html',
  # success_url=reverse_lazy('homepage'), model=User, fields=['first_name',
  #                                                           'last_name',
  #                                                          ], ), name='sec-completaDadosUsuario'),
  #path('seguranca/login', MeuUpdateView.as_view(template_name='seguranca/login.html'), nome='sec-completaDadosUsuario'),
]