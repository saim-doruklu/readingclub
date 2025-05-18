import {bookListEndpoint} from "./endpoints";
import {BookDetails} from "./bookDetails";

export interface SuccessResult {
    success: true;
    books: BookDetails[];
}

export interface ErrorResult {
    success: false;
    error: string;
}

type FetchResult = SuccessResult | ErrorResult;

export const fetchBookList = async () => {
    return fetch(bookListEndpoint).then(r => {
        if (!r.ok) {
            throw new Error("Got response status " + r.status);
        }
        return r.json();
    }).then(responseJson => {
        const books: BookDetails[] = responseJson;
        return {success: true, books} as FetchResult;
    }).catch(e => {
        return {success: false, error: e.message} as FetchResult;
    });
}