"""
ASGI config for first project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from django.core.asgi import get_asgi_application
from app1.consumer import TestConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first.settings')
application = get_asgi_application()
ws_pattern=[
    path('ws/test/',TestConsumer.as_asgi())
]
application = ProtocolTypeRouter({
    'websocket':URLRouter(ws_pattern)
    })
