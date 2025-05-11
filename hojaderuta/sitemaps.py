from django.contrib import sitemaps
from django.urls import reverse

class HojaDeRutaSiteMaps(sitemaps.Sitemap):

    priority = 0.9

    changefreq = 'daily'

    def items(self):
        
        return ['index']
    
    def location(self, item):
        
        return reverse(item)