from django.contrib import admin
from .models import Docteur  # Make sure to import the Docteur model

# Register the Docteur model with the admin site
admin.site.register(Docteur)

