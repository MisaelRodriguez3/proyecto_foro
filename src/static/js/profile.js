import createFormData from "./utils/create_formData.js"
import { changeInFields } from "./utils/validate_fields.js"
import { put_petition } from "./service/api.js"
import { warning_alert, success_alert, error_alert } from "./utils/alerts.js"

document.addEventListener("DOMContentLoaded", () => {
    const edit_profile_button = document.getElementById("edit-profile")
    const edit_profile_form = document.querySelector(".edit-profile-form-container")
    const close_form = document.querySelector(".close-icon")
    const change_avatar_icon = document.querySelector(".edit-image")
    const submit_button = document.querySelector(".save-changes")

    const avatar_file = document.querySelector(".image-input")

    const elementos = document.body.querySelectorAll("*")

    edit_profile_button.addEventListener("click", () => {
        edit_profile_form.classList.add("active")


        elementos.forEach(elemento => {
            if (elemento !== edit_profile_form && !edit_profile_form.contains(elemento) && !elemento.contains(edit_profile_form)) {
                elemento.classList.add("deshabilitado");
            }
        })
    })

    close_form.addEventListener("click", () => {
        edit_profile_form.classList.remove("active")
        elementos.forEach(elemento => {
            elemento.classList.remove("deshabilitado");
        })
        avatar_file.style.display = "none"
    })


    change_avatar_icon.addEventListener("click", () => {
        avatar_file.style.display = "flex"
    })

    const inputs = edit_profile_form.querySelectorAll("input")

    inputs.forEach(input => {
        input.addEventListener('input', () => {
            submit_button.classList.add("active")
        });
    });

    edit_profile_form.addEventListener("submit", (e) => {
        e.preventDefault();

        const user_Id = document.querySelector(".profile").getAttribute("data-id")

        const usuario = document.getElementById("usuario")
        const correo = document.getElementById("correo")
        const contraseña = document.getElementById("contrasena")
        const img = document.getElementById("avatar")

        const user = usuario.getAttribute("data-usuario")
        const email = correo.getAttribute("data-correo")
        const avatar = img.getAttribute("data-img")

        const initialData = [
            { usuario: user },
            { correo: email },
            { password: "" },
            { imagen_url: avatar}
        ]

        const finalData = [
            { usuario: usuario.value },
            { correo: correo.value },
            { password: contraseña.value },
            { imagen_url: img.value}
        ]

        const data = changeInFields(initialData, finalData)

        console.log(data)
        const formData = createFormData(data, true)

        for (let [key, value] of formData.entries()) {
            console.log(key, value);
        }

        put_petition("update-profile", user_Id, formData).then(res => {
            if(res.status !== 200) {
                return warning_alert(res.message)
            } 
            success_alert(res.message)
            window.location.reload()
        }).catch(() => {
            error_alert()
        })
    })


})