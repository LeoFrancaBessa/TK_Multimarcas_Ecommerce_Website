import React from "react";
import './SectionsGrid.css'

function SectionsGrid({sectionImage1, sectionImage2, sectionImage3}){
    return (
        <div className="sections-container">
            <div className="section-card">
                    <img src={sectionImage1} alt="Roupa 1" className="section-card-img"></img>
            </div>
            <div className="section-card">
                    <img src={sectionImage2} alt="Roupa 1" className="section-card-img"></img>
            </div>
            <div className="section-card">
                    <img src={sectionImage3} alt="Roupa 1" className="section-card-img"></img>
            </div>
        </div>
    )
}

export default SectionsGrid