import React, {useState} from "react";
import './SecondHeader.css'
import logo from '../../../assets/images/main_logo.png';
import CategoriesLinks from '../../commons/CategoriesLinks/CategoriesLinks'
import SearchBar from "../../SearchBar/SearchBar";
import ButtonIcons from '../../commons/ButtonIcons/ButtonIcons'
import UsersOptions from "../../commons/UserOptions/UsersOptions";
import AccountOptions from "../../AccountOptions/AccountOptions";
import SideModalCartItens from "../../SideModalCartItens/SideModalCartItens";


function SecondHeader(){
    const [isCartModalOpen, setCartModalOpen] = useState(false);
    const openCartModal= () => setCartModalOpen(true);
    const closeCartModal = () => setCartModalOpen(false);

    return (
        <div>
            <header className="second-header">
            <div className="logo-container">
                <img src={logo}/>
            </div>
            <div className="clothing-options-container">
                <CategoriesLinks text={'Masculina'} link={"#"}/> 
                <CategoriesLinks text={'Feminina'} link={"#"}/> 
                <CategoriesLinks text={'Infantil'} link={"#"}/> 
                <CategoriesLinks text={'Esportes'} link={"#"}/> 
                <CategoriesLinks text={'Lançamentos'} link={"#"}/> 
                <CategoriesLinks text={'Ofertas'} link={"#"}/> 
            </div>
            <div className="search-bar-container">
                <SearchBar placeholder={"Buscar produto"} />
                <ButtonIcons icon={"search"} />
            </div>
            <div className="user-options-container">
                <AccountOptions />
                <UsersOptions icon={"favorite_border"} />
                <UsersOptions icon={"add_shopping_cart"} onclick={openCartModal} />
            </div>
        </header>
        <SideModalCartItens isOpen={isCartModalOpen} onClose={closeCartModal} />
        </div>
    )
}

export default SecondHeader;