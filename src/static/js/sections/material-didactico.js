import createFormData from "../utils/create_formData.js"
import { required_fields } from "../utils/validate_fields.js"

document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("add-material")
    const form = document.querySelector(".upload-material-container")
    const close_icon = document.querySelector(".close-icon")
    const submit_button = document.querySelector(".save-changes")
    const material_type = document.getElementById("tipo")
    const material_file = document.querySelector(".material-file")
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
    let file;
    let doc;
    
    material_type.addEventListener("change", (e) => {
        material_file.innerHTML = ""
        if(e.target.value === "link") {
            file = false
            material_file.innerHTML += `
                <label for="link">Enlace</label>
                <input type="text" name="link" id="link" value="" data-link="">
            `;
        } else if (e.target.value === "archivo"){
            file = true
            material_file.innerHTML += `
                <label for="archivo">Archivo</label>
                <input type="file" name="archivo" id="archivo" class="input-file" accept=".png, .jpg, .jpeg, .pdf, .doc, .docx, .ppt">
            `
            const archivo = document.getElementById("archivo")
            archivo.addEventListener("change", (e) => {
                doc = e.target.files[0]
            })
        }
    })

    form.addEventListener("submit", async (e) => {
        e.preventDefault()

        // Campos del formulario
        const titulo = document.getElementById("titulo").value
        const descripcion = document.getElementById("descripcion").value
        const material = file ? doc : document.getElementById("link").value

        const nullFields = await required_fields([titulo, descripcion, material])
        if (nullFields) return

        const data = [
            { titulo: titulo },
            { descripcion: descripcion },
            { material: material }
        ]
    
        const formData = createFormData(data, file)
        console.log(data)
        for (let [key, value] of formData.entries()) {
            console.log(key, value);
        }
    })

})