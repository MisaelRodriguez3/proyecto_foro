export function save_item(key, value) {
    key.toString()
    value.toString()
    localStorage.setItem(key, value)
}

export function get_item(key) {
    key.toString()
    const item = localStorage.getItem(key)
    return item
}

export function clear_storage() {
    localStorage.clear();
}