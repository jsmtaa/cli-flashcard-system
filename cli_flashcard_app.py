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
        input("\nPress \"Enter\" to flip card.")
        print("\n" + self.answer)

    def gain_feedback(self) -> int:
        print("\nPress the following key:")
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
        self.flashcards = [
                Flashcard("What's the capital of Malaysia?", "Kuala Lumpur"),
                Flashcard("What is 5 + 7?", "12"),
                Flashcard("What language is primarily used for Android apps?", "Kotlin"),
                Flashcard("What planet is known as the Red Planet?", "Mars"),
                Flashcard("What does CPU stand for?", "Central Processing Unit")
        ]

    def run(self):
        for i, card_obj in enumerate(self.flashcards):
            os.system("clear")
            print(f"CARD #{i+1}")
            card_obj.display_card()
            card_obj.flip_card()
            self.feedback = card_obj.gain_feedback()
            card_obj.update_interval_days(self.feedback)

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
