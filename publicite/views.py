from .models import Annonce
from .serializers import *
from rest_framework import generics
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail





class AnnonceList(generics.ListCreateAPIView):
    queryset = Annonce.objects.all()
    serializer_class = AnnonceSerializer

def SendEmail(request):
    
    if request.method=='post':
        send_mail(
        'Test Confirmation Commande',
        'Votre commande a été  prise en compte avec succès vous serez livré bientôt',
        'settings.EMAIL_HOST_USER',
        ['settings.EMAIL_HOST_USER'],
        fail_silently=False
    )
    
    
    return redirect('/admin/')

