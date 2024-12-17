"""
WSGI config for Content project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add your project to the system path
sys.path.append('/Users/saipraneethkotyada/Desktop/Project/Content')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Content.settings')

application = get_wsgi_application()
