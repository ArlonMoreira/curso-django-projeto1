from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', status=200, context={
        'name': 'Arlon Moreira'
    })

def contact(request):
    return HttpResponse('<p>CONTATO</p>')

def about(request):
    return HttpResponse('<p>SOBRE</p>')