from django.urls import path
from . import views

urlpatterns = [
    path('addPrestataire/', views.add_prestataire, name='addPrestataire'),
    path('listPrestataires/', views.get_all_prestataires, name='listPrestataires'),
]
