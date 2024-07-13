from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    assunto = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Contato
        fields = ['nome', 'telefone', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control'}),
        }