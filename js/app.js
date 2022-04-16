const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // LETRAS Y ESPACIOS, PUEDEN LLEVAR ACENTOS
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
//Lete
    telefono: /^\d{8,9}$/, // 8 A 9 NUMEROS
    clave: /^[a-zA-ZÀ-ÿ\s]{1,40}$/,
    clave2: /^[a-zA-ZÀ-ÿ\s]{1,40}$/
// main
}

const campos = { //CAMPOS EN FALSO QUE AL MOMENTO DE VALIDAR CAMBIARAN
    nombre: false,
    correo: false,
    telefono: false,
// Lete
    clave: false,
    clave2: false
// main
}

const validarFormulario = (e) => {
    switch (e.target.name) { //EN CASO DE QUE SEA NOMBRE, CORREO ETC ENTRE A VALIDAR INMEDIATAMENTE
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
            break;
        case "correo":
            validarCampo(expresiones.correo, e.target, 'correo');
            break;
        case "telefono":
            validarCampo(expresiones.telefono, e.target, 'telefono');
            break;
        case "clave":
            validarCampo(expresiones.clave, e.target, 'clave');
        case "clave2":
            validaClave();      
    }
}

function validaClave() {
    if (document.getElementById(`clave`).value == document.getElementById(`clave2`).value) {
        document.getElementById(`grupo__clave2`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__clave2`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__clave2 i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__clave2 i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__clave2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos['clave2'] = true;
    } else {
        document.getElementById(`grupo__clave2`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__clave2`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__clave2 i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__clave2 i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__clave2 .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos['clave2'] = false;
// main
    }
}

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true; //EN CASO DE QUE EL CAMPO SEA CORRECTO SE CAMBIA A TRUE LA CONSTANTE
    } else {
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false; //SI NO, SIGUE EN FALSA Y SE VISUALIZA INCORRECTO
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario); //POR CADA VEZ QUE SE PRESIONE LA TECLA SE IRA VALIDANDO
    input.addEventListener('blur', validarFormulario); //POR CADA VEZ QUE SE PRESIONE FUERA DEL INPUT SE IRA VALIDANDO
});

formulario.addEventListener('submit', (e) => { //QUE AL PRESIONAR EL BOTON ENVIAR NO ENVIE EL FORMULARIO A NO SER QUE ESTE VALIDADO
    e.preventDefault();

    const terminos = document.getElementById('terminos'); // VALIDAR EN EL CHECK DE LOS TERMINOS QUE VALIDE SI EL RESTO ESTA BIEN, PARA ASI ENVIAR EL MENSAJE DE EXITO
    // da error en la consola el checked nosepq if (campos.nombre && campos.correo && campos.telefono && terminos.checked) {
    if (campos.nombre && campos.correo && campos.telefono && campos.clave && campos.clave2) { 
        formulario.reset();

        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);

        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
            icono.classList.remove('formulario__grupo-correcto');
        });
    } else {
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
    }
});
