import createFormData from "../utils/create_formData.js"
import { required_fields } from "../utils/validate_fields.js"
import { post_petition } from "../service/api.js"
import { warning_alert, error_alert, success_alert } from "../utils/alerts.js"

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("ask-question")
    const form = document.querySelector(".ask-question-container")
    const close_icon = document.querySelector(".close-icon")
    const submit_button = document.querySelector(".save-changes")

    const elementos = document.body.querySelectorAll("*")

    button.addEventListener("click", () => {
        form.classList.add("active")

        elementos.forEach(elemento => {
            if(elemento !== form && !form.contains(elemento) && !elemento.contains(form)) {
                elemento.classList.add("deshabilitado")
            }
        })
    })


    close_icon.addEventListener("click", () => {
        form.classList.remove("active")
        elementos.forEach(elemento => {
            elemento.classList.remove("deshabilitado");
        })
    })

    const fields = form.querySelectorAll("input, textarea")

    fields.forEach(field => {
        field.addEventListener("input", (e) => {
            submit_button.classList.add("active")
        })
    })

    form.addEventListener("submit", async (e) => {
        e.preventDefault()

        // Campos del formulario
        const titulo = document.getElementById("titulo").value
        const descripcion = document.getElementById("descripcion").value
        const codigo = document.getElementById("codigo").value
        const topic = document.querySelector(".container").getAttribute("data-topic")

        const nullFields = await required_fields([titulo, descripcion])
        if (nullFields) return

        const data = [
            { titulo: titulo },
            { descripcion: descripcion },
            { codigo: codigo },
            { topic: topic }
        ]
    
        const formData = createFormData(data)
        console.log(data)
        for (let [key, value] of formData.entries()) {
            console.log(key, value);
        }

        // Crear Post
        post_petition("add-post", formData).then(res => {
            if (res.status !== 200) {
                return warning_alert(res.message)
            }
            success_alert(res.message)
            elementos.forEach(elemento => {
                elemento.classList.remove("deshabilitado");
            })
            form.classList.remove("active")

            window.location.reload()
        }).catch(() => {
            error_alert()
        })
    })
    
})