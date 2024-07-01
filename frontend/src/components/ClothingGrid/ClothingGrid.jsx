import React, {useState, useEffect} from "react";
import './ClothingGrid.css'
import ClothingCardHighlight from '../ClothingCardHighlight/ClothingCardHighlight'
import { getClothingList } from "../../services/getClothingListService";

function ClothingGrid(){
    const [clothingList, setClothingList] = useState([]);

    useEffect(() => {
        async function fetchClothingList() {
            const data = await getClothingList();
            setClothingList(data);
        }

        fetchClothingList();
    }, []);

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