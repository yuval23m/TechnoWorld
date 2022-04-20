$(document).ready(function () {

    $("#formulario").validate({
        // in 'rules' user have to specify all the constraints for respective fields
        rules: {
            nombre: {
                required: true,
                minlength: 2  //for length of lastname
            },
            pw1: {
                required: true,
                minlength: 5
            },
            pw2: {
                equalTo: "#clave" //for checking both passwords are same or not
            },
            correo: {
                required: true,
                email: true
            },
            telefono: {
                required: true,
                minlength: 8
            }
        },
        // in 'messages' user have to specify message as per rules
        messages: {
            nombre: {
                required: "Ingrese nombre",
                minlength: "El Nombre debe ser de largo minimo 2"
            },
            pw1: {
                required: "Por favor ingrese una contraseña",
                minlength: "La contraseña debe ser de largo minimo 5"
            },
            pw2: {
                equalTo: "Las contraseña no coinciden"
            },
            telefono: "Ingrese telefono"
        }
    });
});