import {React, useState} from "react";
import './AccountModalAnonymousUser.css'
import LoginModal from '../LoginModal/LoginModal'
import SignUpModal from "../SignUpModal/SignUpModal";

function AccountModal({isOpen}){
    const [isLoginModalOpen, setLoginModalOpen] = useState(false);
    const openLoginModal= () => setLoginModalOpen(true);
    const closeLoginModal = () => setLoginModalOpen(false);

    const [isSignUpModalOpen, setSignUpModalOpen] = useState(false);
    const openSignupModal = () => setSignUpModalOpen(true);
    const closeSignupModal = () => setSignUpModalOpen(false);

    if (!isOpen) return null;

    return (
        <div>
            <div className="account-modal-anonymous">
                <div className="account-modal-anonymous-items-container">
                    <div className="account-modal-anonymous-text-container">
                        <h6>entre ou cadastre-se</h6>
                        <p>Consulte seus pedidos, favoritos e conta:</p>
                    </div>
                    <div className="account-modal-anonymous-buttons-container">
                        <button class="account-modal-anonymous-botao-entrar" onClick={openLoginModal}>entrar</button>
                        <button class="account-modal-anonymous-botao-criar-conta" onClick={openSignupModal}>criar conta</button>
                    </div>
                </div>
            </div>
            <LoginModal isOpen={isLoginModalOpen} onClose={closeLoginModal}/>
            <SignUpModal isOpen={isSignUpModalOpen} onClose={closeSignupModal} onCloseLoginModal={closeLoginModal} />
        </div>
    )
}

export default AccountModal;