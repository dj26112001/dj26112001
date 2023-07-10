"""ApartmentVisitorMgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from apartment.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('admin_home',admin_home,name='admin_home'),
    path('logout',Logout,name='logout'),
    path('manage_newvisitors',manage_newvisitors,name='manage_newvisitors'),
    path('visitor_form',visitor_form,name='visitor_form'),
    path('visitor_detail/<int:pid>',visitor_detail,name='visitor_detail'),
    path('changepassword',changepassword,name='changepassword'),
    path('search',search,name='search'),
    path('betweendate_report', betweendate_report, name='betweendate_report'),
    path('betweendate_reportdetails', betweendate_reportdetails, name='betweendate_reportdetails'),
]
