from django.contrib import admin
from .models import *

@admin.register(Annonce)
class AnnonceAdmin(admin.ModelAdmin):
    list_display= ('titre','description','image')

