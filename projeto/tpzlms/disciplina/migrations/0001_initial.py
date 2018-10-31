# Generated by Django 2.1.2 on 2018-10-31 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaDAL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('carga_horaria', models.CharField(max_length=3, null=True, verbose_name='carga_horaria')),
                ('curso', models.CharField(max_length=255, null=True, verbose_name='curso')),
                ('semestre', models.CharField(max_length=8, null=True, verbose_name='cep')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name': 'nome',
                'verbose_name_plural': 'nomes',
                'ordering': ['criado_em'],
            },
        ),
    ]