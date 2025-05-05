import {useParams} from "react-router-dom";

function Book() {
    const { bookId } = useParams<{ bookId: string }>();

    return (
        <div>
            <p>
                {"Book details "+bookId}
            </p>
        </div>
    )
}

export default Book;