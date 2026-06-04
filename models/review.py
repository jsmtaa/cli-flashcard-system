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
            if len(card) == 4: # 4 is one with Multiple choice
                choices = card[3].split(",")
                self.cli.show_question(card_type, question, choices)
            else:
                self.cli.show_question(card_type, question)

            self.cli.get_user_answer(card_type)
            
            # TODO: Validate answer in future
            
            self.cli.show_correct_answer(correct_answer)
            
            input("press anything to continue")

            os.system("clear")

            # feedback = self.cli.get_feedback()
            
            # interval_days = update_interval_days(feedback)
            
