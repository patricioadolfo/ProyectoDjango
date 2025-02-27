// Retorna info para abrir maps en modal

function  verMaps() {
    $(".btnModalMaps").click(function () {
        let info = $(this).data('info');
        $('.maps').html(info);
    });
};

// Agranda la letra al pasar con el mouse por el elemento td (celda en tabla)
$( "td" )
    .on( "mouseover", function() {
        $( this ).css('font-size','medium');
    } )
    .on( "mouseout", function() {
        $( this ).css('font-size','small');
} );

// Aparece parrafo e imagenes de forma lenta al cargase la pagina

function parrafos() {
    $( "p" ).slideDown( "slow" );
    };   

function verImagen() {
        $( "img:hidden" ).fadeIn( 3000 );
  } ;

$(document).ready( function(){
    parrafos();
    verMaps();
    verImagen();
});


