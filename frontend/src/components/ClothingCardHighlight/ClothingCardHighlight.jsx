import React, {useState} from "react";
import { Link } from "react-router-dom";
import './ClothingCardHighlight.css'
import heartFill from '../../assets/images/heartFill.png'
import heartOutline from '../../assets/images/heartOutline.png'
import { createFavorite, deleteFavorite } from "../../services/favoriteService";

function ClothingCardHighlight({id, image, favorite, clothing_name, clothing_price}){
    const [isFavorite, setFavorite] = useState(favorite)
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
    
    return (
        <div className="destaque" key={id}>
            <img src={image} alt="Roupa 1"></img>
            <Link to={`/roupa/${id}/${clothing_name}`}> <button className="btn-mais-detalhes">Mais Detalhes</button> </Link>
            <span className="favorite-heart">
            <img src={isFavorite ? heartFill : heartOutline} onClick={toggleFavorite}></img>
            </span>
            <div className="info">
                <div className="info-clothe-name">
                    <h3 className="clothe-name">{clothing_name}</h3>
                </div>
                <hr></hr>
                <p className="price">por <b>R$ {clothing_price}</b> à vista</p>
                <p className="price-parcelado">ou <b>3x de {clothing_price}</b> sem juros</p>
            </div>
        </div>
    )
}

export default ClothingCardHighlight