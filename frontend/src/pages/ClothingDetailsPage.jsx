import {React, useEffect, useState} from "react";
import { useParams } from "react-router-dom";
import FirstHeader from '../components/headers/FirstHeader/FirstHeader'
import SecondHeader from '../components/headers/SecondHeader/SecondHeader';
import Footer from '../components/Footer/Footer';
import { getClothingDetail } from "../services/getClothingDetail";
import ClothingDetails from "../components/ClothingDetails/ClothingDetails";
import { setLogin, setLogout } from "../redux/authSlice";
import {useDispatch} from 'react-redux'
import {checkUserAuth} from '../services/checkUserAuthService'

function ClothingDetail(){
    const {clothingID} = useParams();
    const [clothingData, setClothingData] = useState({})

    const dispatch = useDispatch();
    //Check if user is logged in everytime that the pages loads or if the user logged of unlogged
    useEffect(() => {
        async function handleCheckAuth(){
            const response = await checkUserAuth();
            const isAuth = response.authenticated;
            if (isAuth){
                dispatch(setLogin());
            }
            else{
                dispatch(setLogout());
            }
        }

        handleCheckAuth();
    });

    useEffect(() => {
        async function fetchClothingDetail() {
            const data = await getClothingDetail(clothingID);
            setClothingData(data);
        }

        fetchClothingDetail();
    }, [clothingID]);

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