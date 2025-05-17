# return num of words in passage
def count_words(text):
    words = text.split()
    return len(words)

# return dictionary of characters and their counts
def count_characters(passage):
    string_to_int = {}

    for character in passage:
        character = character.lower()
        string_to_int.setdefault(character, 0)
        string_to_int[character] += 1

    return string_to_int

# function for dictionary key
def sort_on(dict):
    return dict["num"]

# return sorted dictionary by highest to lowest character count    
def sorted_dict(char_counts):
    result = []
    
    for char, count in char_counts.items():
        result.append({"char": char, "num": count})

    result.sort(reverse=True, key=sort_on)

    return result
    