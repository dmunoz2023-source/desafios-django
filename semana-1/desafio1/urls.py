from django.contrib import admin
from django.urls import path
from desafio.views import hola_mundo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hola_mundo),  # Página principal
]
