from django.shortcuts import redirect, render
from django.contrib import auth

from django.shortcuts import redirect, render
from django.contrib import auth
from django.urls import reverse

def home(request):
    if not request.user.is_authenticated:
        # Se o usuário estiver autenticado, renderize a página inicial de receitas
        return redirect('/usuarios/logar')
    else:
        # Se o usuário não estiver autenticado e não estiver na página de login,
        # redirecione para a página de login
        return render(request, 'home.html')
    
def acesso(request):
    if not request.user.is_authenticated:
        # Se o usuário estiver autenticado, renderize a página inicial de receitas
        return redirect('/usuarios/logar')
    else:
        # Se o usuário não estiver autenticado e não estiver na página de login,
        # redirecione para a página de login
        return render(request, 'acesso.html')
    
    
def receita1(request):
    return render(request, 'receitas_templates/receita1.html')

def receita2(request):
    return render(request, 'receitas_templates/receita2.html')

def receita3(request):
    return render(request, 'receitas_templates/receita3.html')

def receita4(request):
    return render(request, 'receitas_templates/receita4.html')

def receita5(request):
    return render(request, 'receitas_templates/receita5.html')

def receita6(request):
    return render(request, 'receitas_templates/receita6.html')

def receita7(request):
    return render(request, 'receitas_templates/receita7.html')

def receita8(request):
    return render(request, 'receitas_templates/receita8.html')

def receita9(request):
    return render(request, 'receitas_templates/receita9.html')

def receita10(request):
    return render(request, 'receitas_templates/receita10.html')

def receita11(request):
    return render(request, 'receitas_templates/receita11.html')

def receita12(request):
    return render(request, 'receitas_templates/receita12.html')

def receita13(request):
    return render(request, 'receitas_templates/receita13.html')

def receita14(request):
    return render(request, 'receitas_templates/receita14.html')

def receita15(request):
    return render(request, 'receitas_templates/receita15.html')

def receita16(request):
    return render(request, 'receitas_templates/receita16.html')

def receita17(request):
    return render(request, 'receitas_templates/receita17.html')

def receita18(request):
    return render(request, 'receitas_templates/receita18.html')

def receita19(request):
    return render(request, 'receitas_templates/receita19.html')

def receita20(request):
    return render(request, 'receitas_templates/receita20.html')

def receita21(request):
    return render(request, 'receitas_templates/receita21.html')

def receita22(request):
    return render(request, 'receitas_templates/receita22.html')
