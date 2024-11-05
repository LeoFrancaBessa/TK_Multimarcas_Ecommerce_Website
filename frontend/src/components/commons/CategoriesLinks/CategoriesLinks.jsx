import React from "react";
import './CategoriesLinks.css';
import { Link } from "react-router-dom";

function CategoriesLinks({text, url}){
    return (
        <Link to={`/busca/${url}`} style={{ textDecoration: 'none' }}> 
            <a className="clothing-options" href="#">{text}</a> 
        </Link> 
    )
}

export default CategoriesLinks
