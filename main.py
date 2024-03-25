def get_word_count(text):
    words = text.split()
    return len(words)

def count_how_many_different_characters(text):
    letter_dict = {}
    text = text.lower()

    for i in text:
        if i.isalpha():
            if i in letter_dict:
                letter_dict[i] +=1
            else:
                letter_dict[i] = 1
    return letter_dict

def sort_on(d):
    return d["number"]

def report_on_words_and_characters(text):
    word_count = get_word_count(text)
    character_count = count_how_many_different_characters(text)
    character_list = []

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")

    for character in character_count:
        character_list.append({"character": character, "number": character_count[character]})
    character_list.sort(reverse=True, key=sort_on)

    for i in character_list:
        print(f"The '{i['character']}' character was found {i['number']} times")

    print(f"--- End Report ---")
    return

    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report_on_words_and_characters(text)
    
main()