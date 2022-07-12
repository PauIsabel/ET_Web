const formulario = document.getElementById('formulario-login');
const inputs = document.querySelectorAll('#formulario-login input');

const expresiones = {
    usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
    nombre: /^[a-zA-Z�-�\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-Z�-�\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    rut: /^.{9,9}$/, // 9 a 10 digitos.
    telefono: /^\d{9,9}$/, // 9 numeros.
    password: /^.{4,12}$/, // 4 a 12 digitos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/

}

const campos = {
    password: false,
    correo: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "password":
            validarCampo(expresiones.password, e.target, 'password');
            break;
        case "correo":
            validarCampo(expresiones.correo, e.target, 'correo');
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

inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    if (campos.password && campos.correo) {
        formulario.reset();
        $.notify("�Acceso correcto!", { color: '#fff', background: '#20D67B' });

        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
            icono.classList.remove('formulario__grupo-correcto');
        });

        alert("!Bien!, Has accedido a su cuenta correctamente");
        window.location.href = "./404.html";
    } else {
        $.notify("Porfavor, Complete los campos obligatorios del formulario", { color: '#fff', background: '#D44950' });
    }
});