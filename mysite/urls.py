"""mysite URL Configuration

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
from db import views as db_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', db_views.index, name = 'home'),
    path('register/', db_views.register, name = 'register'),
    path('log/', db_views.log, name = 'log'),
    path('logout/', db_views.logout, name = 'logout'),
    path('user/<str:name>', db_views.userpage, name = 'userpage'),
    path('tables/', db_views.tables, name = 'tables'),
    
    path('tables/diseasetypes', db_views.dt, name = 'dt'),
    path('tables/diseasetypes/<int:id>', db_views.dt_edit, name = 'dt_edit'),
    path('tables/diseasetypes/add', db_views.dt_add, name = 'dt_add'),
    
    path('tables/country', db_views.country, name = 'country'),
    path('tables/country/add', db_views.country_add, name = 'country_add'),
    path('tables/country/<int:id>', db_views.country_edit, name = 'country_edit'),
    
    path('tables/disease', db_views.disease, name = 'disease'),
    path('tables/disease/add', db_views.disease_add, name = 'disease_add'),
    path('tables/disease/<int:id>', db_views.disease_edit, name = 'disease_edit'),
    
    path('tables/discover', db_views.discover, name = 'discover'),
    path('tables/discover/<int:id>', db_views.discover_edit, name = 'discover_edit'),
    path('tables/discover/add', db_views.discover_add, name = 'discover_add'),
    
    path('tables/users', db_views.users, name = 'users'),
    path('tables/users/add', db_views.users_add, name = 'users_add'),
    path('tables/users/<int:id>', db_views.users_edit, name = 'users_edit'),
    
    path('tables/publicservant', db_views.ps, name = 'ps'),
    path('tables/publicservant/<int:id>', db_views.ps_edit, name = 'ps_edit'),
    path('tables/publicservant/add', db_views.ps_add, name = 'ps_add'),
    
    path('tables/doctor', db_views.doctor, name = 'doctor'),
    path('tables/doctor/<int:id>', db_views.doctor_edit, name = 'doctor_edit'),
    path('tables/doctor/add', db_views.doctor_add, name = 'doctor_add'),
    
    path('tables/specialize', db_views.specialize, name = 'specialize'),
    path('tables/specialize/<int:id>', db_views.specialize_edit, name = 'specialize_edit'),
    path('tables/specialize/add', db_views.specialize_add, name = 'specialize_add'),
    
    path('tables/record', db_views.record, name = 'record'),
    path('tables/record/<int:id>', db_views.record_edit, name = 'record_edit'),
    path('tables/record/add', db_views.record_add, name = 'record_add'),
]
