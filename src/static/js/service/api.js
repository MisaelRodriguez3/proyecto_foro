import { get_item } from "../utils/storage.js"

export async function get_petition(url_without_prefix) {
    try {        
        const response = await fetch(`/api/${url_without_prefix}`, {
            method: "GET"
        })

        return await response.json()
    } catch (error) {
        return console.error("Error en la petición: ",error);
    }
}

export async function post_petition(url_without_prefix, formData) {
    try {        
        const response = await fetch(`/api/${url_without_prefix}`, {
            method: "POST",
            body: formData
        })
        return await response.json()
    } catch (error) {
        return console.error("Error en la petición: ",error);
    }
}

export async function put_petition(url_without_prefix, id, formData) {
    try {        
        const response = await fetch(`/api/${url_without_prefix}/${id}`, {
            method: "PUT",
            body: formData
        })

        return await response.json()
    } catch (error) {
        return console.error("Error en la petición: ",error);
    }
}

export async function delete_petition(url_without_prefix, id) {
    try {        
        const response = await fetch(`/api/${url_without_prefix}/${id}`, {
            method: "DELETE",
        })

        return await response.json()
    } catch (error) {
        return console.error("Error en la petición: ",error);
    }
}