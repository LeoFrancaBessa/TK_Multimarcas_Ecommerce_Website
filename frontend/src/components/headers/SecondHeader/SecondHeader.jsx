import React from "react";
import './SecondHeader.css'
import logo from '../../../assets/images/main_logo.png';
import CategoriesLinks from '../../commons/CategoriesLinks/CategoriesLinks'
import SearchBar from '../../commons/SearchBar/SearchBar'
import ButtonIcons from '../../commons/ButtonIcons/ButtonIcons'
import UserOptions from './UsersOptions'

function SecondHeader(){
    return (
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
                <UserOptions icon={"person_outline"} />
                <UserOptions icon={"favorite_border"} />
                <UserOptions icon={"add_shopping_cart"} />
            </div>
        </header>
    )
}

export default SecondHeader;