import React from 'react';
import {Link} from "react-router-dom";

const NotFound = () => {
    return ( 
        <div className="not_found">
            <h2>404 Sorry</h2>
            <p>thiat page cannot be found</p>
            <Link to="/">Back to the hompage...</Link>
        </div>
     );
}

export default NotFound;