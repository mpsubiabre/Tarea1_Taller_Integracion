from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
    path('episodiosbb/<temporada>', views.episodiosbb,name='episodiosbb'),    
    path('episodiosbcs/<temporada>', views.episodiosbcs,name='episodiosbcs'),

    path('episodiosbcs/detalle/<episodio>', views.detalle,name='detalle'),
    path('episodiosbb/detalle/<episodio>', views.detalle,name='detalle'),

    path('episodiosbb/detalle/personaje/<nombre>', views.personaje,name='personaje'),
    path('episodiosbcs/detalle/personaje/<nombre>', views.personaje,name='personaje'),

]
