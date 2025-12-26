def get_num_words(text: str) -> int:
    number_of_words = len(text.split())
    return number_of_words

def get_num_chars(text: str) -> dict:
    char_dict = {}
    for char in text:
        _char = char.lower()
        if _char in char_dict:
            char_dict[_char] += 1
        else:
            char_dict[_char] = 1
    return char_dict

__all__ = ["get_num_words", "get_num_chars"]

if __name__ == "__main__":
    assert get_num_words("one two") == 2
    assert get_num_chars("on o") == {"o": 2, "n": 1, " ": 1}
    print("basic checks passed")