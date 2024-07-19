import {React, useState} from "react";
import './SearchBar.css';
import SearchRecommendationsModal from "../SearchRecommendationsModal/SearchRecommendationsModal";

function SearchBar({placeholder}){
    const [searchTerm, setSearchTerm] = useState('');
    const [isSearchModalOpen, setIsSearchModalOpen] = useState(false);
    
    const openSearchModal = () => setIsSearchModalOpen(true);
    const closeSearchModal = () => setIsSearchModalOpen(false);

    const handleChange = (event) => {
        const {value} = event.target;
        setSearchTerm(value);
        if (value.length > 3){
            openSearchModal();
        }
        else{
            closeSearchModal();
        }
    }

    return (
        <div className="search-bar-container"> 
            <input className="search-bar" type="text" placeholder={placeholder} onChange={handleChange} onBlur={closeSearchModal} onClick={openSearchModal}></input>
            <SearchRecommendationsModal isOpen={isSearchModalOpen} searchTerm={searchTerm} />
        </div>
    )
}

export default SearchBar;