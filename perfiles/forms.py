from django import forms
from perfiles.models import Perfil
from nodos.models import Nodo
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):

    nodos = forms.ModelMultipleChoiceField(
        
        queryset = Nodo.objects.all(),
                                    
            widget = forms.CheckboxSelectMultiple( 
                
                attrs = { 
                            
                    'data-bs-theme' : 'dark',

                    'style' : 'margin: 8px 10px 3px 8px;',

                    } 
                
                ) 
            )
    
    class Meta:
            
        model = Perfil
                
        fields = ['nodos',]

    def __init__(self, *args, **kwargs):

        super(PerfilForm, self).__init__(*args, **kwargs)

class UsuarioForm(forms.ModelForm):
   
    class Meta:
            
        model = User
                
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):

        super(UsuarioForm, self).__init__(*args, **kwargs)