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
    $("#form_agregar_curso").validate({
        rules: {
            nro_curso: {
                number: true,
                required: true,
                maxlength: 1
            },
            letra: {
                lettersonly: true,
                required: true,
                maxlength: 1
            },
            anno_curso: {
                number: true,
                required: true,
                minlength: 4,
                maxlength: 4
            },
            cant_alumnos: {
                number: true,
                required: true
            },
        },
        messages: {
            nro_curso: {
                required: "El campo no puede estar vacío",
                maxlength: "No se permite más de 1 dígito"
            },
            letra: {
                required: "El campo no puede estar vacío",
                maxlength: "No se permite más de una letra"
            },
            anno_curso: {
                required: "Introduzca el año",
                maxlength: "El año debe tener 4 dígitos",
                minlength: "El año debe tener 4 dígitos"
            },
            cant_alumnos: {
                required: "Ingrese la cantidad de alumnos",
            },
        }

    });
});