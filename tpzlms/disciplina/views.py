from django.shortcuts import render
from django.views.generic import CreateView, ListView
from disciplina.models import DisciplinaDAL

def home(request):
    return render(request, 'index.html')

class Cadastro_disciplina(CreateView):
    template_name = 'cadastro-disciplina.html'
    model = DisciplinaDAL
    fields = "__all__"

class Listagem_disciplina(ListView):
    template_name = 'lista-disciplina.html'
    model = DisciplinaDAL
    context_object = 'nome'
    fields = "__all__"
