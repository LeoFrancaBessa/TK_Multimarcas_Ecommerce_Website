import React from "react";
import './LoginModal.css'
import FormLabelsInput from '../commons/FormLabelsInput/FormLabelsInput'
import ButtonSubmitForm from '../commons/ButtonSubmitForm/ButtonSubmitForm'

function LoginModal({isOpen, onClose}){
    if(!{isOpen}){
        return null
    }

    return (
        <div class="login-modal">
            <div class="login-modal-content">
                <button class="login-modal-close" onclick={onClose}>X</button>
                <form class="login-form" method="post">
                    <FormLabelsInput id_element={"id_username"} label={"Usuário"} type={"text"}/>
                    <FormLabelsInput id_element={"id_password"} label={"Senha"} type={"password"}/>
                    <ButtonSubmitForm text={"Entrar"}/>
                </form>
                <p>Ainda não tem uma conta? <a href="#" onclick="">Cadastre-se</a></p>
            </div>
        </div>
    )
}

export default LoginModal