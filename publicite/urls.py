from django.urls import path

from . import views

app_name='publicite'
urlpatterns = [
    path('Annonces/', views.AnnonceList.as_view(), name='Annonce-list'),
    path('testEmail/', views.SendEmail, name='TestEmail'),
   
]