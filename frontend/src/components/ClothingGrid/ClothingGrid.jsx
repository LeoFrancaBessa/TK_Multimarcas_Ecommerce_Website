import React, {useState, useEffect} from "react";
import './ClothingGrid.css'
import ClothingCardHighlight from '../ClothingCardHighlight/ClothingCardHighlight'
import { getClothingList } from "../../services/getClothingListService";


function ClothingGrid({filters}){
    const [clothingList, setClothingList] = useState([]);

    // No futuro, cada chamada aqui representará um tipo de roupa diferente: mais vendidas, favoritas, promoções, etc...
    useEffect(() => {
        async function fetchClothingList() {
            const data = await getClothingList(filters);
            setClothingList(data);
        }

        fetchClothingList();
    }, [filters]);

    return (
        <div className="grid-destaque-container">
            <div className="grid-destaque">
                {clothingList.map((clothing) => (
                    <ClothingCardHighlight id={clothing.id} image={clothing.image} favorite={clothing.favorite} clothing_name={clothing.name} clothing_price={clothing.price} />
                ))}
            </div>
        </div>
    )
}

export default ClothingGrid;