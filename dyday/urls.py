"""dyday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import  settings
from django.conf.urls.static import static
from compte.views import WelcomeView, InscriptionView, HomeView, connection, deconnection


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('inscription/', InscriptionView.as_view(), name='signup'),
    path('', HomeView.as_view(), name='home'),
    path('membre/', include('compte.urls', namespace='compte')),
    path('membre/', include('blog.urls', namespace='blog')),
    path('logout/', deconnection, name='logout'),
    path('login/', connection, name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
