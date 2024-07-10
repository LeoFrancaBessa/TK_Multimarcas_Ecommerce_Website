import React from "react";
import FirstHeader from '../components/headers/FirstHeader/FirstHeader'
import SecondHeader from '../components/headers/SecondHeader/SecondHeader';
import SectionsTitle from '../components/commons/SectionsTitle/SectionsTitle';
import ClothingGrid from '../components/ClothingGrid/ClothingGrid';
import SectionsGrid from '../components/SectionsGrid/SectionsGrid';
import Footer from '../components/Footer/Footer';
import model1 from '../../src/assets/images/model1.jpg';
import model2 from '../../src/assets/images/model2.jpg';
import model3 from '../../src/assets/images/model3.jpg';

function Home(){
    return (
        <div className="App">
            <FirstHeader phone={"(98) 98419-0129"} email={"tkmultimarcas@gmail.com"}/>
            <SecondHeader/>
            <SectionsTitle text={"Mais Vendidos"} />
            <ClothingGrid/>
            <SectionsTitle text={"Explorar Sessões"} />
            <SectionsGrid sectionImage1={model1} sectionImage2={model2} sectionImage3={model3} />
            <SectionsTitle text={"Ofertas Imperdíveis"} />
            <ClothingGrid/>
            <Footer/>
        </div>
    )
}

export default Home