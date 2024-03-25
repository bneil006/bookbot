def get_word_count(text):
    words = text.split()
    return len(words)

def count_how_many_different_characters(text):
    letter_dict = {}
    text = text.lower()

    for i in text:
        if i in letter_dict:
            letter_dict[i] +=1
        else:
            letter_dict[i] = 1
    return letter_dict
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    character_count = count_how_many_different_characters(text)
    print(character_count)
    
main()