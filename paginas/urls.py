from django.urls import path
from .views import PaginaInicial, Sobre

urlpatterns = [
    # path('endereço/', MinhaView.as_view(), name='nome da url'),
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    ]
