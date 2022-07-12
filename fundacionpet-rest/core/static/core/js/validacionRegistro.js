const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    rut: /^.{9,9}$/, // 9 a 10 digitos.
    telefono: /^\d{9,9}$/, // 9 numeros.
    password: /^.{4,12}$/, // 4 a 12 digitos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/

}

const campos = {
    usuario: false,
    nombre: false,
    apellido: false,
    rut: false,
    telefono: false,
    password: false,
    correo: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "usuario":
            validarCampo(expresiones.usuario, e.target, 'usuario');
            break;
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
            break;
        case "apellido":
            validarCampo(expresiones.apellido, e.target, 'apellido');
            break;
        case "rut":
            validarCampo(expresiones.rut, e.target, 'rut');
            break;
        case "telefono":
            validarCampo(expresiones.telefono, e.target, 'telefono');
            break;
        case "password":
            validarCampo(expresiones.password, e.target, 'password');
            validarPassword2();
            break;
        case "password2":
            validarPassword2();
            break;
        case "correo":
            validarCampo(expresiones.correo, e.target, 'correo');
            validarCorreo2();
            break;
        case "correo2":
            validarCorreo2();
            break;

    }
}

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
    } else {
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
    }
}

const validarPassword2 = () => {
    const inputPassword1 = document.getElementById('password');
    const inputPassword2 = document.getElementById('password2');

    if (inputPassword1.value !== inputPassword2.value) {
        document.getElementById(`grupo__password2`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__password2 i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__password2 i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos['password'] = false;
    } else {
        document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__password2`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__password2 i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__password2 i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__password2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos['password'] = true;
    }
}

const validarCorreo2 = () => {
    const inputCorreo1 = document.getElementById('correo');
    const inputCorreo2 = document.getElementById('correo2');

    if (inputCorreo1.value !== inputCorreo2.value) {
        document.getElementById(`grupo__correo2`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__correo2`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__correo2 i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__correo2 i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__correo2 .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos['correo'] = false;
    } else {
        document.getElementById(`grupo__correo2`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__correo2`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__correo2 i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__correo2 i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__correo2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos['correo'] = true;
    }
}

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    const suscripcionOK = document.getElementById('suscripcionOK');
    const suscripcionNO = document.getElementById('suscripcionNO');

    if (campos.nombre && campos.apellido && campos.rut && campos.telefono && campos.password && campos.correo && terminos.checked) {
        formulario.reset();

        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);
        $.notify("¡Su registro a finalizado con exito!", { color: '#fff', background: '#20D67B' });

        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
            icono.classList.remove('formulario__grupo-correcto');
        });

        alert("¡Su registro a finalizado con éxito!");
        window.location.href = "./error_404.html";

    } else if (campos.nombre && campos.apellido && campos.rut && campos.telefono && campos.password && campos.correo && terminos.checked == false) {

        $.notify("Por favor, acepte los términos y condiciones.", { color: '#fff', background: '#D44950' });

    } else {
        $.notify("Porfavor, Complete los campos obligatorios del formulario", { color: '#fff', background: '#D44950' });
    }
});