import {useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import {bookDetails} from "./endpoints";
import "./book.css";

function Book() {
    const {bookId} = useParams<{ bookId: string }>();
    const [contents, setContents] = useState("");

    useEffect(() => {
        if (!bookId) return;
        console.log("Fetching book details for bookId: " + bookId);
        const bookDetailsUrl = bookDetails(bookId);
        fetch(bookDetailsUrl).then(r => {
            r.text().then(setContents);
        });
    }, [bookId]);


    return (
        contents ? <pre className={"bookContents"}>{contents}</pre> : <div>Loading...</div>
    )
}

export default Book;