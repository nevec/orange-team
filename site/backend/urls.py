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
from django.contrib.auth import logout

import accounts
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.index, name='index'),
    path('map/', accounts.views.map, name='map'),
    path('test/', accounts.views.test, name='test'),

    path('locations/', accounts.views.getPlaces, name='locations'),

    path('login/', accounts.views.loginp, name ='loginp'),
    path('register/',accounts.views.register, name = 'register'),

    path('login_data/',accounts.views.get_log_pass, name ='get_log_pass'),
    path('register_data/',accounts.views.get_reg, name ='get_reg'),
    path('test2/', accounts.views.test2, name='test2'),
    path('success/', accounts.views.success, name='success'),
    path('logout/', accounts.views.logout),
    path('test1_answ/', accounts.views.test1_answ),
    path('test2_answ/', accounts.views.test2_answ),
] + staticfiles_urlpatterns()


