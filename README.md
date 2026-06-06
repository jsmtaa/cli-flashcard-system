# CLI Flashcard System

Command-line flashcard app for running simple review sessions in the terminal.

## What it does

- Loads flashcards from `storage/flashcards.csv`
- Runs a review session that shows cards one at a time
- Supports 3 card types:
  - Basic flip/reveal
  - Fill-in-the-blank
  - Multiple choice
- Prompts the user for an answer, then reveals the correct answer

## Run

```bash
python main.py
```

## In progress / future featur
- Validate user answers instead of only revealing the correct answer
- Wire feedback scoring into the review flow
- Track review intervals with spaced-repetition-style logic
- Update card scheduling data back into storage
- Integrate AI to suggest hints, answer feedback, and possibly advanced features such as card generators
