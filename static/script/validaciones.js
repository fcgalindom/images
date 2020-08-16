
function validacionImagen() {
        var validarImagen = document.getElementById('validarImagen');
        var Ruta = validarImagen.value;
        var archivosP = /(.png|.jpg)$/i;
        if (!archivosP.exec(Ruta)) {
            alert('Asegurese que su archivo sea una imagen y tenga extencion JPG , JPEG o PNG');
            validarImagen.value = '';
            return false;
        }
 }
function alertaChecked(){
   	var  habilitar =  document.formulariImagen.checkTexto.checked


   	if (habilitar == true){
         document.formulariImagen.textoMeme.disabled = false;
         document.formulariImagen.numeroMeme.disabled = false;

   	}
   	else{
        document.formulariImagen.textoMeme.disabled = true;
        document.formulariImagen.numeroMeme.disabled = true;
   	}

}
function alterarTexto(){
	var  habilitar =  document.formulariImagen.ceckTamaño.checked
		if (habilitar == true){
         document.formulariImagen.cambiarAlto.disabled = false;
         document.formulariImagen.cambiarAncho.disabled = false;

   	}
   	else{
        document.formulariImagen.cambiarAlto.disabled = true;
        document.formulariImagen.cambiarAncho.disabled = true;
   	}




}


