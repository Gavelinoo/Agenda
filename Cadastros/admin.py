from django.contrib import admin
from .models import Dono, Pet

# Register your models here.

admin.site.site_header = "Sistema de Administracao Pet Shop"
admin.site.site_title = "Cadastros de Pets e Donos"
admin.site.register(Dono)
admin.site.register(Pet)


