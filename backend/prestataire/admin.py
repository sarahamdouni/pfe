from django.contrib import admin
from .models import Prestataire  # Make sure to import the Docteur model

# Register the Docteur model with the admin site
admin.site.register(Prestataire)

# Register your models here.
