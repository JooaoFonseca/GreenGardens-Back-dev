from django.contrib import admin
from .models import contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'assunto', 'nome')
    list_display_links = ('id', 'nome')
    list_filter = ('nome', 'assunto')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(contato, ContatoAdmin)