import React from "react";
import './UsersOptions.css'

function UsersOptions({icon, onclick}){
    return (
        <a className="user-options" href="#" onClick={onclick}><i className="large material-icons">{icon}</i></a>
    )
}

export default UsersOptions;