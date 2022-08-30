from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from apps.tcc.form import TccForm
from apps.tcc.models import Tcc, Autor
from apps.tcc.form import TccForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages

class TccCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tcc
    form_class = TccForm
    success_message = 'Tcc cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_tccs_usuario")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tccs - Repositório'
        context['descricao'] = 'Cadastro de Tcc'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class TccUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tcc
    form_class = TccForm
    success_message = 'Tcc atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_tccs_usuario")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tcc - Biblioteca'
        context['descricao'] = 'Editar Tcc'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TccDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Tcc
    success_message = 'Tcc excluída com sucesso!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar_tccs_usuario")

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Tcc - Biblioteca'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TccDelete, self).delete(request, *args, **kwargs)

class TccDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Tcc
    template_name = "cadastros/detalhes/tcc.html"

""" class TccDetailPublicado(DetailView):
    model = Tcc
    template_name = "cadastros/detalhes/tcc.html"
 """
class TccListPorUsuario(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tcc
    template_name = "cadastros/listas/dashboard.html"

    def get_queryset(self):
        return Tcc.objects.filter(usuario=self.request.user)
""" 
class TccPublicadoList(ListView):
    model = Tcc
    template_name = "index.html"

    def get_queryset(self):
        return Tcc.objects.filter(publicado=True) """

class TccAutorList(ListView):
    model = Tcc
    template_name = "index.html"

"""     def get_queryset(self):
        self.object_list = Tcc.objects.filter(publicado=True, autor=Autor.objects.get(pk=self.kwargs['autor']))
        return self.object_list """

class TccList(ListView):
    model = Tcc
    template_name = "index.html"