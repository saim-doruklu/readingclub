import sys
import re

books_root = "resources/books"

if __name__ == '__main__':
    book_name = sys.argv[1:][0]

    with open(f'{books_root}/{book_name}/raw.txt', "r", encoding="utf8") as raw:
        with open(f'{books_root}/{book_name}/tokenized.txt', "r", encoding="utf8") as tokenized:
            with open(f'{books_root}/{book_name}/with_separator.txt', "w", encoding="utf8") as with_separator:
                tokenized_line = tokenized.readline()
                tokenized_line_without_whitespace = re.sub(r'\s+', '', tokenized_line)
                tokenized_line_length = len(tokenized_line_without_whitespace)
                raw_line = []
                raw_all_characters_until_match = []
                while True:
                    char = raw.read(1)
                    if not char:  # EOF
                        break
                    if char.isspace():
                        raw_all_characters_until_match.append(char)
                        continue
                    raw_all_characters_until_match.append(char)
                    raw_line.append(char)
                    if len(raw_line) > tokenized_line_length:
                        raw_line = raw_line[ len(raw_line)-tokenized_line_length : ]
                    raw_line_as_string = ''.join(raw_line)
                    if raw_line_as_string.__eq__(tokenized_line_without_whitespace):
                        with_separator.write(''.join(raw_all_characters_until_match))
                        with_separator.write('\\/\\/')

                        tokenized_line = tokenized.readline()
                        if not tokenized_line:  # EOF
                            exit(0)
                        tokenized_line_without_whitespace = re.sub(r'\s+', '', tokenized_line)
                        tokenized_line_length = len(tokenized_line_without_whitespace)
                        raw_line = []
                        raw_all_characters_until_match = []
