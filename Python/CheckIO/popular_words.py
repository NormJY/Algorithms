# In this mission your task is to determine the popularuty of certain words in the text.
# Input: The text and the search words array
# Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text
# The words should be sought in all registers.

def popular_words(text: str, words: list) -> dict:
    text = text.lower()
    splitted_words = text.split()
    answer = {}

    for word in words:
        answer[word] = splitted_words.count(word)

    return answer