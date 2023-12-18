from . import views
from django.urls import path


app_name = 'Gestion'
urlpatterns = [ 
    path('index/', views.index, name='index'), 
    #path('admin/', admin.site.urls),
    path('discussion/', views.discussion, name='discussion'),        
    path('profile/', views.profile, name='profile'),
    path('rendez_vous', views.rendez_vous, name='rendez_vous'),
    path('liste_clients', views.liste_utilisateurs, name='liste_clients'),
    path('liste_contacts', views.liste_contact, name='liste_contacts'),
    path('repondre_message/<int:contact_id>/', views.repondre_message, name='repondre_message'),
    path('supprimer_message/<int:contact_id>/', views.supprimer_message, name='supprimer_message'),
    path('candidatures', views.candidatures, name='candidatures'),
    path('ajout_client', views.Ajouter_Client, name='ajout_client'),
    path('modifier_client/<int:user_id>/', views.modifier_client, name='modifier_client'),
    path('supprimer_client/<int:user_id>/', views.supprimer_client, name='supprimer_client'),
    path('logout/', views.logout_user, name='logout'),
]