from django.shortcuts import render
from .models import Contato


# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'index.html', {
        'contatos': contatos
    })


def detail(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    return render(request, 'details.html', {
        'contato': contato
    })
