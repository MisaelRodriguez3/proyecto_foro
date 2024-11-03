function see_password(inputID, iconID) {
    const input = document.getElementById(inputID);
    const icon = document.getElementById(iconID);

    icon.addEventListener("click", () => {
        const actual_type = input.getAttribute("type");

        if(actual_type === "password") {
            input.setAttribute("type", "text");
        } else {
            input.setAttribute("type", "password")
        }
    })
}

export default see_password;