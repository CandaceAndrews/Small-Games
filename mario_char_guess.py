import random


possible_characters = {
    "mario": {
        "clues": [
            "main character",
            "wears a hat",
            "has a mustache"
        ]
    },
    "luigi": {
        "clues": [
            "has a brother",
            "wears a hat",
            "likes green"
        ]
    },
    "bowser": {
        "clues": [
            "can breathe fire",
            "main villain",
            "has horns"
        ]
    },
    "princess peach": {
        "clues": [
            "wears a dress",
            "wears a crown",
            "gets kidnapped a lot"
        ]
    },
    "toad": {
        "clues": [
            "wears a vest",
            "is a mushroom",
            "princess peach's attendant"
        ]
    },
    "yoshi": {
        "clues": [
            "mario and luigi ride him",
            "is a dinosaur",
            "eats enemies with tongue"
        ]
    }
}

play_again = True
while play_again:
    guess = ""
    character = random.choice(list(possible_characters.keys()))
    number_of_clues = len(possible_characters[character]["clues"])
    if number_of_clues >= 3:
        turns = 3
    else:
        turns = number_of_clues

    while turns > 0:
        clue = random.choice(possible_characters[character]["clues"])
        possible_characters[character]["clues"].remove(clue)
        print(f"\n\nTurns remaining: {turns}")
        print(f"Your clue is: {clue}\n\n")
        guess = input("Enter your guess or 'exit' to exit: ").lower()

        if guess == character:
            print(f"You win! The character was {character}!")
            break
        elif guess == "exit":
            break
        else:
            print("Incorrect, try again")
            turns -= 1
    answer = input("Do you want to play again? ").lower()
    if answer == "no":
        play_again = False
