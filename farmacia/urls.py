"""
URL configuration for farmacia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from nodos.sitemaps import NodosSiteMaps, DestinosSitemaps
from hojaderuta.sitemaps import HojaDeRutaSiteMaps

sitemaps = {

    'nodos': NodosSiteMaps,

    'destinos': DestinosSitemaps,

    'hojaderuta': HojaDeRutaSiteMaps,
}


urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', include('hojaderuta.urls')),

    path('nodos/', include('nodos.urls')),

    path('perfil/', include('perfiles.urls')),
    
    path('accounts/', include('registration.backends.default.urls')),

    path('captcha/', include('captcha.urls')),

    path('api/', include('api.urls')),

    path('FAQ/', include('FAQ.urls')),   

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name= 'django.contrib.sitemaps.views.sitemap' ),

    path('ckeditor/', include('ckeditor_uploader.urls')),           

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


if settings.DEBUG:
    
    import debug_toolbar

    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
