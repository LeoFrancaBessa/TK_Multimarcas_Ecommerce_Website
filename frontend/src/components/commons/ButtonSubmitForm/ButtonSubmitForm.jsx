import React from "react";
import './ButtonSubmitForm.css'

function ButtonSubmitForm({text}){
    return (
        <button className="button-submit-form" type="submit">{text}</button>
    )
}

export default ButtonSubmitForm