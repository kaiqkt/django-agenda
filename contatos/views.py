from django.shortcuts import render
from .models import Contato


# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'index.html', {
        'contatos': contatos
    })
