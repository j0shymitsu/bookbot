def count_words(text):
    words = text.split()
    num_words = 0

    for word in words:
        num_words += 1

    print(f"{num_words} words found in the document")

def count_characters(passage):
    string_to_int = {}

    for character in passage:
        character = character.lower()
        string_to_int.setdefault(character, 0)
        string_to_int[character] += 1

    return string_to_int