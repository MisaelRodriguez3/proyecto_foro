import { required_alert, warning_alert } from "./alerts.js"

export async function required_fields(values) {
    let nullField = false
    values.forEach(value => {
        if(value == "") {
            nullField = true;
        }
    });
    if(nullField) {
        return required_alert()
    }
}

export async function compare_two_fields(firstField, secondField, errorMessage) {
    if(firstField != secondField) {
        return warning_alert("Error", errorMessage)
    }
}

export function changeInFields(initialValues, finallyValues) {
    let data = []
    const no_data = ["", undefined, null, "None"]
    for (let i = 0; i < initialValues.length; i++) {
        const obj1 = initialValues[i];
        const obj2 = finallyValues[i];

        for(const key in obj1) {
            if(obj1[key] !== obj2[key] && !no_data.includes(obj2[key])) {
                data.push(obj2)
            }
        }
    }
    return data;
}