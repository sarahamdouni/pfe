from django.urls import path
from . import views

urlpatterns = [
    path('addClinique/', views.add_clinique, name='addClinique'),
    path('listClinique/', views.get_all_cliniques, name='listClinique'),
]