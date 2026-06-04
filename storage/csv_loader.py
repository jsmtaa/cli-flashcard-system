import csv

def csv_loader(file):
    cards = []
    with open(file, "r") as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            cards.append(row) 
    return cards

if __name__ == "__main__":
    cards = csv_loader("storage/flashcards.csv")
    print(cards)
