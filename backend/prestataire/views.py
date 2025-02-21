from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Prestataire, Clinique  # Import models

@csrf_exempt  # Disable CSRF for testing (not recommended for production)
def add_prestataire(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))  # Decode JSON request
            nom = data.get("nom")
            specialite = data.get("specialite")
            adresse = data.get("adresse")
            clinique_id = data.get("clinique_id")

            if not nom or not specialite or not adresse:
                return JsonResponse({"error": "Nom, Spécialité, and Adresse are required!"}, status=400)

            # Validate clinique_id (it should exist in Clinique model)
            try:
                clinique = Clinique.objects.get(clinique_id=clinique_id)  # Use 'clinique_id' as per your model
            except Clinique.DoesNotExist:
                return JsonResponse({"error": "Clinique not found!"}, status=404)

            prestataire = Prestataire(
                nom=nom,
                specialite=specialite,
                adresse=adresse,
                clinique=clinique
            )
            prestataire.save()

            return JsonResponse({"message": "Prestataire added successfully!", "id": prestataire.prestataire_id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)


def get_all_prestataires(request):
    prestataires = Prestataire.objects.all().values(
        "prestataire_id", "nom", "specialite", "adresse", "clinique__nom"
    )  # Ensure 'nom' exists in Clinique model
    return JsonResponse(list(prestataires), safe=False)
