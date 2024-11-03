function createFormData(data, filesBool) {
    const formData = new FormData();

    data.forEach(obj => {
        const key = Object.keys(obj)[0];
        const value = obj[key];

        if (value !== undefined && value !== "") {
            if (filesBool && key === "files") {
                value.forEach(file => {
                    formData.append("files", file);
                });
            } else {
                formData.append(key, value);
            }
        }
    });

    return formData;
}

export default createFormData;