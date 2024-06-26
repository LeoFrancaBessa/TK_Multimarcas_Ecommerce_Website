import React, {useState} from "react";
import './SecondHeader.css'
import logo from '../../../assets/images/main_logo.png';
import CategoriesLinks from '../../commons/CategoriesLinks/CategoriesLinks'
import SearchBar from '../../commons/SearchBar/SearchBar'
import ButtonIcons from '../../commons/ButtonIcons/ButtonIcons'
import UserOptions from './UsersOptions'
import LoginModal from "../../LoginModal/LoginModal";

function SecondHeader(){
    const [isLoginModalOpen, setLoginModalOpen] = useState(false);

    const openLoginModal= () => setLoginModalOpen(true);
    const closeLoginModal = () => setLoginModalOpen(false);
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
                <UserOptions icon={"person_outline"} onclick={openLoginModal} />
                <UserOptions icon={"favorite_border"} />
                <UserOptions icon={"add_shopping_cart"} />
            </div>
        </header>
        <LoginModal isOpen={isLoginModalOpen} onClose={closeLoginModal}/>
        </div>
    )
}

export default SecondHeader;