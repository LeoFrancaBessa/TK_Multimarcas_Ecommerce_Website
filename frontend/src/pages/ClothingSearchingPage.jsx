import {React, useEffect, useState} from "react";
import { useParams } from "react-router-dom";
import FirstHeader from '../components/headers/FirstHeader/FirstHeader';
import ClothingGrid from "../components/ClothingGrid/ClothingGrid";
import SectionsTitle from "../components/commons/SectionsTitle/SectionsTitle";
import SecondHeader from '../components/headers/SecondHeader/SecondHeader';
import Footer from '../components/Footer/Footer';

function ClothingSearchingPage(){
    const {clothingTitle} = useParams();

    return (
        <div className="App">
            <FirstHeader phone={"(98) 98419-0129"} email={"tkmultimarcas@gmail.com"}/>
            <SecondHeader/>
            <SectionsTitle text={`Resultados para "${clothingTitle}"`} />
            <ClothingGrid filters={{global: clothingTitle}} />
            <Footer/>
        </div>
    )
}

export default ClothingSearchingPage