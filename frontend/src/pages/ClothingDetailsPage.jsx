import {React, useEffect, useState} from "react";
import { useParams } from "react-router-dom";
import FirstHeader from '../components/headers/FirstHeader/FirstHeader'
import SecondHeader from '../components/headers/SecondHeader/SecondHeader';
import Footer from '../components/Footer/Footer';
import { getClothingDetail } from "../services/getClothingDetail";
import ClothingDetails from "../components/ClothingDetails/ClothingDetails";

function ClothingDetail(){
    const {clothingID} = useParams();
    const [clothingData, setClothingData] = useState({})

    useEffect(() => {
        async function fetchClothingDetail() {
            const data = await getClothingDetail(clothingID);
            setClothingData(data);
        }

        fetchClothingDetail();
    }, []);

    return (
        <div className="App">
            <FirstHeader phone={"(98) 98419-0129"} email={"tkmultimarcas@gmail.com"}/>
            <SecondHeader/>
            <ClothingDetails id={clothingData.id} name={clothingData.name} price={clothingData.price} 
            gender={clothingData.gender} brand={clothingData.brand} images={clothingData.images} sizes={clothingData.sizes}
            colors={clothingData.colors} favorite={clothingData.favorite} />
            <Footer/>
        </div>
    )
}

export default ClothingDetail