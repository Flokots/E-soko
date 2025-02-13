from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
  
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
    
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)