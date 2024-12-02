import pytest
from hojaderuta.models import Envio

@pytest.mark.base
@pytest.mark.django_db
def test_crear_envio(fixture_base):

    envio = Envio(usuario= None,
                               
                  origen= fixture_base[1], 
                  
                  estado= fixture_base[0],  
                  
                  destino= fixture_base[1], 
                  
                  descripcion= "Envio desde pytest")
    
    envio.save()

    print("Envio ID", envio.id)

    assert envio.estado.nombre == "PREPARADO"

@pytest.mark.base
@pytest.mark.django_db
def test_crear_envio_factory(envio):

    print(envio.descripcion)

    print(envio.origen.nombre)

    assert envio.estado.nombre == "PREPARADO"


