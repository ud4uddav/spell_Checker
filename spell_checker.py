"""A small command-line spelling checker for beginners.

Run this file with: python spell_checker.py
"""

import re

from spellchecker import SpellChecker


def get_words(text):
    """Return the words in *text*, without punctuation or numbers.

    For example, "Hello, world!" becomes ["hello", "world"].
    Converting to lowercase keeps the check case-insensitive.
    """
    return re.findall(r"[a-zA-Z']+", text.lower())


def check_spelling(text):
    """Print spelling mistakes and one suggested replacement for each."""
    spell = SpellChecker()
    words = get_words(text)

    # unknown() returns only the words that are not in the dictionary.
    misspelled_words = spell.unknown(words)

    if not misspelled_words:
        print("\nGreat! No spelling mistakes were found.")
        return

    print("\nPossible spelling mistakes:")
    for word in sorted(misspelled_words):
        # correction() returns the closest word the library can find.
        suggestion = spell.correction(word)

        if suggestion:
            print(f"- {word} -> Did you mean: {suggestion}?")
        else:
            # A word may be a name or a new word that the dictionary does not know.
            print(f"- {word} -> No suggestion found")


def main():
    """Ask the user for a sentence and check it."""
    print("Welcome to the simple spelling checker!")
    print("Type a sentence, then press Enter.")

    sentence = input("> ")

    # strip() removes accidental spaces at the beginning and end.
    if not sentence.strip():
        print("Please enter some text next time.")
        return

    check_spelling(sentence)


# This makes main() run only when this file is run directly.
if __name__ == "__main__":
    main()
