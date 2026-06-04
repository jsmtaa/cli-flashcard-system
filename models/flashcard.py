class Flashcard:
    def __init__(self, card_type, question, answer, choices=None: List[str]):
        self.card_type = card_type
        self.question = question
        self.answer = answer
        self.choices = choices
        self.interval_days = 0

    # TODO: Implement and update with flashcards.csv
    def update_interval_days(self, feedback):
        match feedback:
            case 1:
                self.interval_days = 7
            case 2:
                self.interval_days = 5
            case 3:
                self.interval_days = 2
            case 4:
                self.interval_days = 1

