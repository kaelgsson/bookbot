def get_num_words(text: str) -> int:
    number_of_words = len(text.split())
    return number_of_words

__all__ = ["get_num_words"]

if __name__ == "__main__":
    assert get_num_words("") == 0
    assert get_num_words("one two") == 2
    print("stats.get_num_words: basic checks passed")