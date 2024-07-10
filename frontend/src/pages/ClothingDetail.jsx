import {React, useEffect, useState} from "react";
import { useParams } from "react-router-dom";
import FirstHeader from '../components/headers/FirstHeader/FirstHeader'
import SecondHeader from '../components/headers/SecondHeader/SecondHeader';
import Footer from '../components/Footer/Footer';
import { getClothingDetail } from "../services/getClothingDetail";

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
            <Footer/>
        </div>
    )
}

export default ClothingDetail