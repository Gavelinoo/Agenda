from django.contrib.auth.urls import urlpatterns
from django.urls import path
from Cadastros import views

urlpatterns = [
    path('Cadastros/', views.Cadastros, name='Cadastros'),
]
