from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.


class UsuarioCreate(CreateView):
    template_name = 'usuarios/form.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='empresa')

        url = super(UsuarioCreate, self).form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        return url