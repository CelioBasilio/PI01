from django.shortcuts import render
from django.views import generic
from sintproedu.core.models import Empresa


# Create your views here.
def home(request):
    return render(request, 'core/home.html')


class EmpresaCadastro(generic.CreateView):
    model = Empresa
    fields = 'nome', 'representante', 'email',

