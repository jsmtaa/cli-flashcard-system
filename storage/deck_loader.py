import csv
from models.flashcard import Flashcard
from models.deck import Deck

def _load_csv_rows(path):
    with open(path, "r") as f:
        return list(csv.DictReader(f))


def deck_loader(decks_path, cards_path):
    decks = {}
    
    for row in _load_csv_rows(decks_path):
        deck = Deck(row["deck_id"], row["deck_name"])
        decks[row["deck_id"]] = deck

    for row in _load_csv_rows(cards_path):
        card_obj = Flashcard(
                row["deck_id"], 
                row["card_id"], 
                row["card_type"], 
                row["question"], 
                row["answer"], 
                row["choices"]
            )
        deck = decks[row["deck_id"]]
        deck.cards.append(card_obj)

    return decks


def main():
    decks = deck_loader("storage/decks.csv","storage/flashcards.csv")
    print(decks)

if __name__ == "__main__":
    main()
