import {React, useState } from "react";
import './AccountOptions.css'
import AccountModal from "../../AccountModal/AccountModal";

function AccountOptions(){
    const [isAccountModalOpen, setIsAccountModalOpen] = useState(false);

    const openAccountModal = () => setIsAccountModalOpen(true);
    const closeAccountModal = () => setIsAccountModalOpen(false);

    return (
        <div className="account-options-container">
            <div className="account-options" onClick={openAccountModal} onBlur={closeAccountModal}>
                <div className="account-options-text">
                    <p>Minha conta e</p>
                    <p><b>Meus pedidos</b></p>
                </div>
                <a href="#"><svg width="24" height="24" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" className="cea-cea-store-theme-0-x-header-login__icon"><path d="M42 42C42 39.8988 41.5344 37.8183 40.6298 35.8771C39.7252 33.9359 38.3994 32.172 36.7279 30.6863C35.0565 29.2006 33.0722 28.022 30.8883 27.2179C28.7044 26.4139 26.3638 26 24 26C21.6362 26 19.2956 26.4139 17.1117 27.2179C14.9278 28.022 12.9435 29.2006 11.2721 30.6863C9.60062 32.172 8.27475 33.9359 7.37017 35.8771C6.46558 37.8183 6 39.8988 6 42" stroke="#212B36" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"></path><circle cx="24" cy="16" r="10" stroke="#212B36" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"></circle></svg></a>
                </div>
            <AccountModal isOpen={isAccountModalOpen} />
        </div>
    )
}

export default AccountOptions