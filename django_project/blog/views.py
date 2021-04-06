from django.shortcuts import render
from django.http import HttpResponse

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
   # return HttpResponse('<h1>Homee</h1>')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'abput'})
