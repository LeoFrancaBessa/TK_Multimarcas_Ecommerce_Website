import React, {useState} from "react";
import './SecondHeader.css'
import logo from '../../../assets/images/main_logo.png';
import { Link } from "react-router-dom";
import CategoriesLinks from '../../commons/CategoriesLinks/CategoriesLinks'
import SearchBar from "../../SearchBar/SearchBar";
import ButtonIcons from '../../commons/ButtonIcons/ButtonIcons'
import UsersOptions from "../../commons/UserOptions/UsersOptions";
import AccountOptions from "../../AccountOptions/AccountOptions";
import SideModalCartItens from "../../SideModalCartItens/SideModalCartItens";
import SideModalFavorites from "../../SideModalFavorites/SideModalFavorites";


function SecondHeader(){
    const [isCartModalOpen, setCartModalOpen] = useState(false);
    const openCartModal= () => setCartModalOpen(true);
    const closeCartModal = () => setCartModalOpen(false);

    const [isFavoritesModalOpen, setFavoritesModalOpen] = useState(false);
    const openFavoritesModal= () => setFavoritesModalOpen(true);
    const closeFavoritesModal = () => setFavoritesModalOpen(false);

    //Caixa de busca e botão de busca usam o mesmo valor
    const [searchTerm, setSearchTerm] = useState('');

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
                <SearchBar placeholder={"Buscar produto"} searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
                <Link to={`/busca/${searchTerm}`}> 
                    <ButtonIcons icon={"search"} /> 
                </Link>
            </div>
            <div className="user-options-container">
                <AccountOptions />
                <UsersOptions icon={"favorite_border"} onclick={openFavoritesModal} />
                <UsersOptions icon={"add_shopping_cart"} onclick={openCartModal} />
            </div>
        </header>
        <SideModalCartItens isOpen={isCartModalOpen} onClose={closeCartModal} />
        <SideModalFavorites isOpen={isFavoritesModalOpen} onClose={closeFavoritesModal} />
        </div>
    )
}

export default SecondHeader;