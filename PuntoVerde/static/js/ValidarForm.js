function validarDatos(){
	var nombre,apellido,correo,correo2,mensaje,expresion;
	nombre=document.getElementById("validationDefault01").value;
	apellido=document.getElementById("validationDefault02").value;
	correo=document.getElementById("validationDefault03").value;
	correo2=document.getElementById("validationDefault04").value;
	mensaje=document.getElementById("validationDefault05").value;

	expresion=/\w+@\w+\.+[a-z]/;
  
	if(nombre ===""){
       alert("Ingrese Nombre");
	   return false;
	}
	else if(nombre.length<=3 || nombre.length>=20){
		alert("Ingrese Nombre Valido");
	   return false;
	}
	else if (apellido ===""){
		alert("Ingrese Apellido");
	   return false;
	}
	else if (apellido.length<=3 || apellido.length>=30){
		alert("Ingrese Apellido Valido");
	   return false;
	}
	else if (correo ===""){
		alert("Ingrese Correo");
	   return false;
	}
	else if (correo.length<=6){
		alert("Ingrese Correo Valido");
	   return false;
	}
	else if (correo.length>=50){
		alert("Correo demasiado largo");
	   return false;
	}
	else if (!expresion.test(correo)){
		alert("Formato Correo Invalido");
	   return false;
	}
	else if (correo2===""){
		alert("Re-Ingrese correo");
	   return false;
	}
	else if (correo2!=correo){
		alert("Correo NO coinciden");
	   return false;
	}
	else if (mensaje.length<=4){
		alert("Ingrese Mensaje más largo");
	   return false;
	}


}
