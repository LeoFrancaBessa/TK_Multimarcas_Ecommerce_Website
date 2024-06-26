import React, {useState} from "react";
import './LoginModal.css'
import FormLabelsInput from '../commons/FormLabelsInput/FormLabelsInput'
import ButtonSubmitForm from '../commons/ButtonSubmitForm/ButtonSubmitForm'
import SignUpModal from "../SignUpModal/SignUpModal";
import {login} from '../../services/authServices';

function LoginModal({isOpen, onClose}){
    const [isSignUpModalOpen, setSignUpModalOpen] = useState(false);
    const openSignupModal = () => setSignUpModalOpen(true);
    const closeSignupModal = () => setSignUpModalOpen(false);

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    if(!isOpen){
        return null
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError('');
        const data = await login(username, password);
        if ('message' in data){
            setError(data.message);
        }
        else{
            onClose();
        }
    }

    return (
        <div>
            <div className="login-modal">
                <div className="login-modal-content">
                    <button className="login-modal-close" onClick={onClose}>&times;</button>
                    <form className="login-form" method="post">
                        <FormLabelsInput id_element={"id_email"} label={"Email"} type={"email"} value={username} onChange={(e) => setUsername(e.target.value)}/>
                        <FormLabelsInput id_element={"id_password"} label={"Senha"} type={"password"} value={password} onChange={(e) => setPassword(e.target.value)}/>
                        <ButtonSubmitForm text={"Entrar"} onclick={handleSubmit}/>
                        <p className="login-form-error">{error}</p>
                    </form>
                    <p>Ainda não tem uma conta? <a href="#" onClick={openSignupModal}>Cadastre-se</a></p>
                </div>
            </div>
        <SignUpModal isOpen={isSignUpModalOpen} onClose={closeSignupModal} />
        </div>
    )
}

export default LoginModal