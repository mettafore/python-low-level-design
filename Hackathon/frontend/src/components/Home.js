// src/components/Home.js

import React from 'react';

const Home = () => {
    return (
        <div className="home-container">
            <h2>Welcome to Online Library</h2>
            <ul>
                <li><a href="#">Explore Books</a></li>
                <li><a href="#">My Books</a></li>
                <li><a href="#">Orders</a></li>
                <li><a href="#">Transactions</a></li>
            </ul>
        </div>
    );
}

export default Home;
