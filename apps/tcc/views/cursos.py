from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from apps.tcc.form import CursoForm
from apps.tcc.models import Curso
from apps.tcc.form import CursoForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages

class CursoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Curso
    form_class = CursoForm
    success_message = 'Curso cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_cursos")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Cursos - Repositório'
        context['descricao'] = 'Cadastro de Curso'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class CursoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Curso
    form_class = CursoForm
    success_message = 'Curso atualizado com sucesso!'
    template_name = "cadastros/form.html"
    """ success_url = reverse_lazy("listar_cursos") """

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Curso - Biblioteca'
        context['descricao'] = 'Editar Curso'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class CursoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Curso
    success_message = 'Curso excluída com sucesso!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar_cursos")

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Curso - Biblioteca'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CursoDelete, self).delete(request, *args, **kwargs)


class CursosList(ListView):
    model = Curso
    template_name = "cadastros/listas/cursos.html"



