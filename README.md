# PROYECTO DJANGO
## Descripción del proyecto

El proyecto consiste en un sitio para envíos desde una sucursal (nodo) a otra dentro de una cadena de farmacias. Con la posibilidad de crear nuevos destinos diferentes a las sucursales en caso de ser necesario. 

Dentro de cada envío se detalla el usuario de creación, fecha, hora, estado y la descripción. Cada envío tiene un seguimiento; este detalla también al usuario que lo modificó y su nuevo estado con fecha y hora. El fin de este seguimiento es para tener un control de cada envío para saber su estado actual y si llegó a su destino correcto.

## Estados

Actualmente, los envíos cuentan con 4 estados:

* PREPARADO: Indica el nivel inicial de un envío, es decir, se creó un envío y está en la sucursal de origen.

* IGNORADO: Este es el caso de un envío creado por error o por x motivo no debe ser enviado. Solo puede tomar este estado por su usuario de creación.

* EN CAMINO: El envío debe tomar este estado cuando el repartidor lo retira de su sucursal de origen. Y está listo para ser entregado a la sucursal destino o al destino nuevo que creó el usuario de envío (ejemplo: un envío a una ferretería, la cual es ajena a la organización).

* ENTREGADO: Por último, este es el estado que le da un cierre al envío, solo puede tomar dicho estado por un usuario correspondiente a la sucursal de destino. En el caso de ser un envío con destino diferente, es el repartidor quien puede hacer esta modificación.

Los estados no solo sirven para envíos, sino que también para habilitar/deshabilitar nodos/destinos por el usuario administrador. La función de crear nuevos estados es para definir situaciones que se presenten a futuro con respecto a envíos, nodos, links de accesos. Uno de los objetivos principales de los estados es no eliminar información dentro de la base de datos, sino actualizar su situación.

## Login y perfil del usuario

El proyecto actualmente cuenta con "registration-redux" para la creación de usuarios y una sección de perfil para que el usuario complete indicando a la o las sucursales a las que pertenece. Vale mencionar que un usuario puede pertenecer solo a una sucursal o a varias, lo que le da acceso a enviar desde todos sus nodos y recibir envíos con destinos a esos nodos. En producción, la sección de perfil solo va a ser administrada por un usuario con privilegios. Este mismo será quien defina la o las sucursales en las que pueden operar los usuarios.   

# Sitio
## Página Principal

Esta sección del sitio ofrece información al usuario logueado de sus envíos, los que tiene para recibir y los envíos que serán enviados a destinos fuera de la organización, todos estos datos son presentados en forma de tabla con la posibilidad de acceder a un detalle más exacto de cada envío, este muestra más información sobre el envío y los cambios de estados que afectaron dicho envío, también muestra un código QR del ID del envío, esta será útil para que el usuario repartidor para reconocer rápidamente el envío a la hora de recibirlo y actualizar su estado a "EN CAMINO", y para el usuario receptor a la hora de recepcionar y cambiar su estado a "RECIBIDO".

Dentro de la sección *MIS ENVÍOS* y *OTROS DESTINOS* está el link para acceder al formulario para crear en envíos. En los dos casos, este formulario solo dará la opción para crear los envíos con origen relacionado a  nodos (sucursales) habilitados que tenga el usuario logueado. La fecha y hora de creación no serán un campo a completar, ya que la base de datos tomaría por defecto la actual. Solo deberá completar el destino (nodo de la organización) al cual quieran relacionar su envío y una descripción de lo que se está enviando.

La diferencia con la sección para "otros destinos" es que el formulario ofrecerá una lista de destinos por fuera de la organización habilitados para los usuarios. De no existir dicho destino, el usuario deberá acceder a *DESTINOS* y crearlo. 

## Sección de NODOS y DESTINOS

Estas dos secciones ofrecen información de los orígenes/destinos habilitados, como la dirección, teléfono y localidad de los mismos, y también un enlace para ver su ubicación dentro de mapas de Google. Dicha información es útil para que el usuario repartidor sepa dónde retirar y/o entregar los pedidos. El caso de los nodos (sucursales de la cadena) son ingresados por el administrador. En el caso de los destinos, pueden ser creados por el usuario para casos en que los envíos sean para fuera de la organización.

## Sección QR 

Aún no realizada, se proyecta utilizar la cámara para escanear el QR de los envíos y acceder de forma rápida a ellos.

## Sección Footer

Dentro del sitio se puede ver el footer, el cual contiene links de acceso a páginas externas al sitio que la organización considere útiles. Estos links deben ser creados desde el panel 'admin', para que el usuario los pueda ver.

# Base de datos

Actualmente, la base de datos es la que Django ofrece por defecto (SQLite). En producción está planeado utilizar PostgreSQL, ya que es la base de datos con la que tengo más afinidad. 

A continuación se detallan las tablas y su relación.

