import React from "react";
import './FormLabelsInput.css'

function FormLabelsInput({id_element, label, type, value, onChange, width}){
    const style = {
        width : width
    }

    return (
            <div className="form-label-input">
                <label>{label}:</label>
                <input type={type} id={id_element} name={id_element} value={value} onChange={onChange} style={style}></input>
            </div>
    )
}

export default FormLabelsInput