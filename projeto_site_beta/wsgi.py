"""
WSGI config for projeto_site_beta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Adiciona o diretório que contém o projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Define as configurações do Django para o projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_site_beta.settings')

# Obtém a aplicação WSGI padrão do Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()