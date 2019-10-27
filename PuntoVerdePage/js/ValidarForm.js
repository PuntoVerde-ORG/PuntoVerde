function validarDatos(){
	var nombre,apellido,correo,correo2,telefono,asunto,mensaje,expresion;
	nombre=document.getElementById("Nombres").value;
	apellido=document.getElementById("Apellidos").value;
	correo=document.getElementById("Correo").value;
	correo2=document.getElementById("Correo2").value;
	telefono=document.getElementById("Telefono").value;
	asunto=document.getElementById("Asunto").value;
	mensaje=document.getElementById("Mensaje").value;
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
	else if (isNaN(telefono)){
		alert("Telefono Ingresado No Valido");
	   return false;
	}
	else if (telefono.length<9){
		alert("Le Faltan Numeros al telefono");
	   return false;
	}
	else if (asunto.length<4){
		alert("Ingrese un asunto");
	   return false;
	}
	else if (mensaje.length<=4){
		alert("Ingrese Mensaje más largo");
	   return false;
	}


}
