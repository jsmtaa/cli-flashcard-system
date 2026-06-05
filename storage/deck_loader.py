import csv

def _load_csv_rows(path):
    with open(path, "r") as f:
        return list(csv.DictReader(f))


def deck_loader(decks_path, cards_path):
    decks = {}

    for row in _load_csv_rows(decks_path):
        deck = {"name": row["deck_name"], "cards": []}
        decks[row["deck_id"]] = deck

    for row in _load_csv_rows(cards_path):
        deck = decks[row["deck_id"]]
        deck["cards"].append(row)

    return decks


def main():
    decks = deck_loader("storage/decks.csv","storage/flashcards.csv")
    print(decks)

if __name__ == "__main__":
    main()
