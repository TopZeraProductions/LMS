from django.shortcuts import render
from django.views.generic import CreateView, ListView
from cadastroaluno.models import Inscricao
from cadastroaluno.forms import InscricaoForm

def home(request):
    return render(request, 'index.html')


class Criar(CreateView):

    template_name = 'cadastro.html'
    model = Inscricao
    fields = "__all__"


class Lista(ListView):

    template_name = 'lista.html'
    model = Inscricao
    context_object = 'nome'
    fields = "__all__"
