"""onlineshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('editpro/<int:id>',views.editpro,name='editpro'),
    path('deletepro',views.deletepro,name='deletepro'),
    path('singlepro',views.singlepro,name='singlepro'),
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('property',views.property,name='property'),
    path('add',views.add,name='add'),
    path('about',views.about,name='about'),
	path('',views.home,name="index"),
	path('profile',views.profile,name="profile"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('admin/', admin.site.urls)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
