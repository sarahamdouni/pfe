 
from django.urls import path
from . import views

urlpatterns = [
    path('addDocteur/', views.add_docteur, name='addDocteur'),
    path('listDocteurs/', views.get_all_docteurs, name='listDocteurs'),
]
