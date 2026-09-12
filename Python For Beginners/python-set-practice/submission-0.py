from typing import List

def contains_duplicate(words: List[str]) -> bool:
    # compare len of list vs len of set(list)
    count_list_words = len(words)
    count_unique_words = len(set(words))
    duplicates = count_list_words != count_unique_words
    return duplicates

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
