from django.contrib import admin
from .forms import descricaoForm
from .models import carausel, descricao

class descricaoAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'
    search_fields = 'title',
    form = descricaoForm

admin.site.register(carausel)
admin.site.register(descricao)

# Register your models here.
