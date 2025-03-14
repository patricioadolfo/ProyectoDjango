from django import forms
from hojaderuta.models import Envio

class EnvioForm(forms.ModelForm):
    class Meta:
            
        model = Envio
        
        widgets = {
            
            'origen': forms.Select(attrs={'class': 'form-select'}),

            'destino': forms.Select(attrs={'class': 'form-select'}),
            
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 206px;'}),
        
        }
        
        fields = ['origen', 'destino' ,'descripcion']


    def __init__(self, *args, **kwargs):

        super(EnvioForm, self).__init__(*args, **kwargs)

class EnvioOtroDestinoForm(forms.ModelForm):
    class Meta:
            
        model = Envio
        
        widgets = {
            
            'origen': forms.Select(attrs={'class': 'form-select' }),

            'otro_destino': forms.Select(attrs={'class': 'form-select'}),
            
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 175px;'}),
        
        }
        
        fields = ['origen', 'otro_destino' ,'descripcion']


    def __init__(self, *args, **kwargs):

        super(EnvioOtroDestinoForm, self).__init__(*args, **kwargs)

class BuscarDestino(forms.Form):
    
    buscar = forms.CharField(
        
        label='Selecciona destino', 
        
        widget=forms.TextInput(
            
            attrs=
            {
                'class': 'form-control form-sm'
                }
            )
        )
    
class FormFechas(forms.Form):
    
    desde = forms.CharField(
        
        label='Desde', 
        
        widget=forms.DateInput(
            
            attrs=
            {
                'class': 'form-control form-sm'
                }
            )
        )
    
    hasta = forms.CharField(
        
        label='Hasta', 
        
        widget=forms.DateInput(
            
            attrs=
            {
            'class': 'form-control form-sm'
             }
            )
        )