from nltk.tokenize import sent_tokenize

if __name__ == '__main__':
    occured = False
    start_parsing = False
    book_name = "moby_dick"
    with open(f'resources/books/{book_name}', "rb") as untokenized_book:
        with open(f'resources/books_tokenized/{book_name}', "wt") as tokenized_book:
            as_string = untokenized_book.read().decode('utf-8')
            tokens = sent_tokenize(as_string)
            tokens_with_newlines_removed = [item.replace("\r\n", " ") for item in tokens]
            for token in tokens_with_newlines_removed:
                if start_parsing is False:
                    if "Loomings." in token:
                        if occured is False:
                            occured = True
                        else:
                            start_parsing = True
                else:
                    tokenized_book.writelines(token)
                    tokenized_book.write("\r\n")