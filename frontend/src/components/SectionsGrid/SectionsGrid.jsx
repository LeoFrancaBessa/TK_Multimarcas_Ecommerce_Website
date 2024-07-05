import React from "react";
import './SectionsGrid.css'

function SectionsGrid({sectionImage1, sectionImage2, sectionImage3}){
    return (
        <div class="sections-container">
            <div class="section-card">
                    <img src={sectionImage1} alt="Roupa 1" class="section-card-img"></img>
            </div>
            <div class="section-card">
                    <img src={sectionImage2} alt="Roupa 1" class="section-card-img"></img>
            </div>
            <div class="section-card">
                    <img src={sectionImage3} alt="Roupa 1" class="section-card-img"></img>
            </div>
        </div>
    )
}

export default SectionsGrid