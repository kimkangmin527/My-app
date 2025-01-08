import random

def football_quiz():
    players = [
        {"name": "Lionel Messi", "hint": "He is an Argentinian player and has won 7 Ballon d'Or awards."},
        {"name": "Cristiano Ronaldo", "hint": "This Portuguese star is famous for his goal-scoring records."},
        {"name": "Kylian Mbappé", "hint": "A French forward who starred in the 2018 World Cup at a young age."},
        {"name": "Neymar Jr", "hint": "A Brazilian forward known for his skills and flair."},
        {"name": "Zlatan Ibrahimović", "hint": "A Swedish striker famous for his acrobatic goals."},
    ]

    print("Welcome to the Football Player Guessing Game!\n")
    random_player = random.choice(players)

    print("Hint: ", random_player["hint"])

    attempts = 3
    while attempts > 0:
        guess = input(f"You have {attempts} attempts left. Enter your guess: ")
        if guess.lower() == random_player["name"].lower():
            print("Correct! You guessed the player.")
            break
        else:
            print("Wrong guess. Try again!")
            attempts -= 1

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct answer was {random_player['name']}.")

if __name__ == "__main__":
    football_quiz()

