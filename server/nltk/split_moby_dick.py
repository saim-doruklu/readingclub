from nltk.tokenize import sent_tokenize

if __name__ == '__main__':
    occured = False
    start_parsing = False
    with open("resources/books/moby_dick", "rb") as file:
        as_string = file.read().decode('utf-8')
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
                print("Printing proper")