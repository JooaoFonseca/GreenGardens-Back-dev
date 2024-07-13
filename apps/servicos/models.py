from django.db import models
from django.utils import formats

class carausel(models.Model):
    imagem = models.ImageField('Foto de Exibição', blank=True, null=True, upload_to='core/static/img/slider')

class descricao(models.Model):
    logo = models.ImageField('Imagem de Exibição', blank=True, null=True, upload_to='core/static/img/home/logo-Text.svg')
    logo2 = models.ImageField('Logo', blank=True, null=True, upload_to='core/static/img/geral/logo.svg')
    narrativa = models.TextField('Narrativa', blank=False, null=False)
    logo3 = models.ImageField('Imagem de Exibição', blank=True, null=True, upload_to='core/static/img/geral/deco-verdeClaro.svg')

    class Meta:
        verbose_name = "descrição"
        verbose_name_plural = "descrições"
        db_table = 'descricao'

class nossos_servicos(models.Model):
    titulo = models.CharField(verbose_name='Titulação', max_length=100)
    imagem = models.ImageField('Imagem de Exibição', blank=True, null=True, upload_to='img/servicos')
    titulo2 = models.CharField(verbose_name='Titulo', max_length=100)