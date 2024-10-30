import os
import django
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.contrib import auth, messages
from .models import Categoria, Receita  # Importação absoluta dos modelos
from .forms import ReceitaForm, SugestaoForm

def home(request):
    receitas = Receita.objects.all()

    return render(request, 'home.html', {'receitas': receitas})

def acesso(request):
    return render(request, 'acesso.html')

def adicionar_receita(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar')
    else:
        if request.method == 'POST':
            form = ReceitaForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,
                                """Receita adicionada com sucesso!
                                 Em breve o administrador irá verificar sua receita e adicioná-la ao site!
                                 Certifique-se de verificar seu email: O administrador te enviará notícias por lá!""")
                return redirect('adicionar_receita')
        else:
            form = ReceitaForm()
        return render(request, 'receitas/adicionar_receita.html', {'form': form})

def sugestao(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar')
    else:
        if request.method == "POST":
            form = SugestaoForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,
                                """Sugestão enviada com sucesso!
                                 Em breve o administrador irá verificar sua sugestão e tentar adicioná-la ao site!
                                 Certifique-se de verificar seu email: O administrador te enviará notícias por lá!""")
                return redirect('sugestao')
        else:
            form = SugestaoForm()
        return render(request, 'receitas/sugestao.html', {'form': form})

def paes(request):
    categoria = get_object_or_404(Categoria, nome='Pão')
    receitas = get_list_or_404(Receita, categoria=categoria)
    return render(request, "paes.html", {'receitas': receitas})

def bolos(request):
    categoria = get_object_or_404(Categoria, nome='Bolo')
    receitas = get_list_or_404(Receita, categoria=categoria)
    return render(request, "bolos.html", {'receitas': receitas})
def outras_sobremesas(request):
    categoria = get_object_or_404(Categoria, nome='Sobremesa')
    receitas = get_list_or_404(Receita, categoria=categoria)
    return render(request, "outras_sobremesas.html", {'receitas': receitas})


def outras_massas_e_salgados(request):
    categoria = get_object_or_404(Categoria, nome='Massas/salgados')
    receitas = get_list_or_404(Receita, categoria=categoria)
    return render(request, "outras_massas_e_salgados.html", {'receitas': receitas})

def buscar_receitas(request):
    query = request.GET.get('q')
    if query:
        receitas = Receita.objects.filter(nome__icontains=query)
    else:
        receitas = Receita.objects.all()
    return render(request, 'buscar_receitas.html', {'receitas': receitas})


def receitas_por_categoria(request):
    categoria_id = request.GET.get('categoria_id')
    termo_busca = request.GET.get('q')

    categorias = Categoria.objects.all()

    if categoria_id:
        categoria = get_object_or_404(Categoria, id=categoria_id)
        receitas = Receita.objects.filter(categoria=categoria)
    else:
        receitas = Receita.objects.all()

    if termo_busca:
        receitas = receitas.filter(nome__icontains=termo_busca)

    context = {
        'receitas': receitas,
        'termo_busca': termo_busca,
        'categorias': categorias,
    }
    return render(request, 'buscar_receitas.html', context)
def exibir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    receitas = Receita.objects.filter(categoria=categoria)
    return render(request, 'categoria.html', {'categoria': categoria, 'receitas': receitas})

def exibir_receita(request, num_receita):
    receita = get_object_or_404(Receita, id=num_receita)
    ingredientes = receita.ingredientes.split(',')
    modo_preparo = receita.modo_preparo.split('\n')
    modo_preparo_formatado = [passo.replace('\r\n', '<br>') for passo in modo_preparo]

    return render(request, 'receita_detail.html', {
        'receita': receita,
        'ingredientes': ingredientes,
        'modo_preparo': modo_preparo_formatado,
    })