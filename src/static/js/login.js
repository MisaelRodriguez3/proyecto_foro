import see_password from "./utils/see_password.js";
import { required_fields } from "./utils/validate_fields.js";
import createFormData from "./utils/create_formData.js";
import { post_petition } from "./service/api.js";
import { error_alert, warning_alert } from "./utils/alerts.js";

// función para ver el contenido del campo passwoord
see_password("password", "see-password")

document.addEventListener("DOMContentLoaded", () => {
    //Obtener el formulario 
    const login_form = document.getElementById("login-form");

    //Evento de envio del formulario
    login_form.addEventListener("submit", async (e) => {
        // Prevenir la acción por defecto
        e.preventDefault();

        // Obtener el valor de los campos del formualrio
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        // Verificar que los campos no esten vacios
        const nullFields = await required_fields([email, password])
        if (nullFields) return

        // Organización de la información del formulario
        const data = [
            { "correo": email },
            { "password": password }
        ]

        // Crear un FormData con la información
        const formData = createFormData(data)

        post_petition("login", formData).then(res => {
            if(res.status !== 200) {
                console.log(res)
                return warning_alert(res.message)
            } 
            window.location.href = "/"
        }).catch(() => {
            error_alert()
        })
    })
})