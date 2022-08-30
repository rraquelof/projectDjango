from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, View
from apps.tcc.models import Orientador
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from apps.tcc.form import OrientadorForm

class OrientadorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Orientador
    form_class = OrientadorForm
    success_message = 'Orientador cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_orientadores")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientadores - Tcc'
        context['descricao'] = 'Cadastro de Orientador(a)'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Orientador
    form_class = OrientadorForm
    success_message = 'Orientador(a) atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_orientadores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Orientadores - Tcc'
        context['descricao'] = 'Editar Orientador(a)'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class OrientadorDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Orientador
    success_message = 'Orientador(a) excluído com sucesso!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar_orientadores")

class OrientadorList(ListView):
    model = Orientador
    template_name = "cadastros/listas/orientadores.html"