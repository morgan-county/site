import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "morgan.settings.prod")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

