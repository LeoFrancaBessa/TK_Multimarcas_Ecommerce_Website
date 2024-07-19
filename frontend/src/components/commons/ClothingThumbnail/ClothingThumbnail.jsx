import React from "react";
import './ClothingThumbnail.css';

function ClothingThumbnail({image}) {
    return (
        <div className='clothing-item-image'>
            <img src={image}></img>
        </div>  
    )
}

export default ClothingThumbnail