import React from 'react';
import './App.css';
import BookList from "./bookList";
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Book from "./book";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<BookList/>}/>
                <Route path="/book/:bookId" element={<Book/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
