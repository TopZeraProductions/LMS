from django.db import models

class AlunoDAL(models.Model):

    nome    = models.CharField(max_length=100)
    cidade  = models.CharField('cidade', max_length=20, null=True)
    uf      = models.CharField('uf', max_length=2, null=True)
    cep     = models.CharField('cep', max_length=8, null=True)
    endereco= models.CharField('endereco', max_length=50, null=True)
    rg      = models.CharField('rg', max_length=20, null=True)
    criado_em = models.DateTimeField('criado em', auto_now_add=True )

    class Meta:
        ordering = ['criado_em']
        verbose_name = (u'nome')
        verbose_name_plural = (u'nomes')

    def get_absolute_url(self):
        return u'/aluno/listagem'

    def __unicode__(self):
        return self.nome