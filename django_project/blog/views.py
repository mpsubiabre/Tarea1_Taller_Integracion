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
    lista_bb = []
    lista_bcs = []
    for i in response:
        print(i['season'])
        if i["series"]=="Breaking Bad":
            if i['season'] in lista_bb:
                print(i['season'])
                print(lista_bb)
                pass
            else:
                lista_bb.append(i['season'])
        if i["series"]=="Better Call Saul":
            if i['season'] in lista_bcs:
                pass
            else:
                lista_bcs.append(i['season'])
    #todo['bb'] = lista_bb
    #todo['bcs'] = lista_bcs
    #print('holi', todo)
    print(lista_bb)
    print(lista_bcs)
    lista_bb.sort()
    lista_bcs.sort()        
    return render(request, 'blog/home.html', {'bb':lista_bb, 'bcs':lista_bcs})


def about(request):
    return render(request, 'blog/about.html', {'title': 'abput'})

def episodiosbb(request, temporada):
    print("entro a episodiosbb")
    print(request)
    print(temporada)
    episodios = []
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    for i in response:
        if i['season'] == temporada:
            episodios.append(i['title'])

    print(episodios)
    return render(request, 'blog/episodios.html', {'title': 'episodios', 'response': episodios, 'temporada': temporada})

def episodiosbcs(request, temporada):
    print("entro a episodiosbcs")
    print(request)
    print(temporada)
    episodios = []
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes').json()
    for i in response:
        if i['series'] == 'Better Call Saul' and i['season'] == str(temporada):
            episodios.append(i['title'])

    #print(response)
    print(episodios)
    return render(request, 'blog/episodios.html', {'title': 'episodios', 'response': episodios, 'temporada':temporada})

def detalle(request, episodio):
    print("entro a detallebcs")
    print(episodio)
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes').json()
    for i in response:
        if i['title'] == episodio:
            info = i
            print(i)
    info_episodio = []
    personajes = []
    for key,values in info.items():
        if key == 'characters':        
            personajes = values
        else:
            info_episodio.append(str(key) +" : "+ str(values))
    return render(request, 'blog/detalle.html', {'title': 'detalle', 'response': info_episodio, 'episodio':episodio, 'personajes': personajes})

def personaje(request, nombre):
    print("entro a personajes")
    print(nombre)
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+ nombre.replace(" ", "+")).json()
    citas = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/quote?author='+ nombre.replace(" ", "+")).json()
    print(response)      

    for i in response:
        for key,values in i.items():
            print(key, values)
            if key == 'status':
                status = values
            if key == 'nickname':
                nickname = values
            if key == 'appearance':
                appearance = values
            if key == 'portrayed':
                portrayed = values    
            if key == 'img':
                img = values            
            if key == 'category':
                category = values
            if key == 'occupation':
                occupation = values
            if key == 'better_call_saul_appearance':
                if values != []:
                    better_call_saul_appearance = values
                else:
                    better_call_saul_appearance = []
                    pass

    return render(request, 'blog/personaje.html', {'title': 'detalle', 'personaje': nombre, 'status': status, 'nickname':nickname, 'apparence':appearance,'portrayed':portrayed, 'category':category, 'better_call_saul_appearance':better_call_saul_appearance, 'occupation' : occupation, 'img':img, 'citas':citas})


def buscar(request):
    todos = []
    srch = request.GET['buscando']
    print(srch)
    i = 0
    if requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+srch+'&offset='+str(i)).status_code == 200:
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+srch+'&offset='+str(i)).json()
        while response:
            for j in response:
                todos.append(j)
            i+=10 #paginacion
            response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+srch+'&offset='+str(i)).json()
            if requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+srch+'&offset='+str(i)).status_code != 200:
                break
    print('REVISAR ACA')
    print(todos)
    print(request)
    return render(request, 'blog/busqueda.html', {'todos': todos})