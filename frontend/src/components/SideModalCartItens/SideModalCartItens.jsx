import {React, useEffect, useState } from 'react';
import './SideModalCartItens.css';
import { getCartItens } from '../../services/getCartItensService';
import { updateClothingCartItem, deleteClothingCartItem } from '../../services/updateClothingCart';
import ButtonSubmitForm from '../commons/ButtonSubmitForm/ButtonSubmitForm';
import ClothingThumbnail from '../commons/ClothingThumbnail/ClothingThumbnail';


function SideModalCartItens({isOpen, onClose}){
    const [cart, setCart] = useState(null);
    const [itensCount, setItensCount] = useState(0);
    const [isUpdateCart, setIsUpdatedCart] = useState(false);

    //Hide scrollbar
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

    //Update cart
    useEffect(() => {
        async function fetchCartItens(){
            const data = await getCartItens();
            setCart(data);
            setItensCount(data.cartItems ? data.cartItems.length : 0);
        }

        if (isOpen) fetchCartItens();
    }, [isOpen, isUpdateCart]);

    //Handle item quantity options
    const optionsArray = Array.from({length:10}, (_, index) => index + 1)
    const handleUpdateQuantity = (cartItemId) => async (event) => {
        await updateClothingCartItem(cartItemId, event.target.value);
        setIsUpdatedCart(!isUpdateCart);
    }

    //Handle delete item from cart
    const handleDeleteCartItem = async function(cartItemId){
        await deleteClothingCartItem(cartItemId);
        setIsUpdatedCart(!isUpdateCart);
    }

    if(!isOpen) return null;

    if(!cart) return null;

    return(
        <>
        <div className="cart-modal-overlay" onClick={onClose}></div>
        <div className="cart-side-modal open">
          <div className="cart-side-modal-content">
            <button className="cart-modal-close-button" onClick={onClose}>
              &times;
            </button>
            <div className="cart-modal-top-section">
              <p className='resume'>Resumo da sua sacola</p>
              <p className='count-info'>Sua sacola possui {itensCount} {itensCount == 1 ? 'item' : 'itens'}</p>
              
              <div className='cart-items'>
                {cart.cartItems.map((item) => (
                    <div className='clothing-item-container' key={item.id}>
                        <ClothingThumbnail id={item.clothing.id} name={item.clothing.name} image={item.clothing.image} />
                        <div className='clothing-item-info'>
                            <p className='clothing-item-title'>{item.clothing.name}</p>
                            <p className='clothing-item-price'>R$ {item.clothing.price}</p>
                            <p className='clothing-item-size'>Tamanho: {item.size.size}</p>
                            <p className='clothing-item-color'>Cor:  {item.color.color}</p>
                            <div className='clothing-item-update'>
                                <select className='clothing-item-quantity' onChange={handleUpdateQuantity(item.id)}>
                                    {optionsArray.map((quantity) => (
                                        <option value={quantity} selected={item.quantity == quantity}>{quantity}</option>
                                    ))}
                                </select>
                                <a href="#" onClick={() => handleDeleteCartItem(item.id)}><i className="material-icons">delete_outline</i></a>
                            </div>
                        </div>
                    </div>
                ))}
              </div>
            
            </div>
            <div className="cart-modal-bottom-section">
              <div className='cart-total-price'>
                <h4>Total</h4>
                <p>R$ {cart.price}</p>
              </div>
              <div className='cart-confirm-section'>
                <p>Você poderá <b>calcular o frete</b> e visualizar mais benefícios ao <b>Fechar o pedido</b></p>
                <ButtonSubmitForm text={'Fechar o pedido'} />
              </div>
            </div>
          </div>
        </div>
      </>
    )
}

export default SideModalCartItens