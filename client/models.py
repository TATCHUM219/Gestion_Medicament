from django.db import models
from django.utils import timezone

class Fabricant(models.Model):
    nom=models.CharField(max_length=50)
    logo=models.ImageField(upload_to='fabricant',blank=False)
    def __str__(self):
        return self.nom

class Medicament(models.Model):
    
    libelle=models.CharField(max_length=50)
    prix=models.FloatField()
    reduction=models.FloatField(default=0.0)
    image=models.ImageField(upload_to='medicament',null=False,blank=False)
    domaine_application=models.TextField(null=True,blank=True)
    arte=models.CharField(max_length=50,null=True,blank=True)
    marque=models.ForeignKey(to=Fabricant,on_delete=models.DO_NOTHING,null=True)
    qte=models.IntegerField(default=1)
    fabricant=models.CharField(max_length=50,null=True,blank=True)
   
    def __str__(self):
        return self.libelle
    
    


class Client(models.Model):
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=200)
    contact=models.CharField(max_length=50)
    nom=models.CharField(max_length=50,default='nom')
    def __str__(self):
        return self.nom

class Commande(models.Model):
    
    date_heure=models.DateTimeField(default=timezone.now())
    client=models.ForeignKey(to=Client,on_delete=models.DO_NOTHING)
    est_livre=models.BooleanField(default=False)
    
class Expedition(models.Model):
    contact = models.CharField(max_length=20,default='contact')
    adr=models.CharField(max_length=100)
    ville=models.CharField(max_length=50)
    commande=models.OneToOneField(to=Commande,on_delete=models.CASCADE,related_name='expedition')
    
class Ligne_commande(models.Model):
    commande=models.ForeignKey(to=Commande,on_delete=models.CASCADE,related_name='ligne_commande')
    medicament=models.ForeignKey(to=Medicament,on_delete=models.DO_NOTHING)
    qte_cmd=models.IntegerField()


