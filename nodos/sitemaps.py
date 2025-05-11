from django.contrib import sitemaps
from django.urls import reverse

class NodosSiteMaps(sitemaps.Sitemap):

    priority = 0.8

    changefreq = 'daily'

    def items(self):
        
        return ['ver_nodos']
    
    def location(self, item):
        
        return reverse(item)
    
class DestinosSitemaps(sitemaps.Sitemap):

    priority = 0.8

    changefreq = 'daily'

    def items(self):
        
        return ['ver_destinos']
    
    def location(self, item):
        
        return reverse(item)