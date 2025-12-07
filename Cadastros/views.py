from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dono



# Create your views here.

def Cadastros(request):
    listadono = Dono.objects.all().values()
    template = loader.get_template('cadastros_criados.html')
    context = {
        'listadono' : listadono,
    }


