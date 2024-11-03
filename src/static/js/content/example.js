import createFormData from "../utils/create_formData.js"
import { required_fields, changeInFields } from "../utils/validate_fields.js"
import { put_petition, delete_petition } from "../service/api.js"
import { warning_alert, success_alert, confirmation_alert, error_alert } from "../utils/alerts.js"

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("editar")
    const delete_example = document.getElementById("eliminar")
    const form = document.querySelector(".upload-example-container")
    const close_icon = document.querySelector(".close-icon")
    const submit_button = document.querySelector(".save-changes")

    const ejemplo_Id = document.querySelector(".example").getAttribute("data-example")
    const topic = document.querySelector(".container").getAttribute("data-topic")

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

    const fields = form.querySelectorAll("input, textarea")

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
        const codigo = document.getElementById("codigo")

        // Valores iniciales
        const title = titulo.getAttribute("data-titulo")
        const description = descripcion.getAttribute("data-descripcion")
        const code = codigo.getAttribute("data-codigo")

        const nullFields = await required_fields([titulo.value, descripcion.value, codigo.value])
        if (nullFields) return
        
        const initialData = [
            { titulo: title },
            { descripcion: description },
            { codigo: code }
        ]

        const finalData = [
            { titulo: titulo.value },
            { descripcion: descripcion.value },
            { codigo: codigo.value }
        ]

        const data = changeInFields(initialData, finalData)
    
        const formData = createFormData(data)
        console.log(data)
        for (let [key, value] of formData.entries()) {
            console.log(key, value);
        }

        put_petition("update-example", ejemplo_Id, formData).then(res => {
            if(res.status !== 200) {
                return warning_alert(res.message)
            }
            success_alert(res.message)
            window.location.reload()
        }).catch(() => {
            error_alert()
        })
    })

    delete_example.addEventListener("click", () => {
        confirmation_alert("Eliminar ejemplo", "eliminar").then(result => {
            if(result.isConfirmed) {
                delete_petition("delete-example", ejemplo_Id).then(res => {
                    if(res.status !== 200) {
                        return warning_alert(res.message)
                    }
                    success_alert(res.message)
                    window.location.href = `/${topic}/ejemplos-de-codigo`
                }).catch(() => {
                    error_alert()
                })
            }
        })
    })
    
})