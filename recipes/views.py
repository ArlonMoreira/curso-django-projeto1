from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(requiest):
    return HttpResponse('<p>HOME</p>')

def contact(requiest):
    return HttpResponse('<p>CONTATO</p>')

def about(requiest):
    return HttpResponse('<p>SOBRE</p>')