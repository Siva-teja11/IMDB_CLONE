"""
URL configuration for imdb_clone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from movies.views import index,ninestar,add_movie
from accounts.views import register,user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('ninestar/',ninestar,name="ninestar"),
    path('add/', add_movie, name='add_movie'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
]
