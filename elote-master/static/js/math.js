// Evento que se dispara cuando se termina de cargar el DOM
// DOM: Document Object Model
document.addEventListener("DOMContentLoaded", function() {

        // Declaramos una variable en JavaScript que representa el botón "btn-ok" en el HTML
        var btnOK = document.getElementById("btn-ok");
        
        //Declaramos un evento click a ese botón
        btnOK.addEventListener("click", function() {
           
            //Aquí agarramos el valor (o contenido) de la caja de texto input
            // El cual retorna un tipo string
            var value1 = document.getElementById("input-value1").value;

            //Transforma el valor de la caja de texto a tipo float
            var value1Number = parseFloat(value1)

            //En una sola línea obtiene el valor del texto del input y lo transforma a float
            var value2Number = parseFloat(document.getElementById("input-value2").value);


            // isNaN = is not a number
            if(isNaN(value1Number) || isNaN(value2Number)) {
                // alert es un mensaje para el usuario
                alert("Introduce solamente valores numéricos");
                // console son mensajes para el desarrollador
                console.error("El usuario ingresó un valor inválido");
                return;
            }
            
            var result = value1Number + value2Number;
            alert("La suma de los valores es " + result);
            
    })
})