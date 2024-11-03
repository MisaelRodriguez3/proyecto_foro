import createFormData from "../utils/create_formData.js"
import { required_fields, changeInFields } from "../utils/validate_fields.js"
import { put_petition, delete_petition, post_petition } from "../service/api.js"
import { warning_alert, success_alert, error_alert, confirmation_alert } from "../utils/alerts.js"

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("editar")
    const delete_post = document.getElementById("eliminar")
    const do_comment = document.getElementById("comment-button")
    const edit_comment = document.getElementById("editar-comment")
    const delete_comment = document.getElementById("eliminar-comment")
    const form = document.querySelector(".ask-question-container")
    const comment_form = document.querySelector(".comment-form-container")
    const edit_comment_form = document.querySelector(".edit-comment-form-container")
    const close_icon = document.querySelector(".close-icon")
    const close_icon_comment = document.querySelector(".close-icon-comment")
    const close_icon_edit_comment = document.querySelector(".close-icon-edit-comment")
    const submit_button = document.querySelector(".save-changes")
    const submit_comment = document.querySelector(".save-comment")
    const submit_edit_comment = document.getElementById("save-comment-button")

    const post_Id = document.querySelector(".post").getAttribute("data-post")
    const topic = document.querySelector(".container").getAttribute("data-topic")

    const elementos = document.body.querySelectorAll("*")
    // boton de edicion
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

    // boton de responder
    if(do_comment) {
        do_comment.addEventListener("click", () => {
            comment_form.classList.add("active")
            elementos.forEach(elemento => {
                if(elemento !== comment_form && !comment_form.contains(elemento) && !elemento.contains(comment_form)) {
                    elemento.classList.add("deshabilitado")
                }
            })
        })
    }

    // boton de editar comentario
    if(edit_comment) {
        edit_comment.addEventListener("click", (e) => {
            edit_comment_form.setAttribute("data-comment-id", e.target.dataset.id)
            const txt = document.getElementById("edit-comentario")
            txt.value = e.target.dataset.value
            edit_comment_form.classList.add("active")
            elementos.forEach(elemento => {
                if(elemento !== edit_comment_form && !edit_comment_form.contains(elemento) && !elemento.contains(edit_comment_form)) {
                    elemento.classList.add("deshabilitado")
                }
            })
    
        })
    }

    // Cerrar cuestionario de edicion
    close_icon.addEventListener("click", () => {
        form.classList.remove("active")
        elementos.forEach(elemento => {
            elemento.classList.remove("deshabilitado");
        })
    })

    //Cerrar cuestionario de comentario
    close_icon_comment.addEventListener("click", () => {
        comment_form.classList.remove("active")
        elementos.forEach(elemento => {
            elemento.classList.remove("deshabilitado");
        })
    })

    // cerrar cuestionario de edicion de comentario
    close_icon_edit_comment.addEventListener("click", () => {
        edit_comment_form.classList.remove("active")
        elementos.forEach(elemento => {
            elemento.classList.remove("deshabilitado");
        })
    })

    const fields = form.querySelectorAll("input, textarea")
    const comment_field = comment_form.querySelector("textarea")
    const edit_comment_field = edit_comment_form.querySelector("textarea")

    fields.forEach(field => {
        field.addEventListener("input", (e) => {
            submit_button.classList.add("active")
        })
    })

    comment_field.addEventListener("input", () => {
        submit_comment.classList.add("active")
    })

    edit_comment_field.addEventListener("input", () => {
        submit_edit_comment.classList.add("active")
    })

    // Formulario de edicion de publicación
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

        // Validar campos requeridos
        const nullFields = await required_fields([titulo.value, descripcion.value])
        if (nullFields) return

        const initialData = [
            { titulo: title },
            { descripcion: description },
            { codigo: code }
        ]

        const finalData = [
            { titulo: titulo.value },
            { descripcion: descripcion.value },
            { codigo: codigo.value },
        ]

        const data = changeInFields(initialData, finalData)
    
        const formData = createFormData(data)

        put_petition("update-post", post_Id, formData).then(res => {
            if(res.status !== 200) {
                return warning_alert(res.message)
            }
            success_alert(res.message)
            window.location.reload()
        })
    })

    if(delete_post) {
        delete_post.addEventListener("click", () => {
            confirmation_alert("Eliminar publicación", "eliminar").then(result =>{
                if(result.isConfirmed) {
                    delete_petition("delete-post", post_Id).then(res => {
                        if(res.status !== 200) {
                            return warning_alert(res.message)
                        }
                        success_alert(res.message)
                        window.location.href = `/${topic}/foro`
                    }).catch(() => {
                        error_alert()
                    })
                }
            })
        })
    }

    //Formulario de comentarios
    comment_form.addEventListener("submit", async (e) => {
        e.preventDefault()

        // Campos del formulario
        const comment = document.getElementById("comentario").value

        const nullFields = await required_fields([comment])
        if (nullFields) return

        const data = [
            { comentario: comment },
            { post_Id: post_Id }
        ]
    
        const formData = createFormData(data)

        post_petition("add-comment", formData).then(res => {
            if (res.status !== 200) {
                return warning_alert(res.message)
            }
            success_alert(res.message)
            window.location.reload()
        }).catch(() => {
            error_alert()
        })
    })

    // formulario de edición de comentario
    edit_comment_form.addEventListener("submit", async (e) => {
        e.preventDefault()
        const edit_comentario = document.getElementById("edit-comentario").value
        const id = edit_comment_form.getAttribute("data-comment-id")

        const nullField = await required_fields([edit_comentario])
        if (nullField) return

        const data = createFormData([{comentario: edit_comentario}])

        put_petition("update-comment", id, data).then(res => {
            if(res.status !== 200) {
                return warning_alert(res.message)
            }
            success_alert(res.message)
            window.location.reload()
        }).catch(() => {
            error_alert()
        })

    })

    if(delete_comment) {
        delete_comment.addEventListener("click", (e) => {
            const id = e.target.dataset.id
            confirmation_alert("Se eliminara el comentario", "Eliminar").then(result => {
                if(result.isConfirmed) {
                    delete_petition("delete-comment", id).then(res => {
                        if(res.status !== 200) {
                            return warning_alert(res.message)
                        }
                        success_alert(res.message)
                        window.location.reload()
                    })
                }
            })
        })
    }
    
})