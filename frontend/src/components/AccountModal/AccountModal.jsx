import React from "react";
import './AccountModal.css'

function AccountModal({isOpen}){

    if (!isOpen) return null;

    console.log('aaaaa');

    return (
        <div className="account-modal">
            <div className="account-modal-content">
                <div className="account-modal-items-container">
                    <p>aaaaa</p>
                </div>
            </div>
        </div>
    )
}

export default AccountModal;