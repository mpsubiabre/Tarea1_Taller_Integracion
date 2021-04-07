from django.shortcuts import render
from django.http import HttpResponse
import requests

posts = [
    {
        'author': 'pachi',
        'title': 'soy el titulo',
        'content': 'holi'
    },
    {
        'author': 'flo',
        'title': 'soy el titulo2',
        'content': 'holi2'
    }
]

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Homee</h1>')
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes').json()
    lista = []
    for i in response:
        if i['episode'] in lista:
            pass
        else:
            lista.append(i['episode'])
    return render(request, 'blog/home.html', {'response': lista})

def home1(request):
   # return HttpResponse('<h1>Homee</h1>')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'abput'})
