import React, {useState} from "react";
import './SecondHeader.css'
import logo from '../../../assets/images/main_logo.png';
import CategoriesLinks from '../../commons/CategoriesLinks/CategoriesLinks'
import SearchBar from '../../commons/SearchBar/SearchBar'
import ButtonIcons from '../../commons/ButtonIcons/ButtonIcons'
import UserOptions from './UsersOptions'
import AccountOptions from "./AccountOptions";
import LoginModal from "../../LoginModal/LoginModal";
import SideModalCartItens from "../../SideModalCartItens/SideModalCartItens";


function SecondHeader(){
    const [isLoginModalOpen, setLoginModalOpen] = useState(false);
    const openLoginModal= () => setLoginModalOpen(true);
    const closeLoginModal = () => setLoginModalOpen(false);

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
                <UserOptions icon={"favorite_border"} />
                <UserOptions icon={"add_shopping_cart"} onclick={openCartModal} />
            </div>
        </header>
        <LoginModal isOpen={isLoginModalOpen} onClose={closeLoginModal}/>
        <SideModalCartItens isOpen={isCartModalOpen} onClose={closeCartModal} />
        </div>
    )
}

export default SecondHeader;