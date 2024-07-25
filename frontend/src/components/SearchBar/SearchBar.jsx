import {React, useState} from "react";
import './SearchBar.css';
import SearchRecommendationsModal from '../SearchRecommendationsModal/SearchRecommendationsModal'

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

    const handleClickOutside = async function(){
        setTimeout(() => {
            closeSearchModal();
        }, 100);
    }

    return (
        <div className="search-bar-container"> 
            <input className="search-bar" type="text" placeholder={placeholder} onChange={handleChange} onBlur={handleClickOutside} onClick={openSearchModal}></input>
            <SearchRecommendationsModal isOpen={isSearchModalOpen} searchTerm={searchTerm} onClose={closeSearchModal} />
        </div>
    )
}

export default SearchBar;