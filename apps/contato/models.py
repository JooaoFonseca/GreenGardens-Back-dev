from django.db import models

class contato(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    telefone = models.IntegerField(verbose_name='Telefone', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=200)
    mensagem = models.TextField(verbose_name='Mensagem', max_length=255)

    class Meta:
        verbose_name = 'Contato'
        db_table = 'contato'
    
    def __str__(self):
        return self.nome