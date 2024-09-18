from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Medicament
from django.db.models import Q
from .serializer import *
from django.views import View
import json
from django.db.models import Prefetch
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib import messages



class MedicamentList(generics.ListCreateAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer

class FabricantList(generics.ListCreateAPIView):
    queryset = Fabricant.objects.all()
    serializer_class = FabricantSerializer


class MedicamentSearch(View):
    def get(self,request):
      
        medicaments=list(Medicament.objects.values().filter(Q(libelle__icontains=request.GET['term'])))
        return JsonResponse({'medicaments':medicaments})
            
    

class MedicamentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicament.objects.all()
    serializer_class = MedicamentSerializer
    
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class CommandeList(generics.ListCreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

class CommandeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

class Ligne_commandeList(generics.ListCreateAPIView):
    queryset = Ligne_commande.objects.all()
    serializer_class = Ligne_commandeSerializer

class Ligne_commandeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ligne_commande.objects.all()
    serializer_class = Ligne_commandeSerializer

class ExpeditionList(generics.ListCreateAPIView):
    queryset = Expedition.objects.all()
    serializer_class = ExpeditionSerializer

class ExpeditionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expedition.objects.all()
    serializer_class = ExpeditionSerializer
class LastCommande(View):
    def get(self,request):
        return JsonResponse({'lastcmd':Commande.objects.latest('id').pk})
    

class login(View):
    def post(self,request):
        data=json.loads(request.body)
        email=data['email']
        password=data['password']
        if Client.objects.filter(email=email).exists() :
            clt=Client.objects.get(email=email)
            if password==clt.password:
                client=clt.pk
                return JsonResponse({'success':client})
            else:
                return JsonResponse({'error':'Identifiants ou mots de passe incorrect'})
        else:         
            return JsonResponse({'error':'Identifiants ou mots de passe incorrect'})
        
class FabricantMedicamens(View):
    def get(self,request,id_f):
        med=list(Medicament.objects.filter(marque_id=id_f).values())
        fab=list(Fabricant.objects.filter(id=id_f).values())
        return JsonResponse({'medicaments':med,'fabricant':fab})
@login_required  
def Dashboard(request):
    nbcmd = Commande.objects.filter().count()
    cmdnexp = Commande.objects.filter(est_livre=False).count()
    prod_rupture=float(Medicament.objects.filter(qte=0).count() / Medicament.objects.count())*100
    ca=0.0
    for l in Ligne_commande.objects.all():
        ca+=float(l.medicament.prix * l.qte_cmd)
    context={
        "nbcmd":nbcmd,
        "cmdnexp":cmdnexp,
        "prod_rupture":prod_rupture,
        "ca": ca
    }
    return render(request,'dashboard.html',context)    
@login_required 
def liste_cmd(request):
    if request.method=='PUT':
        
        exped=request.PUT.get('exped')
        id_cmd=request.PUT.get('id_cmd')
        cmd=Commande.objects.get(id=id_cmd)
        if exped=='true':
            cmd.est_livre=True
           
        else:
            cmd.est_livre=False
        cmd.save()
        messages.info(request,'La commande '+str(id_cmd)+' a été modifié avec success')
    cmd=Commande.objects.prefetch_related(Prefetch('ligne_commande',queryset=Ligne_commande.objects.all())).all()
    return render(request,'liste_commande.html',{'commandes':cmd})

class DeleteCommande(View):
    def delete(self,request,id_cmd):
        
        cmd=Commande.objects.get(id=id_cmd)
        cmd.delete()
        return JsonResponse({'success':'Deleted Successfully'})

from django.utils.translation import gettext as _
import json

def get_translations(request, lang_code):
    try:
        with open(f'locales/{lang_code}/translation.json', 'r') as file:
            translations = json.load(file)
        return JsonResponse(translations)
    except FileNotFoundError:
        return JsonResponse({'error': 'Translations not found'}, status=404)
        
    