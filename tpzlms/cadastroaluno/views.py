from django.shortcuts import render
from django.views.generic import CreateView, ListView
from cadastroaluno.models import AlunoDAL

def home(request):
    return render(request, 'index.html')


class Cadastro_aluno(CreateView):
    template_name = 'cadastro-aluno.html'
    model = AlunoDAL
    fields = "__all__"


class Listagem_aluno(ListView):
    template_name = 'lista-aluno.html'
    model = AlunoDAL
    context_object = 'nome'
    fields = "__all__"
