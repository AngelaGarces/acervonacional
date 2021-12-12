
from django.contrib import admin
from django.urls import path, include

from apps.livros import urls as livros_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/', include(livros_urls)),
]
