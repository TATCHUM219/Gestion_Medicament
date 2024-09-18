from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name='client'
urlpatterns = [
    path('Medicaments/', views.MedicamentList.as_view(), name='Medicament-list'),
    path('MedicamentSearch/', views.MedicamentSearch.as_view(), name='Medicament-search'),
    path('Medicaments/<int:pk>/', views.MedicamentDetail.as_view(), name='Medicament-detail'),
     path('Fabricants/', views.FabricantList.as_view(), name='Fabricant-list'),
    path('Commandes/', views.CommandeList.as_view()),
    path('Commandes/<int:pk>/', views.CommandeDetail.as_view()),
    path('Clients/', views.ClientList.as_view()),
    path('Clients/<int:pk>/', views.ClientDetail.as_view()),
    path('Expeditions/', views.ExpeditionList.as_view()),
    path('Expeditions/<int:pk>/', views.ExpeditionDetail.as_view()),
    path('Ligne_commandes/', views.Ligne_commandeList.as_view()),
    path('Ligne_commandes/<int:pk>/', views.Ligne_commandeDetail.as_view()),
    path('login/',csrf_exempt(views.login.as_view())),
    path('lastCommande/',csrf_exempt(views.LastCommande.as_view())),
    path('fabricantMedicaments/<int:id_f>/',csrf_exempt(views.FabricantMedicamens.as_view())),
    path("deleteCommande/<int:id_cmd>",csrf_exempt(views.DeleteCommande.as_view()))
     

]