import os

class ReviewSession:
    def __init__(self, deck, cli):
        self.deck = deck
        self.cli = cli

    def run(self):
        os.system("clear")
        for card in self.deck:
            card_type = int(card[0])
            question, correct_answer = card[1], card[2]

            hasChoices = len(card) == 4
            if hasChoices: # 4 is one with Multiple choice
                choices = card[3].split(",")
                self.cli.display_card(card_type, question, correct_answer, choices)
            else:
                self.cli.display_card(card_type, question, correct_answer)

            
            
