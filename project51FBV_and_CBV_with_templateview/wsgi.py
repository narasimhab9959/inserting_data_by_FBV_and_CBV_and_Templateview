"""
WSGI config for project51FBV_and_CBV_with_templateview project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project51FBV_and_CBV_with_templateview.settings')

application = get_wsgi_application()
