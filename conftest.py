import pytest
from nodos.models import Nodo
from estados.models import Estado
from hojaderuta.models import Envio
from faker import Faker

fake = Faker()

@pytest.fixture
def fixture_base(db):

    estado_activo= Estado(nombre= "ACTIVO")

    estado_activo.save()

    estado_preparado= Estado(nombre= "PREPARADO")

    estado_preparado.save()

    nodo= Nodo(
        
        nombre= "CENTRAL", 
        
        calle= "Rivadavia", 
        
        numero= 1001, 
        
        localidad= "Jose C Paz", 
        
        telefono= "1532267049", 
        
        estado= estado_activo 
        
        )
    
    nodo.save()
    
    yield estado_preparado, nodo

    print("retorna nodo " + nodo.nombre + " y estado " + estado_preparado.nombre)

@pytest.fixture()
def fixture_base_factory(db):
    
    estado_activo= Estado(nombre= "ACTIVO")

    estado_activo.save()

    estado_preparado= Estado(nombre= "PREPARADO")

    estado_preparado.save()

    nodo= Nodo( nombre= fake.name(), calle= "Rivadavia", numero= 1001, localidad= "Jose C Paz", telefono= fake.phone_number(), estado= estado_activo)
    
    nodo.save()
    
    def crear_envio(
            
            descripcion: str = "Envio desde pytest",
            
            usuario = None, 
            
            origen = nodo, 
            
            estado = estado_preparado, 
            
            destino = nodo, 
            
            ):
        
        envio = Envio(usuario= usuario,
                            
                origen= origen, 
                
                estado= estado,  
                
                destino= destino, 
                
                descripcion= descripcion)
    
        envio.save()

        return envio
    
    return crear_envio

@pytest.fixture()
def envio(db, fixture_base_factory):

    return fixture_base_factory(fake.text(), None)


