# Simple Python Spelling Checker

A small command-line project for learning Python. It accepts one sentence, finds words that are not in its English dictionary, and shows a likely correction.

## What you need

- Python 3 installed
- A terminal

## Install and run

Open a terminal inside this project folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python spell_checker.py
```

The first command creates a virtual environment: a private place for this
project's Python packages. You only need to create it once. In a new terminal,
run `source .venv/bin/activate` before running the app again.

Example:

```text
Welcome to the simple spelling checker!
Type a sentence, then press Enter.
> I am lerning Pythn

Possible spelling mistakes:
- lerning -> Did you mean: learning?
- pythn -> Did you mean: python?
```

## How it works

1. `input()` reads the sentence you type.
2. `get_words()` uses a regular expression to remove punctuation and split the sentence into words.
3. `SpellChecker()` loads an English word dictionary from the `pyspellchecker` package.
4. `spell.unknown(words)` finds words missing from that dictionary.
5. `spell.correction(word)` finds the closest likely spelling for each unknown word.

## Important note

This is a learning project, so it checks only one sentence at a time. A real spelling checker could add a graphical interface, multiple languages, a personal dictionary, or a database for saved words. This starter version does not need a database.
