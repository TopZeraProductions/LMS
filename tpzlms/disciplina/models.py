from django.db import models

class DisciplinaDAL(models.Model):

    nome       = models.CharField(max_length=100)
    carga_horaria  = models.CharField('carga_horaria', max_length=3, null=True)
    curso      = models.CharField('curso', max_length=255, null=True)
    semestre   = models.CharField('cep', max_length=8, null=True)
    criado_em = models.DateTimeField('criado em', auto_now_add=True )


    class Meta:
        ordering = ['criado_em']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')

    def get_absolute_url(self):
        return u'/disciplina/listagem/'

    def __unicode__(self):
        return self.nome
