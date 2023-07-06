from . import views
from django.urls import path

urlpatterns = [ 
    path('', views.index, name='index'), 
    #path('admin/', admin.site.urls),
    path('evenement/', views.event, name='event'),        
    path('appointment/', views.appointment, name='appointment'),
    path('galerie/', views.galerie, name='galerie'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout')
]
