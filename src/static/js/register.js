import see_password from "./utils/see_password.js";
import {required_fields, compare_two_fields} from "./utils/validate_fields.js";
import createFormData from "./utils/create_formData.js";
import { post_petition } from "./service/api.js";
import { warning_alert, error_alert } from "./utils/alerts.js";

/** Funciones para poder ver las contraseñas */
see_password("password", "see-password")
see_password("password_confirmation", "see-password_confirmation")


document.addEventListener("DOMContentLoaded", () => {
    // Obtener el formulario 
    const register_form = document.getElementById("register-form")

    //Gestionar el evento de envio del formulario
    register_form.addEventListener("submit", async (e) => {
        // Prevenir las acciones por defecto
        e.preventDefault();

        // Obtener el valor de los campos del formulario
        const fullname = document.getElementById("fullname").value;
        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        const password_confirmation = document.getElementById("password_confirmation").value;

        // Lista de los campos
        const fields = [fullname, username, email, password, password_confirmation]

        // Verifica que ningun campo este vacío
        const nullFields = await required_fields(fields)
        if (nullFields) return

        // Verifica que las contraseñas sean iguales
        const errorPassword = await compare_two_fields(password, password_confirmation, "Las contraseñas no coinciden")
        if(errorPassword) return

        const data = [
            { "fullname": fullname },
            { "username": username },
            { "email": email },
            { "password": password }
        ]

        const formData = createFormData(data)

        for (let [key, value] of formData.entries()) {
            console.log(key, value);
        }

        post_petition("register", formData).then(res => {
            if(res.status !== 200) {
                return warning_alert(res.message)
            }
            window.location.href = "/"
        }).catch(() => {
            error_alert()
        })
    })
})

