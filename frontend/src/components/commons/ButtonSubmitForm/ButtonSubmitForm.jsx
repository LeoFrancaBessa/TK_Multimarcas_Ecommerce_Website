import React from "react";
import './ButtonSubmitForm.css'

function ButtonSubmitForm({text, onclick}){
    return (
        <button className="button-submit-form" onClick={onclick}>{text}</button>
    )
}

export default ButtonSubmitForm