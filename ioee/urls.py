# urls.py
"""ioee URL Configuration

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
from django.urls import path, include
#from code_share.views import ssl_cert
from api import views as api

from django.contrib.auth import views as auth_views
from . import views


from django.contrib.sitemaps.views import sitemap
from .sitemaps import EachCodeViewSitemap, CodeHomePageViewSitemap

sitemaps = {
    'cods_collection': CodeHomePageViewSitemap,
    'each_codes': EachCodeViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # path('code/', include('code_share.urls')),
    
    path('images/', include('images.urls')),
    #path('community/', include('community.urls')),
    
    # for login and logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}),
    path('ioe_overflow/', include('ioe_overflow.urls')),
    path('pdf/', include('pdf_engine.urls')),
    path('pdf', include('pdf_engine.urls')),
    path('', include('code_share.urls')),

    path('community/', include('person.urls')),
]