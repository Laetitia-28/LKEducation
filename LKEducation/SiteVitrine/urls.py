from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('', views.index, name='index'), 
    #path('admin/', admin.site.urls),
    path('evenement/', views.event, name='event'),        
    path('appointment/', views.appointment, name='appointment'),
    path('galerie/', views.galerie, name='galerie'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('services/', views.services, name='services'),
    # path('partenaires/', views.partenaires, name='partenaires'),
    path('partenaires_en_Allemagne/', views.partenaires_allemagne, name='partenaires_allemagne'),
    path('partenaires_en_Espagne/', views.partenaires_espagne, name='partenaires_espagne'),
    path('partenaires_en_Lituanie/', views.partenaires_lituanie, name='partenaires_lituanie'),
    path('partenaires_en_France/', views.partenaires_france, name='partenaires_france'),

    # URL pour la réinitialisation du mot de passe
    path('reset_password/', views.password_reset_form, name='password_reset_form'),
    path('reset_password_sent/', views.password_reset_done, name='password_reset_Done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset_password_complete/', views.password_reset_complete, name='password_reset_complete'),
]
