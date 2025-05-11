// Retorna info para abrir maps en modal

$(".btnModalMaps").on( "click", function () {
        let info = $(this).data('info');
        $('.maps').html(info);
    });

// Agranda la letra al pasar con el mouse por el elemento td (celda en tabla)
$( "td" )
    .on( "mouseover", function() {
        $( this ).css('font-size','110%');
        $( this ).css('color','#0dcaf0');
    } )
    .on( "mouseout", function() {
        $( this ).css('font-size','small');
        $( this ).css('color','#fff');
} );

$( ".link-tabla" )
    .on( "mouseover", function() {
        $( this ).css('font-size','130%');
        $( this ).css('color','#0dcaf0');
    } )
    .on( "mouseout", function() {
        $( this ).css('font-size','small');
        $( this ).css('color','#0d6efd');
} );

$( "p" ).slideDown( "slow" ); // Aparece parrafo e imagenes de forma lenta al cargase la pagina

$( "img:hidden" ).fadeIn( 3000 );


  // Para Todos mis envios
$( "#id_buscar" ).autocomplete(
    { 
        source:"/ver_envios" 
    },
    "classes.ui-autocomplete", "highlight",
    "autoFocus", 
    true,);

$('#id_desde').datepicker({
    dateFormat: "yy-mm-dd"
    });

$('#id_hasta').datepicker({
    dateFormat: "yy-mm-dd"
    });


$('.agregarDoc').click(function (event) { //Cuando se hace click en el elemento agregarDoc
    "use strict";
    event.preventDefault(); // Previene que se desencadenen otros scripts
            
    let envioId = $(this).parent().find('.envioId').val(); // De el elemento padre busca el valor del elemento envioId
    
    localStorage.setItem(envioId, 'envio');   // Guarda mi dato en el LocalStorage	

    alert(envioId + " enviado a impresiones");

});

function printDiv(nombreDiv) {
    var contenido= document.getElementById(nombreDiv).innerHTML;   
    let i;
    for(i = 0; i < localStorage.length; i++){ 		// bucle for recorre todas las claves del LocalStorage
        let claveEliminar = localStorage.key(i);
        if(claveEliminar.startsWith("imp_")){		// Compueba si no comienza con "imp_"
            localStorage.removeItem(claveEliminar);	// si cumple con la declaracion lo elimina
            i--; // Resta uno ya que el la claves del localstorage son menores al eliminar elemento  
        };
    };

    document.body.innerHTML = contenido;

    window.print();

    location.reload(); 
};
