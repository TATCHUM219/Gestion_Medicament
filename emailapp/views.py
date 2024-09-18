from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse

from datetime import datetime
from client.models import Commande,Ligne_commande
from .utils import send_email_with_html_body
import json
# Create your views here.



class create_view(View):
    """ This view help to create and account for testing sending mails."""
    
    def post(self,request):
        data=json.loads(request.body)
        id_cmd=data['id_cmd']
       
        cmd=Commande.objects.get(id=id_cmd)
        nom=cmd.client.nom
        email=cmd.client.email
        lignes=Ligne_commande.objects.filter(commande=cmd)
        subjet = "Test Email"
        template = 'email.html'
        tot=0
        for ligne in lignes:
            tot+=(ligne.qte_cmd * ligne.medicament.prix)
        context = {
            'date': datetime.today().date,
            'nom': nom,
            'lignes':lignes,
            'tot':tot
        }
        print(lignes)
        receivers = [email]
        

        send_email_with_html_body(subjet=subjet,receivers=receivers, template=template,context=context)
        return JsonResponse({'success':'Email envoye'})
        
def Email(request):
    return render(request,'email.html')
        