import React from "react";
import './ButtonSubmitForm.css'

function ButtonSubmitForm({text, onclick}){
    return (
        <button className="button-submit-form" onClick={onclick} type="submit">{text}</button>
    )
}

export default ButtonSubmitForm