def count_words(text):
    words = text.split()
    return len(words)

def count_characters(passage):
    string_to_int = {}

    for character in passage:
        character = character.lower()
        string_to_int.setdefault(character, 0)
        string_to_int[character] += 1

    return string_to_int

def sort_on(dict):
    return dict["num"]
    
def sorted_dict(char_counts):
    result = []
    
    for char, count in char_counts.items():
        result.append({"char": char, "num": count})

    result.sort(reverse=True, key=sort_on)

    return result
    