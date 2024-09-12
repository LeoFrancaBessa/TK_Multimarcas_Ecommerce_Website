import React from "react";
import './AccountModalLoggedUser.css';
import {useDispatch} from 'react-redux';
import { logout } from "../../services/authServices";
import { setLogout } from "../../redux/authSlice";

function AccountModalLoggedUser({isOpen, OnClose}){
    const dispatch = useDispatch();
    if (!isOpen) return null;

    async function handleSubmit(){
        await logout();
        dispatch(setLogout());
        window.location.reload();
        OnClose();
    }

    return (
        <div>
            <div className="account-modal-logged">
                <div className="account-modal-logged-items-container">
                    <ul class="menu-options">
                        <li><a href="#">Minha conta</a></li>
                        <li><a href="#">Meus pedidos</a></li>
                        <li onClick={handleSubmit}><a href="#">Sair</a></li>
                    </ul>
                </div>
            </div>
        </div>
    )
};

export default AccountModalLoggedUser;