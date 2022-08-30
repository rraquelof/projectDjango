from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, View
from apps.tcc.models import Usuario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from apps.tcc.form import UsuarioForm

class UsuariosList(ListView):
    model = Usuario
    template_name = "cadastros/detalhes/usuarios.html"