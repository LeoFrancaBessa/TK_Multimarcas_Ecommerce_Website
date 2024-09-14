import {React, useEffect, useState} from "react";
import './SideModalFavorites.css'
import ClothingThumbnail from "../commons/ClothingThumbnail/ClothingThumbnail";
import {getFavorites} from '../../services/getFavoritesService'
import {deleteFavorite} from '../../services/favoriteService'

function SideModalFavorites({isOpen, onClose}){
    const [favorites, setFavorites] = useState(null);
    const [itensCount, setItensCount] = useState(0);
    const [isUpdateFavorites, setIsUpdatedFavorites] = useState(false);

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

    //Update favorites
    useEffect(() => {
        async function fetchFavorites(){
            const data = await getFavorites();
            setFavorites(data);
            setItensCount(data ? data.length : 0);
        }

        if (isOpen) fetchFavorites();
    }, [isOpen, isUpdateFavorites]);

    //Handle delete item from cart
    const handleDeleteFavoritesItem = async function(clothingId){
        await deleteFavorite(clothingId);
        setIsUpdatedFavorites(!isUpdateFavorites);
    }

    if(!isOpen) return null;

    if(!favorites) return null;

    return (
        <>
        <div className="favorites-modal-overlay" onClick={onClose}></div>
        <div className="favorites-side-modal open">
            <div className="favorites-side-modal-content">
                <button className="favorites-modal-close-button" onClick={onClose}>
                    &times;
                </button>
                <div className="favorites-modal-top-section">
                    <p className='resume'>Favoritos</p>
                    <p className='count-info'>Você possui {itensCount} {itensCount == 1 ? 'favorito' : 'favoritos'}</p>
                    
                    <div className='favorites-items'>
                    {favorites.map((item) => (
                        <div className='clothing-item-container' key={item.id}>
                            <ClothingThumbnail id={item.clothing.id} name={item.clothing.name} image={item.clothing.image} />
                            <div className='clothing-item-info'>
                                <p className='clothing-item-title'>{item.clothing.name}</p>
                                <p className='clothing-item-price'>R$ {item.clothing.price}</p>
                                <div className='clothing-item-update'>
                                    <a href="#" onClick={() => handleDeleteFavoritesItem(item.clothing.id)}><i className="material-icons">delete_outline</i></a>
                                </div>
                            </div>
                        </div>
                    ))}
                    </div>
                </div>
            </div>
        </div>
      </>
    )
}

export default SideModalFavorites