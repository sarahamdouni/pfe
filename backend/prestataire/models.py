from django.db import models
from clinique.models import Clinique

class Prestataire(models.Model):
    prestataire_id = models.AutoField(primary_key=True)
    clinique = models.ForeignKey(Clinique, on_delete=models.CASCADE)  # Adjust Clinique model accordingly
    nom = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)
    adresse = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "prestataires"  # Match your existing table name

    def __str__(self):
        return self.nom

