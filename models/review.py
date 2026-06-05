import os

class ReviewSession:
    def __init__(self, deck, cli):
        self.deck = deck
        self.cli = cli

    def run(self):
        os.system("clear")
        for card in self.deck["cards"]:
            hasChoices = card["choices"] != ""
            if hasChoices:
                choices = card["choices"].split(",")
                self.cli.display_card(int(card["card_type"]), card["question"], card["answer"], card["choices"])
            else:
                self.cli.display_card(int(card["card_type"]), card["question"], card["answer"], card["choices"])
