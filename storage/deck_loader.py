import csv

def deck_loader(file, deck_id):
    rows = []
    with open(file, "r") as f:
        data = csv.DictReader(f)
        for row in data:
            if row["deck_id"] == deck_id:
                rows.append(row)
    return rows

def main():
    rows = deck_loader("storage/flashcards.csv", "12345")
    print(rows)

if __name__ == "__main__":
    main()
