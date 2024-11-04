import {React, useState, useEffect} from "react";
import './SearchRecommendationsModal.css'
import {getClothingList} from '../../services/getClothingListService';
import ClothingThumbnail from '../commons/ClothingThumbnail/ClothingThumbnail';
import { Link } from "react-router-dom";

function SearchRecommendationsModal({isOpen, searchTerm, onClose}){
    const [searchedItens, setSearchedItens] = useState(null);

    useEffect(() => {
        async function fetchSearchedItems(){
            const data = await getClothingList({'name': searchTerm}, 4);
            setSearchedItens(data);
        }

        if (isOpen) fetchSearchedItems();
    }, [isOpen, searchTerm])

    if (!isOpen || searchTerm.length < 4) return null;

    return (
        <div className="recommendations-modal">
            <div className="recommendations-content">
                <p>Sugestões para "{searchTerm}"</p>
                <div className="searched-items-container">
                    {searchedItens ? searchedItens.map((items) => (
                        <div className="searched-items-flex-item" onClick={onClose}>
                            <ClothingThumbnail id={items.id} name={items.name} image={items.image} />
                            <p>{items.name}</p>
                            <p>R$ {items.price}</p>
                        </div>
                    )) : <p>Carregando...</p>}
                </div>
            </div>
        </div>
    )
}

export default SearchRecommendationsModal