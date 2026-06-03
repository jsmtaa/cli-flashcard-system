import os

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.interval_days = 0
        self.feedback = None

    def display_card(self):
        print(self.question)
    
    def flip_card(self):
        input("Press \"Enter\" to flip card.")
        print(self.answer)

    def gain_feedback(self) -> int:
        print("Press the following key:")
        print("1 Trivial | 2 Easy | 3 Medium | 4 Hard")
        self.feedback = int(input("> "))

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

class App:
    def __init__(self):
        self.flashcards = []

def main():
    q1 = Flashcard("What's the capital of Malaysia?", "Kuala Lumpur")
    print(q1.interval_days)
    q1.display_card()
    q1.flip_card()
    q1.gain_feedback()
    q1.update_interval_days(q1.feedback)
    print(q1.interval_days)
if __name__ == "__main__":
    main()
