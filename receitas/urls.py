from django.urls import path
from . import views
from receitas.views import pagina_inicial

urlpatterns = [
    path('home/', views.home, name="home"),
    path('acesso/', views.acesso, name="acesso"),
    path('adicionar/', views.adicionar_receita, name='adicionar_receita'),
    path('sugestao/', views.sugestao, name="sugestao"),
    path('receita1/', views.receita1, name='receita1'),
    path('receita2/', views.receita2, name='receita2'),
    path('receita3/', views.receita3, name='receita3'),
    path('receita4/', views.receita4, name='receita4'),
    path('receita5/', views.receita5, name='receita5'),
    path('receita6/', views.receita6, name='receita6'),
    path('receita7/', views.receita7, name='receita7'),
    path('receita8/', views.receita8, name='receita8'),
    path('receita9/', views.receita9, name='receita9'),
    path('receita10/', views.receita10, name='receita10'),
    path('receita11/', views.receita11, name='receita11'),
    path('receita12/', views.receita12, name='receita12'),
    path('receita13/', views.receita13, name='receita13'),
    path('receita14/', views.receita14, name='receita14'),
    path('receita15/', views.receita15, name='receita15'),
    path('receita16/', views.receita16, name='receita16'),
    path('receita17/', views.receita17, name='receita17'),
    path('receita18/', views.receita18, name='receita18'),
    path('receita19/', views.receita19, name='receita19'),
    path('receita20/', views.receita20, name='receita20'),
    path('receita21/', views.receita21, name='receita21'),
    path('receita22/', views.receita22, name='receita22'),
    path('receita23/', views.receita23, name='receita23'),
    path('', pagina_inicial, name='pagina_inicial'),
]
