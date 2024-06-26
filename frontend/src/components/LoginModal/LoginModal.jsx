import React, {useState} from "react";
import './LoginModal.css'
import FormLabelsInput from '../commons/FormLabelsInput/FormLabelsInput'
import ButtonSubmitForm from '../commons/ButtonSubmitForm/ButtonSubmitForm'
import SignUpModal from "../SignUpModal/SignUpModal";

function LoginModal({isOpen, onClose}){
    const [isSignUpModalOpen, setSignUpModalOpen] = useState(false);

    const openSignupModal = () => setSignUpModalOpen(true);
    const closeSignupModal = () => setSignUpModalOpen(false)

    if(!isOpen){
        return null
    }

    return (
        <div>
            <div className="login-modal">
                <div className="login-modal-content">
                    <button className="login-modal-close" onClick={onClose}>&times;</button>
                    <form className="login-form" method="post">
                        <FormLabelsInput id_element={"id_email"} label={"Email"} type={"email"}/>
                        <FormLabelsInput id_element={"id_password"} label={"Senha"} type={"password"}/>
                        <ButtonSubmitForm text={"Entrar"}/>
                    </form>
                    <p>Ainda não tem uma conta? <a href="#" onClick={openSignupModal}>Cadastre-se</a></p>
                </div>
            </div>
        <SignUpModal isOpen={isSignUpModalOpen} onClose={closeSignupModal} />
        </div>
    )
}

export default LoginModal