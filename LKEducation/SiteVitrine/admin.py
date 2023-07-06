from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(User)
admin.site.register(evenement)
admin.site.register(galerie)
admin.site.register(article)
admin.site.register(document)
admin.site.register(modele_rdv)
admin.site.register(rendezvous)
admin.site.register(notification)
admin.site.register(historique_paie)