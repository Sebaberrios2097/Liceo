// Validación de campos Inicio Sesión
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("frmDatos").addEventListener('submit', valForm);
});

function valForm(evento) {
    evento.preventDefault();
    var usuario = document.getElementById('nameInicio').value;
    var Errores = 0;
    if (usuario.length == 0) {
        document.getElementById("errorNombre").innerHTML = "El nombre es inválido";
        document.getElementById("errorNombre").classList.add("error");
        Errores += 1;
    }
    var clave = document.getElementById('contraInicio').value;
    if (clave.length < 6) {
        document.getElementById("errorContra").innerHTML = "La contraseña es inválida";
        document.getElementById("errorContra").classList.add("error");
        Errores += 1;
    }

    if (Errores > 0) {
        return;
    }
    this.submit();
}



// Validación de campos Registro con JQUERY

jQuery.validator.addMethod('lettersonly', function(value, element) {
    return this.optional(element) || /^[a-z áãâäàéêëèíîïìóõôöòúûüùçñ]+$/i.test(value);
}, "Introduzca solo letras");


$(document).ready(function() {
    $("#formRegistro").validate({
        rules: {
            namesRegistro: {
                lettersonly: true,
                required: true,
                minlength: 3
            },
            apRegistro: {
                lettersonly: true,
                required: true,
                minlength: 3
            },
            correoRegistro: {
                required: true,
                email: true
            },
            nacRegistro: {
                required: true
            },
            contra1Registro: {
                required: true
            },
            contra2Registro: {
                required: true,
                equalTo: "#contra1Registro"
            },
        },
        messages: {
            namesRegistro: {
                required: "El campo no puede estar vacío",
                minlength: "El nombre debe tener mínimo 3 caracteres"
            },
            apRegistro: {
                required: "El campo no puede estar vacío",
                minlength: "El apellido debe tener mínimo 3 caracteres"
            },
            nacRegistro: {
                required: "Introduzca una fecha"
            },
            correoRegistro: {
                required: "Ingrese correo",
                email: "Correo inválido"
            },
            contra1Registro: {
                required: "Ingrese contraseña"
            },
            contra2Registro: {
                required: "Ingrese contraseña",
                equalTo: "Las contraseñas no coinciden"
            }
        }

    });
});