from django.shortcuts import render
from django.views.generic import CreateView, ListView
from professor.models import ProfessorDAL

def home(request):
    return render(request, 'index.html')

class Cadastro_professor(CreateView):
    template_name = 'cadastro-professor.html'
    model = ProfessorDAL
    fields = "__all__"

class Listagem_professor(ListView):
    template_name = 'lista-professor.html'
    model = ProfessorDAL
    context_object = 'nome'
    fields = "__all__"
