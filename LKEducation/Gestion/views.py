from django.shortcuts import render

# Create your views here.

# Index view
def index(request):
    context = {}
    return render(request, "index.html", context)

# Vue pour les notifications
def discussion(request):
    context = {}
    return render(request, "discussion.html", context)

# Vue pour le profile 
def profile(request):
    context = {}
    return render(request, "profile.html", context)

# Vue pour l'ensemble des rendez-vous
def rendez_vous(request):
    context = {}
    return render(request, "rendez_vous.html", context)