from django import forms
from hojaderuta.models import Envio

class EnvioForm(forms.ModelForm):

    class Meta:
            
        model = Envio
        
        widgets = {
            
            'origen': forms.Select(attrs={'class': 'form-select', 'disabled': True }),
            
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            
            '(destino': forms.Select(attrs={'class': 'form-select'}),
        
        }
        
        fields = ('origen', 'destino' ,'descripcion',)


    def __init__(self, *args, **kwargs):

        super(EnvioForm, self).__init__(*args, **kwargs)