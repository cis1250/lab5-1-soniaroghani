#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    """Ask the user for a valid sentence and return it."""
    while True:
        sentence = input("Enter a sentence: ").strip()
        if is_sentence(sentence):
            return sentence
        else:
            print("Invalid sentence. Make sure it starts with a capital letter and ends with punctuation.")


def calculate_frequencies(sentence):
    """Split the sentence into words and count how often each word appears."""
    # Remove the final punctuation
    sentence = sentence[:-1].lower()
    words = sentence.split()

    word_list = []
    freq_list = []

    for word in words:
        if word in word_list:
            index = word_list.index(word)
            freq_list[index] += 1
        else:
            word_list.append(word)
            freq_list.append(1)

    return word_list, freq_list


def print_frequencies(words, frequencies):
    """Print words and their frequencies."""
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")


def main():
    """Main function to control the program flow."""
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)


if __name__ == "__main__":
    main()
