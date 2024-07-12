import React, {useState} from "react";
import './SignUpModal.css'
import FormLabelsInput from "../commons/FormLabelsInput/FormLabelsInput";
import ButtonSubmitForm from "../commons/ButtonSubmitForm/ButtonSubmitForm";
import { signup } from "../../services/signupService";

function SignUpModal({isOpen, onClose, onCloseLoginModal}){
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError('');
        const [data, ok] = await signup(email, name, password1, password2);
        if (!ok){
            setError(data.message[0]);
        }
        else{
            onClose();
            onCloseLoginModal();
        }
    }

    if(!isOpen){
        return null
    }

    return (
        <div className="signup-modal">
            <div className="signup-modal-content">
                <button className="signup-modal-close" onClick={onClose}>&times;</button>
                <form className="signup-form" method="post">
                    <FormLabelsInput id_element={"id_name"} label={"Nome"} type={"text"} value={name} onChange={(e) => setName(e.target.value)} width={"98%"}/>
                    <FormLabelsInput id_element={"id_signup_email"} label={"Email"} type={"email"} value={email} onChange={(e) => setEmail(e.target.value)} width={"98%"}/>
                    <FormLabelsInput id_element={"id_password1"} label={"Senha"} type={"password"} value={password1} onChange={(e) => setPassword1(e.target.value)} width={"98%"}/>
                    <FormLabelsInput id_element={"id_password2"} label={"Repita sua senha"} type={"password"} value={password2} onChange={(e) => setPassword2(e.target.value)} width={"98%"}/>
                    <ButtonSubmitForm text={"Cadastrar"} onclick={handleSubmit}/>
                    <p className="signup-form-error">{error}</p>
                </form>
            </div>
        </div>
    )
}

export default SignUpModal;