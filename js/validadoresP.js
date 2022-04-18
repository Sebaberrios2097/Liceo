// Validación de campos Inicio Sesión
$(document).ready(function() {
    $('.error').hide();
    $('#iniSesion').click(function() {
        let nombre = $('#nameInicio').val();
        let contra = $('#contraInicio').val();

        if (nombre == "" || nombre.length < 6) {
            $('#errorNombre').fadeIn();
            setTimeout(function() {
                $("#errorNombre").fadeOut(1500);
            }, 5000);
        }
        if (contra == "" || contra.length < 8) {
            $('#errorContra').fadeIn();
            setTimeout(function() {
                $("#errorContra").fadeOut(1500);
            }, 5000);
        }
    })
})



// Validación de campos Registro con JQUERY
let expr = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;

$(document).ready(function() {
    $('#formRegistro').submit(function() {
        let nombre = $('#nameRegistro').val();
        let apellido = $('#apRegistro').val();
        let correo = $('#correoRegistro').val();
        let contra1 = $('#contra1Registro').val();
        let contra2 = $('#contra2Registro').val();
        let nacimiento = $('#nacRegistro').val();

        if (nombre == "") {
            $('#errorNomRegVacio').fadeIn();
            setTimeout(function() {
                $("#errorNomRegVacio").fadeOut(1500);
            }, 5000);
        } else if (nombre.length < 3) {
            $('#errorNomRegIncompleto').fadeIn();
            setTimeout(function() {
                $("#errorNomRegIncompleto").fadeOut(1500);
            }, 5000);
        }
        if (apellido == "") {
            $('#errorApRegVacio').fadeIn();
            setTimeout(function() {
                $("#errorApRegVacio").fadeOut(1500);
            }, 5000);
        } else if (apellido.length < 3) {
            $('#errorApRegIncompleto').fadeIn();
            setTimeout(function() {
                $("#errorApRegIncompleto").fadeOut(1500);
            }, 5000);
        }
        if (correo == "") {
            $('#errorCorRegVacio').fadeIn();
            setTimeout(function() {
                $("#errorCorRegVacio").fadeOut(1500);
            }, 5000);
        } else if (!expr.test(correo)) {
            $('#errorCorRegIncorrecto').fadeIn();
            setTimeout(function() {
                $("#errorCorRegIncorrecto").fadeOut(1500);
            }, 5000);
        }
        if (nacimiento == "") {
            $('#errorNoFecha').fadeIn();
            setTimeout(function() {
                $("#errorNoFecha").fadeOut(1500);
            }, 5000);
        }
        if (contra1 == "") {
            $('#errorContraVacio').fadeIn();
            setTimeout(function() {
                $("#errorContraVacio").fadeOut(1500);
            }, 5000);
        } else if (contra1.length < 8) {
            $('#errorContraLargo').fadeIn();
            setTimeout(function() {
                $("#errorContraLargo").fadeOut(1500);
            }, 5000);
        }
        if (contra2 != contra1) {
            $('#errorContraNoIgual').fadeIn();
            setTimeout(function() {
                $("#errorContraNoIgual").fadeOut(1500);
            }, 5000);
        }
    })

})

//Validación de formulario de matrícula con Javascript

document.addEventListener("DOMContentLoader"),
    function() {
        document.getElementById("form-matricula").addEventListener('submit', validarFormulario);
    };

function validarFormulario(evento) {
    evento.preventDefault();
    var Fn = {
        // Valida el rut con su cadena completa "XXXXXXXX-X"
        validaRut: function(rutCompleto) {
            if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
                return false;
            var tmp = rutCompleto.split('-');
            var digv = tmp[1];
            var rut = tmp[0];
            if (digv == 'K') digv = 'k';
            return (Fn.dv(rut) == digv);
        },
        dv: function(T) {
            var M = 0,
                S = 1;
            for (; T; T = Math.floor(T / 10))
                S = (S + T % 10 * (9 - M++ % 6)) % 11;
            return S ? S - 1 : 'k';
        }
    }
    let nombres = document.getElementById()
}