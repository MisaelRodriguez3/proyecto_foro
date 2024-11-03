export function success_alert(message) {
    return Swal.fire({
        icon: "success",
        title: message,
        showConfirmButton: false,
        timer: 1200
      });
}

export function warning_alert(title, message) {
    return Swal.fire({
        icon: "warning",
        title: title,
        text: message
      });
}

export function confirmation_alert(title, action) {
    return Swal.fire({
        title: '¿Estás seguro?',
        title: title,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: `¡Si, ${action}!`
      })
}

export function required_alert() {
    return Swal.fire({
        icon: "warning",
        title: "Oops...",
        text: "¡Completa los campos necesarios!",
      });
}

export function error_alert() {
    return Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "¡Algo salió mal!",
      });
}