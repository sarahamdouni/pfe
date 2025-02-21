from django.db import models

class Clinique(models.Model):
    clinique_id = models.AutoField(primary_key=True)  # or use 'id' if it's auto-increment
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    ville = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'cliniques'  # Explicitly set the table name to 'cliniques'

    def __str__(self):
        return self.nom 
