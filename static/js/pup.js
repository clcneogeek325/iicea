
var ventana_pup; 

function abrirVentana(){

	ventana_pup = window.open('/add_user/', 'popup', 'width=800,height=500');
       return false;	
}


function cerraVentana() {
	ventana_pup.close();
	this.reload();
	return false;
}
