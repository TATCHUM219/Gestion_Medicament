from rest_framework import serializers
from .models import *

class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = '__all__'
class FabricantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricant
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = '__all__'
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'
class Ligne_commandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ligne_commande
        fields = '__all__'
