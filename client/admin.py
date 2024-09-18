from django.contrib import admin
from .models import *

@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    list_display= ('id','fabricant','libelle','prix','image','domaine_application','arte','qte','marque')

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display= ('id','date_heure','client','est_livre')

@admin.register(Fabricant)
class FabricantAdmin(admin.ModelAdmin):
    list_display= ('id','nom','logo')

@admin.register(Ligne_commande)
class Ligne_commandeAdmin(admin.ModelAdmin):
    list_display= ('qte_cmd','commande','medicament')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display= ('id','nom','email','password','contact',)

@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display= ('contact','adr','ville','commande')
