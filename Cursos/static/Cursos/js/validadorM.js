jQuery.validator.addMethod('lettersonly', function(value, element) {
    return this.optional(element) || /^[a-z áãâäàéêëèíîïìóõôöòúûüùçñ]+$/i.test(value);
}, "Introduzca solo letras");


$(document).ready(function() {
    $("#formMatricula").validate({
        rules: {
            PnomAlumno: {
                lettersonly: true,
                required: true,
                minlength: 3
            },
            SnomAlumno: {
                lettersonly: true,
                required: true,
                minlength: 3
            },
            appAlumno: {
                lettersonly: true,
                required: true,
                minlength: 3
            },
            apmAlumno: {
                lettersonly: true,
                required: true,
                minlength: 3
            },
            rutAlumno: {
                required: true,
                minlength: 8,
                maxlength: 9
            },
            dvAlumno: {
                maxlength: 1,
                required: true
            },
            nacAlumno: {
                required: true
            },
            correoAlumno: {
                required: true,
                email: true
            },
            motivoAlumno: {
                required: true,
                minlength: 10,
                maxlength: 200
            },
            nomApoderado: {
                required: true,
                lettersonly: true,
                minlength: 3
            },
            apApoderado: {
                required: true,
                lettersonly: true,
                minlength: 3
            },
            correoApoderado: {
                required: true,
                email: true
            },
        },
        messages: {
            PnomAlumno: {
                required: "El campo no puede estar vacío",
                minlength: "El nombre debe tener mínimo 3 caracteres"
            },
            SnomAlumno: {
                required: "El campo no puede estar vacío",
                minlength: "El nombre debe tener mínimo 3 caracteres"
            },
            appAlumno: {
                required: "El campo no puede estar vacío",
                minlength: "El apellido debe tener mínimo 3 caracteres"
            },
            apmAlumno: {
                required: "El campo no puede estar vacío",
                minlength: "El apellido debe tener mínimo 3 caracteres"
            },
            rutAlumno: {
                required: "El campo no puede estar vacío",
                minlength: "El rut debe tener mínimo 8 caracteres",
            },
            dvAlumno: {
                required: "El campo no puede estar vacío",
                maxlength: "El dv debe tener maximo 1 caracter"
            },
            nacRegistro: {
                required: "Introduzca una fecha"
            },
            correoAlumno: {
                required: "Ingrese correo",
                email: "Correo inválido"
            },
            motivoAlumno: {
                required: "El campo no puede estar vacío",
                minlength: "El motivo debe tener minimo 10 caracteres",
                maxlength: "El motivo debe tener maximo 200 caracteres"
            },
            nomApoderado: {
                required: "El campo no puede estar vacío",
                minlength: "El nombre debe tener mínimo 3 caracteres"
            },
            apApoderado: {
                required: "El campo no puede estar vacío",
                minlength: "El apellido debe tener mínimo 3 caracteres"
            },
            correoApoderado: {
                required: "Ingrese correo",
                email: "Correo inválido"
            },
        }

    });
});