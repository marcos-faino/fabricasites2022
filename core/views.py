from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy #para redirecionar a página
from django.contrib import messages

from core.models import Funcionario, Servico
from core.forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('core:index')

    # Sobreescrevendo o método para inserir dados no contexto
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.all()
        context['servicos'] = Servico.objects.all()
        return context

    def form_valid(self, form):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!!!')
        return super(IndexView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar o E-mail!!!')
        return super(IndexView, self).form_invalid(form)


class ServicoDetail(DetailView):
    template_name = 'servico.html'
    model = Servico
    context_object_name = 'servico'
