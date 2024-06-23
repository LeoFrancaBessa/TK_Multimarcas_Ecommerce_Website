import React from "react";
import './CategoriesLinks.css'

function CategoriesLinks({text, link}){
    return (
        <a className="clothing-options" href={link}>{text}</a>
    )
}

export default CategoriesLinks
