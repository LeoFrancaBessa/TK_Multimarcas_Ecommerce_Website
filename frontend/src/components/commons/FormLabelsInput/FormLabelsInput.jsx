import React from "react";
import './FormLabelsInput.css'

function FormLabelsInput({id_element, label, type}){
    return (
            <div className="form-label-input">
                <label>{label}:</label>
                <input type={type} id={id_element} name={id_element}></input>
            </div>
    )
}

export default FormLabelsInput