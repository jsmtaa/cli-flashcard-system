import os

def get_deck(decks):
    print("Choose a deck:")
    hashmap = {}
    for i, deck in enumerate(decks):
        print(f"{i+1}. {decks[deck]["name"]}") 
        hashmap[i] = deck

    choice = int(input("> ")) - 1
    return decks[hashmap[choice]]

def display_card(card_type: int, question: str, answer: str, choices=[]: Optional[List[str]]) -> None:
    show_question(card_type, question, choices)
    get_user_answer(card_type)
    # TODO: Validate answer in future
    show_correct_answer(answer)
    input("\nPress anything to continue...")
    os.system("clear")
    
def show_question(card_type: int, question: str, choices=[]: Optional[List[str]]) -> None:
    print(question)
    choices = choices.split(", ")
    if card_type == 3:
        for idx, choice in enumerate(choices):
            letter_choice = chr(ord("A") + idx)
            print(f"{letter_choice}. {choice}")
    

def get_user_answer(card_type: int) -> str:
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
