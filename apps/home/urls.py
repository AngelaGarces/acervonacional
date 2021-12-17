from django.urls import path
from .views import HomeView, SobreView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', HomeView.as_view(), name='home'), 
    path('sobre/', SobreView.as_view(), name='sobre'),
]
