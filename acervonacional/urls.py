
from django.contrib import admin
from django.urls import path, include

from apps.livros import urls as livros_urls
from apps.home import urls as home_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar/', include(livros_urls)),
    path('', include(home_urls)),
]
