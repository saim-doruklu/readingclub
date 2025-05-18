import sys
from nltk.tokenize import sent_tokenize

books_root = "resources/books"

if __name__ == '__main__':
    book_name = sys.argv[1:][0]
    occured = False
    start_parsing = False
    with open(f'{books_root}/{book_name}/raw', "rb") as raw:
        with open(f'{books_root}/{book_name}/tokenized', "w", encoding='utf-8') as tokenized:
            as_string = raw.read().decode('utf-8')
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
                    tokenized.write(token)
                    tokenized.write("\r\n")