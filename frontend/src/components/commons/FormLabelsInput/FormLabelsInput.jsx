import React from "react";
import './FormLabelsInput.css'

function FormLabelsInput({id_element, label, type, value, onChange}){
    return (
            <div className="form-label-input">
                <label>{label}:</label>
                <input type={type} id={id_element} name={id_element} value={value} onChange={onChange}></input>
            </div>
    )
}

export default FormLabelsInput