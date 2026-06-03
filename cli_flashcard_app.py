import os

flashcard = [("What's the capital of Malaysia?", "Kuala Lumpur")]

def main():
    os.system("clear")
    display_card()
    input("Press Enter to show answer...")
    flip_card()
    gain_feedback()

def display_card():
    print(flashcard[0][0])

def flip_card():
    print(flashcard[0][1])

def gain_feedback() -> int:
    print("Press the following key:")
    print("1 Trivial | 2 Easy | 3 Medium | 4 Hard")
    return input("> ")
    
main()
