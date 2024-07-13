from django.shortcuts import render
from .models import carausel

def index(request):

    obj = carausel.objects.all()
    context = {
        'obj':obj
    }

    return render(request, 'index.html', context)
