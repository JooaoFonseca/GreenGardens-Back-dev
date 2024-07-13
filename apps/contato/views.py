from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContatoForm

def contato(request):
    if request.method == 'GET':
        form = ContatoForm()
        return render(request, 'index.html', locals())
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            contato = form.save()
            send_mail(
                nome,
                telefone,
                email,
                mensagem,
                ['sfojoao.matheus04@gmail.com'])
            
            form = ContatoForm()
            messages.success(request, 'Cadastro realizado com sucesso')
        return render(request, 'index.html', locals())
    