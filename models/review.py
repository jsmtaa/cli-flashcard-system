import os

class ReviewSession:
    def __init__(self, deck, cli):
        self.deck = deck
        self.cli = cli

    def run(self):
        for card in self.deck.cards:
            self.cli.display_card(card)
