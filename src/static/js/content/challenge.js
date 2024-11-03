import createFormData from "../utils/create_formData.js"
import { required_fields, changeInFields } from "../utils/validate_fields.js"
import { put_petition, delete_petition } from "../service/api.js"
import { warning_alert, success_alert, error_alert, confirmation_alert } from "../utils/alerts.js"

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("editar")
    const delete_challenge = document.getElementById("eliminar")
    const form = document.querySelector(".launch-challenge-container")
    const close_icon = document.querySelector(".close-icon")
    const submit_button = document.querySelector(".save-changes")

    const topic = document.querySelector(".container").getAttribute("data-topic")
    const reto_Id = document.querySelector(".challenge").getAttribute("data-challenge")

    const elementos = document.body.querySelectorAll("*")

    if(button) {
        button.addEventListener("click", () => {
            form.classList.add("active")
    
            elementos.forEach(elemento => {
                if(elemento !== form && !form.contains(elemento) && !elemento.contains(form)) {
                    elemento.classList.add("deshabilitado")
                }
            })
        })
    }


    close_icon.addEventListener("click", () => {
        form.classList.remove("active")
        elementos.forEach(elemento => {
            elemento.classList.remove("deshabilitado");
        })
    })

    const fields = form.querySelectorAll("input, textarea, select")

    fields.forEach(field => {
        field.addEventListener("input", (e) => {
            submit_button.classList.add("active")
        })
    })
    
    form.addEventListener("submit", async (e) => {
        e.preventDefault()

        // Campos del formulario
        const titulo = document.getElementById("titulo")
        const descripcion = document.getElementById("descripcion")
        const dificultad = document.getElementById("lv-dificultad")

        // valores iniciales
        const title = titulo.getAttribute("data-titulo")
        const description = descripcion.getAttribute("data-descripcion")
        const lvl = dificultad.getAttribute("data-dificultad")

        const nullFields = await required_fields([titulo.value, descripcion.value, dificultad.value])
        if (nullFields) return

        const initialData = [
            { titulo: title },
            { descripcion: description },
            { dificultad: lvl }
        ]

        const finalData = [
            { titulo: titulo.value },
            { descripcion: descripcion.value },
            { dificultad: dificultad.value }
        ]

        const data = changeInFields(initialData, finalData)
    
        const formData = createFormData(data)
        console.log(data)
        for (let [key, value] of formData.entries()) {
            console.log(key, value);
        }

        put_petition("update-challenge", reto_Id, formData).then(res => {
            if(res.status !== 200) {
                return warning_alert(res.message)
            }
            success_alert(res.message)
            window.location.reload()
        })
    })

    if(delete_challenge) {
        delete_challenge.addEventListener("click", () => {
            confirmation_alert("Eliminar reto", "eliminar").then(result => {
                if(result.isConfirmed) {
                    delete_petition("delete-challenge", reto_Id).then(res => {
                        if(res.status !== 200) {
                            return warning_alert(res.message)
                        }
                        success_alert(res.message)
                        window.location.href = `/${topic}/retos`
                    }).catch(() => {
                        error_alert()
                    })
                }
            })
        })
    }
})