def display_card(card_type):
    post_question(card_type)
    get_answer(card_type)
    receive_feedback()

def show_question(card_type, question, choices=[]):
    print(question)
    if choices and card_type == 3:
        for idx, choice in enumerate(choices):
            letter_choice = chr(ord("A") + idx)
            print(f"{letter_choice}. {choice}")
    

def get_user_answer(card_type):
    match card_type:
        case 1:
            print("Press \"Enter\" to flip card.")
        case 2:
            print("Enter your answer.")
        case 3:
            print("Enter the letter of your answer.")
    return input("> ")

def show_correct_answer(answer):
    print("Correct answer:")
    print(answer)

def get_feedback(self) -> int:
    print("\nHow well did you find this question?")
    print("1 Trivial | 2 Easy | 3 Medium | 4 Hard")
    self.feedback = int(input("> "))
