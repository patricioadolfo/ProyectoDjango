/*..............................................................................................
... PARA VALIDAR LOS DATOS .....................................................
.............................................................................................*/
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
/*..............................................................................................
... TODOS LOS CURSOS .............................................................
............................................................................................. */

$("#btnImp").on("click", function(){
	let valor;
	let lista =[] ; // defino array
	for(valor = 0; valor < localStorage.length; valor++){  //recorro valores del localStorage
		let key = localStorage.key(valor);
		if(key.startsWith("imp_")){ // Si el valor comienza con imp_
			lista.push(key); // guarda valor en array
		}
	}
	console.log(lista);
	verImpresiones(lista);
});

function verImpresiones(lista){
	$.ajax({
		beforeSend : function(xhr, settings){
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/ver_impresiones",
		type : "GET",
		data : { lista : JSON.stringify(lista), },
		success : function(json){
			let valor;
			$('#bodyImp').html("");	
			for(valor = 0; valor < json.length; valor++){ 
				let key = json[valor];

				valor_retornado ="<div class='row card-login'style='max-width: 95%;'>"+
									"<div class='col-xl-2 col-md-2 col-sm-5 col-xxl-2'>"+
										"<div id="+key.id+"></div>"+
									"</div>"+
									"<div class='col-xl-5 col-md-5 col-sm-12 col-xxl-5'>"+
										"<br>"+
										"<li>ID: "+key.id+"</li>"+
										"<li>Desde "+ key.origen+" hasta "+key.destino+" Creado el "+key.fecha+
											", a las "+key.hora+" hs por el usuario "+key.usuario+".</li>"+
									"</div>"+
									//"<br>"+
								"</div>";
				
				$('#bodyImp').append(valor_retornado);

				let codigoQRDiv = document.getElementById(key.id);
				
				let codigoQR = new QRCode(codigoQRDiv, {
					text: '123',
					width: 100,
					height: 100,
					colorDark : "#dee2e6",
					colorLight : "#212529",
					});
			}
		},
		error : function(xhr, errmsg, err){
			console.log('Error en carga de respuesta');
		},
	});
};




$( "#porFecha" ).on( "click", function(){
	desde = $( "#id_desde" ).val();
	hasta = $( "#id_hasta" ).val();
	respuestaPorFecha(desde, hasta)
});

function respuestaPorFecha(desde, hasta ){
    $.ajax({
        beforeSend : function(xhr, settings){
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/ver_envios_por_fecha",
		type : "GET",
		data : { desde : desde, hasta: hasta },
		success : function(json){
			let valor;	
			$('#tablaEnvios').html("");
			for(valor = 0; valor < json.length; valor++){ 
				
				let key = json[valor];
	
				valor_retornado ="<tr>"+                 
								"<td>"+key.origen+"</td>"+
								"<td>"+key.destino+"</td>"+
								"<td>"+key.otro_destino+"</td>"+
								"<td>"+key.fecha+"</td>"+
								"<td>"+key.hora+"</td>"+
								"<td>"+key.estado+"</td>"+
								"<th scope='row'>"+
								"<a href='"+key.id+"/ver' style='font-size: small;'>"+key.id+"</a>"+
								"</th>"+
								"</tr>";
				
				$('#tablaEnvios').append(valor_retornado);
			}
			
		},
		error : function(xhr, errmsg, err){
			console.log('Error en carga de respuesta');
		},
    });
};

$( "#boton_prod" ).on( "click", function(){
	valor = $( "#id_buscar" ).val();
	respuestaPorDestino(valor)
});

function respuestaPorDestino(valor){
    $.ajax({
        beforeSend : function(xhr, settings){
			if(!csrfSafeMethod(settings.type) && !this.crossDomain){
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "/ver_envios_por_destino",
		type : "GET",
		data : { valor : valor,},
		success : function(json){
			let valor;	
			$('#tablaEnvios').html("");
			for(valor = 0; valor < json.length; valor++){ 
				
				let key = json[valor];
	
				valor_retornado ="<tr>"+                 
								"<td>"+key.origen+"</td>"+
								"<td>"+key.destino+"</td>"+
								"<td>"+key.otro_destino+"</td>"+
								"<td>"+key.fecha+"</td>"+
								"<td>"+key.hora+"</td>"+
								"<td>"+key.estado+"</td>"+
								"<th scope='row'>"+
								"<a href='"+key.id+"/ver' style='font-size: small;'>"+key.id+"</a>"+
								"</th>"+
								"</tr>";
				
				$('#tablaEnvios').append(valor_retornado);
			}
			
		},
		error : function(xhr, errmsg, err){
			console.log('Error en carga de respuesta');
		},
    });
}