* Tabla Estado (declarada dentro de app estado): Detalla la situación actual. 

    - id: Identificador único. (int)

    - nombre: Nombre de estado. (str)

    - color: color opcional para identificarlo, ingresar código hexadecimal (str)

*  Tabla Envío (declarada dentro de la app hojaderuta): Donde se crean todos los envíos.
    
    - id: Identificador único. (int)

    - usuario: Clave foránea relacionada con la clase User de Django. Esta representa al usuario creador.
    
    - origen: Clave foránea relacionada con la tabla Nodos. Esta representa el origen de un envío.

    - otro_origen: Clave foránea relacionada con la tabla Destinos. Esta representa a un envío con origen exento de organización (actualmente en desuso). 

    - estado: Clave foránea con tabla Estado. Representa la situación actual de dicho envío.
   
    - destino: Clave foránea con tabla Nodos. Representa el destino del envío.
    
    - otro_destino: Clave foránea relacionado con la tabla Destinos. Esta representa a un envío con destino exento a la organización. 
    
    - descripcion: Detalle de lo que se envía de clase TextField.(str)
    
    - fecha: Fecha de creación del envío. (date)
    
    - hora: Hora de creación del envío. (time) 


El proyecto trata de un sitio de envíos y recepción de pedidos. Para que los usuarios carguen envíos desde un nodo al otro, los nodos son pre cargados por la empresa o el administrador, y cuenta con la posibilidad de que el usuario cree diferentes destinos para hacer sus envíos desde nodos a diferentes destinos o de diferentes destinos a los nodos de la empresa. 

Cada envío cuenta con los de detalles de preparación y  la posibilidad de detallar los movimientos a modo de histórico los cambios de estado que van surgiendo de dicho envío (ejemplo: si el envío es retirado por el repartidor se detalla que el estado del envío es EN CAMINO y cuando es recibido el estado del envío cambia a RECIBIDO). El proyecto cuenta también con la posibilidad de crear nuevos estados, los cuales son creados por el administrador con el fin de detallar nuevas posibilidades que sucedan con los envíos (ej:  el envío no se realizara por x motivo... entonces el estado cambiaria a IGNORADO) y o también para crear estados que describan la situación actual de los nodos, destinos e impresoras.

Sumado a los campos que por defecto trae Django para el registro de usuarios, se agrega el perfil de usuario, este declara si el usuario es repartidor o no y le asigna un nodo que le dará la posibilidad de ver los envíos asignados a ese nodo y no al resto, también así le asigna una impresora (esta parte es destinada a una API)

El usuario que contenga el perfil de reparto podrá ver los pedidos de todos los nodos y solo podrá cambiar de estado PREPARADO a EN CAMINO y el usuario que tenga asignado un nodo solo podrá crear pedidos desde su propio nodo y recibir pedidos referidos a su nodo (ej: cambiar el estado del pedido de EN CAMINO a RECIBIDO) o en el caso de ser quien lo creo podrá cancelar dicho envío.

El proyecto cuenta con un sector dedicado al servicio de impresión (esta parte es destinada a una API), se crean impresoras y se destinan a nodos, y cada envío creado desde la API se pone en una cola de impresión con su respectiva impresora.

Contiene un sector para crear links relacionados con la empresa, estos serán alojados  dentro del footer.

## Boceto para escritorio

![Diseño para escritorio](media/diseñoDSK.png)

En la parte superior una barra de navegación que contiene de izquierda a derecha: 
    
* El nombre del proyecto.

* Los botones de navegación:

    - Home: lleva a la página principal del proyecto

    - Qr: Abre un lector de Qr, cada envío generará un qr el cual podrá ser leído por el lector.

    - Envíos: Dirige a un listado de envíos ordenados cronológicamente.

    - Nodos: Dirige a un listado de Nodos disponibles para realizar los envíos, contiene el detalle de cada nodo (dirección, teléfono, etc.).

    - Destinos: Al igual que los Nodos nos da un listado de los destinos disponibles, y un formulario para crear nuevos destinos.

* Nombre o imagen de usuario logueado en el caso de que lo este, de lo contrario un enlace para registrarse.

* Por último un botón de login - logout

Como cuerpo de la página principal, el listado de los envíos creados por el usuario logueado y  los envíos que recibirá dicho usuario dependiendo del nodo que tenga asignado. Dentro del listado cada envío mostrará sus detalles de preparación y llevará a un enlace único de donde podrá ver el qr asociado al envío y un campo para imprimirlo.

Por último un footer que contenga enlaces a diferentes páginas relacionadas con la empresa creados por el administrador, se mostrará a modo de icono/imagen.

## Boceto para movil

![Diseño movil](media/diseñoMOVIL.png)

Contiene los mismos ítems que el diseño de escritorio, con la diferencia de que los botones de la barra de navegación se agrupan dentro de un icono de menú.  
