import React from "react";
import './UsersOptions.css'

function UsersOptions({icon, onclick}){
    return (
        <a className="user-options" href="#" onclick={onclick}><i class="large material-icons">{icon}</i></a>
    )
}

export default UsersOptions;