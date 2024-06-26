import React from "react";
import './SignUpModal.css'
import FormLabelsInput from "../commons/FormLabelsInput/FormLabelsInput";
import ButtonSubmitForm from "../commons/ButtonSubmitForm/ButtonSubmitForm";

function SignUpModal({isOpen, onClose}){
    if(!isOpen){
        return null
    }

    return (
        <div className="signup-modal">
            <div className="signup-modal-content">
                <button className="signup-modal-close" onClick={onClose}>&times;</button>
                <form className="signup-form" method="post">
                    <FormLabelsInput id_element={"id_name"} label={"Nome"} type={"text"}/>
                    <FormLabelsInput id_element={"id_last_name"} label={"Sobrenome"} type={"text"}/>
                    <FormLabelsInput id_element={"id_signup_email"} label={"Email"} type={"email"}/>
                    <FormLabelsInput id_element={"id_password1"} label={"Senha"} type={"password"}/>
                    <FormLabelsInput id_element={"id_password2"} label={"Repita sua senha"} type={"password"}/>
                    <ButtonSubmitForm text={"Cadastrar"}/>
                </form>
            </div>
        </div>
    )
}

export default SignUpModal;