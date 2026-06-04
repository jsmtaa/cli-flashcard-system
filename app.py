from storage.csv_loader import csv_loader
from models.review import ReviewSession
import ui.cli as cli

class App:
    def __init__(self):
        self.deck = csv_loader("storage/flashcards.csv")

    def run(self):
        self.review = ReviewSession(self.deck, cli)
        self.review.run()
