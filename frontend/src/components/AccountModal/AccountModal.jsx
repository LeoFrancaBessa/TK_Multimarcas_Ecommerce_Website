import {React, useState} from "react";
import './AccountModal.css'

function AccountModal({isOpen}){
    if (!isOpen) return null;

    return (
        <div className="account-modal">
            <p>aaaaaaaaa</p>
        </div>
    )
}

export default AccountModal