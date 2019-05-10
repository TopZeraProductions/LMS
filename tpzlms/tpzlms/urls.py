from professor import views as professor_views
from cadastroaluno import views as aluno_views
from disciplina import views as disciplina_views

from django.contrib import admin
from django.conf.urls import url

admin.autodiscover()
urlpatterns = [

    url(r'^$', aluno_views.home, name='home'),

    url(r'^aluno/cadastro/'     , aluno_views.Cadastro_aluno.as_view(), name='AlunoCadastro'),
    url(r'^aluno/listagem/'     , aluno_views.Listagem_aluno.as_view(), name='AlunoListagem'),
    url(r'^aluno/$'             , aluno_views.Listagem_aluno.as_view(), name='AlunoListagem'),

    url(r'^professor/cadastro/' , professor_views.Cadastro_professor.as_view(), name='ProfessorCadastro'),
    url(r'^professor/listagem/' , professor_views.Listagem_professor.as_view(), name='ProfessorListagem'),
    url(r'^professor/$'         , professor_views.Listagem_professor.as_view(), name='ProfessorListagem'),

    url(r'^disciplina/cadastro/', disciplina_views.Cadastro_disciplina.as_view(), name='DisciplinaCadastro'),
    url(r'^disciplina/listagem/', disciplina_views.Listagem_disciplina.as_view(), name='DisciplinaListagem'),
    url(r'^disciplina/$'        , disciplina_views.Listagem_disciplina.as_view(), name='Disciplina')

    #url(r'^admin/', include(admin.site.urls)),
]
