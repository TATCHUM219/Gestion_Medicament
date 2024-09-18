from django.db import models

class Annonce(models.Model):
     titre=models.CharField(max_length=100)
     description=models.TextField()
     image=models.FileField(upload_to='annonce',null=True,blank=True)
     
     
