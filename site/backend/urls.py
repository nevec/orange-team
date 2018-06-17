"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


import accounts
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.index, name='index'),
    path('map/', accounts.views.map, name='map'),
    path('test/', accounts.views.test, name='test'),
    path('login/', accounts.views.login, name ='login'),
    path('register/',accounts.views.register, name = 'register'),
] + staticfiles_urlpatterns()
