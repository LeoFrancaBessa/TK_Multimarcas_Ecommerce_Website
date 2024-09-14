import React from "react";
import './ClothingThumbnail.css';
import { Link } from "react-router-dom";

function ClothingThumbnail({id, name, image}) {
    return (
        <Link style={{textDecoration: 'none'}} to={`/roupa/${id}/${name}`}>
            <div className='clothing-item-image'>
                <img src={image}></img>
            </div>
        </Link>  
    )
}

export default ClothingThumbnail