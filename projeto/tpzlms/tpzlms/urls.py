from cadastroaluno import views
from django.contrib import admin
from django.conf.urls import url

admin.autodiscover()
urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^aluno/cadastro/$', views.Criar.as_view(), name='cadastro'),

    url(r'^aluno/lista/$', views.Lista.as_view(), name='lista'),

    #url(r'^admin/', include(admin.site.urls)),
]