import React from "react";
import "./index.css";
function Navbar(){
    return(
        <nav className="navbar">
            <div className="navbar-logo">TOUR-X</div>
            <ul className="navbar-links">
                <li>Featues</li>
                <li>How It Works</li>
                <li>About</li>
                <li className="language">ENG</li>
            </ul>
        </nav>
    );
}
export default Navbar;