from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('acesso/', views.acesso, name="acesso"),
    path('adicionar/', views.adicionar_receita, name='adicionar_receita'),
    path('sugestao/', views.sugestao, name="sugestao"),
    path('paes/', views.paes, name='paes'),
    path('bolos/', views.bolos, name='bolos'),
    path('outras_sobremesas/', views.outras_sobremesas, name='outras_sobremesas'),
    path('outras_massas_e_salgados/', views.outras_massas_e_salgados, name='outras_massas_e_salgados'),
    path('categoria/<int:categoria_id>/', views.receitas_por_categoria, name='receitas_por_categoria'),
    path('buscar/', views.buscar_receitas, name='buscar_receitas'),
    path('receita<int:num_receita>/', views.exibir_receita, name='exibir_receita'),

]
