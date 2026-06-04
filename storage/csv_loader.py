import csv

def csv_loader(file):
    rows = []
    with open(file, "r") as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            rows.append(row) 
    return rows

if __name__ == "__main__":
    rows = csv_loader("storage/flashcards.csv")
    print(rows)
