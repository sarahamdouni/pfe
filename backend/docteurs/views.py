from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Docteur, Clinique  # Import models

@csrf_exempt  # Disable CSRF for testing (not recommended for production)
def add_docteur(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))  # Decode JSON request
            nom_complet = data.get("nom_complet")
            specialite = data.get("specialite")
            telephone = data.get("telephone")
            adresse = data.get("adresse")
            clinique_id = data.get("clinique_id")

            if not nom_complet or not specialite or not telephone or not adresse:
                return JsonResponse({"error": "Nom complet, Specialité, Téléphone, and Adresse are required!"}, status=400)

            # Validate clinique_id (it should exist in Clinique model)
            try:
                clinique = Clinique.objects.get(clinique_id=clinique_id)  # Use 'clinique_id' as per your model
            except Clinique.DoesNotExist:
                return JsonResponse({"error": "Clinique not found!"}, status=404)

            docteur = Docteur(  # Fixed variable name
                nom_complet=nom_complet,
                specialite=specialite,
                telephone=telephone,
                adresse=adresse,
                clinique=clinique
            )
            docteur.save()

            return JsonResponse({"message": "Docteur added successfully!", "id": docteur.id}, status=201)  # Keep 'id' (Django's default PK)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)


def get_all_docteurs(request):
    docteurs = Docteur.objects.all().values(
        "id", "nom_complet", "specialite", "telephone", "adresse", "clinique__nom"
    )  # Ensure 'nom' exists in Clinique model
    return JsonResponse(list(docteurs), safe=False)
