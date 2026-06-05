from storage.deck_loader import deck_loader
from models.review import ReviewSession
import ui.cli as cli

class App:
    def __init__(self):
        self.decks = deck_loader("storage/decks.csv", "storage/flashcards.csv")

    def run(self):
        self.deck = cli.get_deck(self.decks)
        self.review = ReviewSession(self.deck, cli)
        self.review.run()
