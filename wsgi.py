import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nome_do_projeto.settings')

application = get_wsgi_application()
