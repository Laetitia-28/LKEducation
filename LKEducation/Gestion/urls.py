from . import views
from django.urls import path


app_name = 'Gestion'
urlpatterns = [ 
    path('index/', views.index, name='index'), 
    #path('admin/', admin.site.urls),
    path('discussion/', views.discussion, name='discussion'),        
    path('profile/', views.profile, name='profile'),
    path('rendez_vous', views.rendez_vous, name='rendez_vous')
]