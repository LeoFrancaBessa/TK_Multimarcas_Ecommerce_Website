import React, {useState} from "react";
import './LoginModal.css'
import FormLabelsInput from '../commons/FormLabelsInput/FormLabelsInput'
import ButtonSubmitForm from '../commons/ButtonSubmitForm/ButtonSubmitForm'
import SignUpModal from "../SignUpModal/SignUpModal";
import {useDispatch} from 'react-redux';
import {login} from '../../services/authServices';
import { setLogin } from "../../redux/authSlice";


function LoginModal({isOpen, onClose}){
    const [isSignUpModalOpen, setSignUpModalOpen] = useState(false);
    const openSignupModal = () => setSignUpModalOpen(true);
    const closeSignupModal = () => setSignUpModalOpen(false);

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const dispatch = useDispatch();

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError('');
        const [data, ok] = await login(username, password);
        if (!ok){
            setError(data.message[0]);
        }
        else{
            dispatch(setLogin());
            onClose();
        }
    }

    if(!isOpen) return null

    return (
        <div>
            <div className="login-modal">
                <div className="login-modal-content">
                    <button className="login-modal-close" onClick={onClose}>&times;</button>
                    <form className="login-form" method="post">
                        <FormLabelsInput id_element={"id_email"} label={"Email"} type={"email"} value={username} onChange={(e) => setUsername(e.target.value)} width={"100%"}/>
                        <FormLabelsInput id_element={"id_password"} label={"Senha"} type={"password"} value={password} onChange={(e) => setPassword(e.target.value)} width={"100%"}/>
                        <ButtonSubmitForm text={"Entrar"} onclick={handleSubmit}/>
                        <p className="login-form-error">{error}</p>
                    </form>
                    <p>Ainda não tem uma conta? <a href="#" onClick={openSignupModal}>Cadastre-se</a></p>
                </div>
            </div>
        <SignUpModal isOpen={isSignUpModalOpen} onClose={closeSignupModal} onCloseLoginModal={onClose} />
        </div>
    )
}

export default LoginModal