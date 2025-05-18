import {useState, useEffect} from 'react';
import {fetchBookList, SuccessResult} from "./backend";
import {BookDetails} from "./bookDetails";
import {useNavigate} from "react-router-dom";

function BookList() {
    const navigate = useNavigate();
    const [bookList, setBooklist] = useState<BookDetails[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<string>();

    useEffect(() => {
        fetchBookList().then(res => {
            if (res.success) {
                const asSuccessResult = res as SuccessResult;
                setBooklist(asSuccessResult.books);
                setIsLoading(false);
            } else {
                setBooklist([]);
                setIsLoading(false);
                setError(res.error);
            }
        });
    }, []);

    if (isLoading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    const handleClick = (book: BookDetails) => {
        const absolutePath = new URL("book/"+book.id, window.location.href).pathname;
        navigate(absolutePath);
    };


    return (
        <div>
            <ul>
                {
                    bookList.map(book => (
                        <li key={book.id}>
                            <a href={`book/${book.id}`}
                               onClick={(e) => {
                                   e.preventDefault();
                                   handleClick(book);
                               }}
                            >
                                {book.name}
                            </a>
                        </li>
                    ))
                }
            </ul>
        </div>
    )

}

export default BookList;