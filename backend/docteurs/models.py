from django.db import models
from clinique.models import Clinique  # Import Clinique model from clinique app

class Docteur(models.Model):
    docteur_id = models.AutoField(primary_key=True)
    nom_complet = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=255)
    clinique = models.ForeignKey(Clinique, on_delete=models.CASCADE)
    class Meta:
        db_table = 'docteur'

    def __str__(self):
        return self.nom_complet
    


