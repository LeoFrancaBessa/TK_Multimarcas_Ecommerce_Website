import {React, useEffect, useState } from 'react';
import './SideModalCartItens.css';
import { getCartItens } from '../../services/getCartItensService';

function SideModalCartItens({isOpen, onClose}){
    const [cartItens, setCartItens] = useState(null);

    useEffect(() => {
        if (isOpen){
            document.body.classList.add('modal-open');
        }
        else{
            document.body.classList.remove('modal-open');
        }

        return () => {
            document.body.classList.remove('modal-open');
        }
    }, [isOpen]);

    useEffect(() => {
        async function fetchCartItens(){
            const data = await getCartItens();
            setCartItens(data);
        }

        if (isOpen) fetchCartItens();
    }, [isOpen]);

    if(!isOpen) return null

    return(
        <>
        <div className="cart-modal-overlay" onClick={onClose}></div>
        <div className="cart-side-modal open">
          <div className="cart-side-modal-content">
            <button className="cart-modal-close-button" onClick={onClose}>
              &times;
            </button>
            <div className="cart-modal-top-section">
              <p>Resumo da sua sacola</p>
            </div>
            <div className="cart-modal-bottom-section">
              <h2>Bottom Section</h2>
              <p>Content for the bottom section...</p>
            </div>
          </div>
        </div>
      </>
    )
}

export default SideModalCartItens