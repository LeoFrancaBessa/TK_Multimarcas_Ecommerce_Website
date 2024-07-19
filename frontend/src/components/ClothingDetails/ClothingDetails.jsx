import {React, useEffect, useState} from "react";
import './ClothingDetails.css'
import heartFill from '../../assets/images/heartFill.png';
import heartOutline from '../../assets/images/heartOutline.png';
import { createFavorite, deleteFavorite } from "../../services/favoriteService";
import { addClothingCart } from "../../services/addClothingCart";
import SideModalCartItens from "../SideModalCartItens/SideModalCartItens";

function ClothingDetails({id, name, price, brand, images, sizes, colors, favorite}){
    const [isFavorite, setFavorite] = useState(favorite)
    const [mainImage, setMainImage] = useState(null);
    const [selectedColor, setSelectedColor] = useState(null);
    const [selectedSize, setSelectedSize] = useState(null);
    const [error, setError] = useState(null);
    const [isCartModalOpen, setCartModalOpen] = useState(false);
    
    const openCartModal= () => setCartModalOpen(true);
    const closeCartModal = () => setCartModalOpen(false);

    const toggleFavorite = () => {
        if (!isFavorite){
            createFavorite(id);
            setFavorite(true);
        }
        else{
            deleteFavorite(id);
            setFavorite(false);
        }
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError(null);
        const [data, ok] = await addClothingCart(id, selectedSize, selectedColor);
        if (!ok){
            setError(data.message);
        }
        else{
            openCartModal();
        }
    }

    useEffect(() => {
        if (images && images.length > 0){
            setMainImage(images[0].image);
        }

        if(favorite !== undefined){
            setFavorite(favorite)
        }
    }, [images, favorite]);


    return (
        <section className="clothing-details">
        <div className="thumbnail-images">
            {images ? images.map(items => (<img src={items.image} alt="Miniatura 2" className="thumbnail" onClick={() => setMainImage(items.image)}></img>)) : 'Carregando...'}
        </div>

        <div className="main-image">
            <img src={mainImage} alt="Nome da Roupa"></img>
        </div>

        <div className="clothing-info-container">
            <div className="clothing-title-container">
                <div className="clothing-title">
                    <h2>{name}</h2>
                    <p>Marca: <b>{brand}</b></p>
                </div>
                <div className="clothing-title-heart">
                    <img src={isFavorite ? heartFill : heartOutline} onClick={toggleFavorite}></img>
                </div>
            </div>

            <div className="additional-info">
                <p className="price-info">por <b>{`R$ ${price}`}</b> à vista</p>
                <p>{`ou 3x de ${price} sem juros`}</p>

                <p className="color-title">Cor</p>
                <div className="color-selection">
                    {colors ? colors.map(items => 
                                        (<div className={items.id === selectedColor ? 'color-border-selected' : 'color-border'} onClick={() => setSelectedColor(items.id)} id={items.id}>
                                        <div className="color-option" style={{backgroundColor : items.color}}></div>
                                        </div>)) : 'Carregando...'}
                </div>

                <p className="size-title">Tamanho</p>
                <div className="size-container">
                    {sizes ? sizes.map(items => (
                        <div className={items.id === selectedSize ? 'size-border-selected' : 'size-border'} onClick={() => setSelectedSize(items.id)} id={items.id}>
                            <p className="size-option">{items.size}</p>
                        </div>
                    )) : 'Carregando'}
                </div>
            </div>

            <button id="buyButton" className="buy-button" onClick={handleSubmit}>Adicionar à sacola</button>
            <p className="add-clothing-error">{error}</p>
            <p className="frete-title"> Consulte o Frete <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-truck" viewBox="0 0 16 16">
                <path d="M0 3.5A1.5 1.5 0 0 1 1.5 2h9A1.5 1.5 0 0 1 12 3.5V5h1.02a1.5 1.5 0 0 1 1.17.563l1.481 1.85a1.5 1.5 0 0 1 .329.938V10.5a1.5 1.5 0 0 1-1.5 1.5H14a2 2 0 1 1-4 0H5a2 2 0 1 1-3.998-.085A1.5 1.5 0 0 1 0 10.5zm1.294 7.456A2 2 0 0 1 4.732 11h5.536a2 2 0 0 1 .732-.732V3.5a.5.5 0 0 0-.5-.5h-9a.5.5 0 0 0-.5.5v7a.5.5 0 0 0 .294.456M12 10a2 2 0 0 1 1.732 1h.768a.5.5 0 0 0 .5-.5V8.35a.5.5 0 0 0-.11-.312l-1.48-1.85A.5.5 0 0 0 13.02 6H12zm-9 1a1 1 0 1 0 0 2 1 1 0 0 0 0-2m9 0a1 1 0 1 0 0 2 1 1 0 0 0 0-2"/>
              </svg></p>
              
            <div className="cpfContainer">
                <input className="cpfInput" type="text" name="" id=""></input>
                <button className="cpfButton">Calcular</button>
            </div>

        </div>
    <SideModalCartItens isOpen={isCartModalOpen} onClose={closeCartModal} />
    </section>
    )
}

export default ClothingDetails