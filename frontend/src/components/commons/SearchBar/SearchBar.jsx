import React from "react";
import './SearchBar.css'

function SearchBar({placeholder}){
    return (
        <input className="search-bar" type="text" placeholder={placeholder}></input>
    )
}

export default SearchBar;