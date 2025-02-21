from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Clinique

@csrf_exempt  # Disable CSRF for testing (not recommended for production)
def add_clinique(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))  # Decode JSON request
            nom = data.get("nom")
            adresse = data.get("adresse")
            ville = data.get("ville")

            if not nom or not adresse:
                return JsonResponse({"error": "Nom and Adresse are required!"}, status=400)

            clinique = Clinique(nom=nom, adresse=adresse, ville=ville)
            clinique.save()

            return JsonResponse({"message": "Clinique added successfully!", "id": clinique.clinique_id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def get_all_cliniques(request):
    cliniques = Clinique.objects.all().values("clinique_id", "nom", "adresse", "ville")
    return JsonResponse(list(cliniques), safe=False)