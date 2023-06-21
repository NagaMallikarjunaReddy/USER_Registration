"""login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings  #first you need to import settigs
from django.conf.urls.static import static
#if you want to connect the media files you need to import static method

from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mail/',mail,name='mail'),
    path('home/',home,name='home'),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path('display_profile/',display_profile,name='display_profile'),
    path('change_password/',change_password,name='change_password'),
    path('forget_password/',forget_password,name='forget_password'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
