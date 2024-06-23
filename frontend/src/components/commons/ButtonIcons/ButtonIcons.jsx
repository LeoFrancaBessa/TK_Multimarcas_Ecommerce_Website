import React from "react";
import './ButtonIcons.css'

function ButtonIcons({icon}){
    return (
        <button className="button-icon"><a href="#"><i class="large material-icons">{icon}</i></a></button>
    )
}

export default ButtonIcons;