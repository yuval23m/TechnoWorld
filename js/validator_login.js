    $("#formulario").validate({
        rules: {
            nombre:{
                required: true,
            },
            clave:{
                required: true,
                minlength: 7
            }
        },
        message: {
            nombre: "Por favor, introduzca su nombre",
            clave: {
                required: "Por favor introduzca su contraseña",
                minlength: "La contraseña debe tener como mínimo 7 carácteres"
            }
        },
        submitHandler: function(form){
            form.submit();
        }
    });