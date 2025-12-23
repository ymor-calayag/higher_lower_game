from data import game_data
from art import logo
import random

print(logo)

OPTION_A = random.choice(game_data) # not really constants, but just to know that they are globals
OPTION_B = random.choice(game_data)
PLAYER_LIFE = 1
SCORE = 0

def check_higher(a, b):
    """Returns which option is higher."""
    return "a" if a['follower_count'] > b['follower_count'] else "b"

def is_the_same(a, b):
    """Checks if the options are the same and changes OPTION_B if they are."""
    while a == b:
        b = random.choice(game_data)
    return b

OPTION_B = is_the_same(OPTION_A, OPTION_B)

print(f"\nCompare A: {OPTION_A['name']}, a {OPTION_A['description']}, from {OPTION_A['country']}\n")
print("Vs.\n")
print(f"Compare B: {OPTION_B['name']}, a {OPTION_B['description']}, from {OPTION_B['country']}\n")

def play_game():
    global OPTION_A, OPTION_B, PLAYER_LIFE, SCORE
    while PLAYER_LIFE > 0:
        answer = check_higher(OPTION_A, OPTION_B)
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        if player_choice == answer:
            if player_choice == "a":
                SCORE += 1
                print(f"You are right! Current score: {SCORE}\n")

                OPTION_B = random.choice(game_data)

                OPTION_B = is_the_same(OPTION_A, OPTION_B)

                print(f"\nCompare A: {OPTION_A['name']}, a {OPTION_A['description']}, from {OPTION_A['country']}\n")
                print("Vs.\n")
                print(f"Compare B: {OPTION_B['name']}, a {OPTION_B['description']}, from {OPTION_B['country']}\n")
            else:
                SCORE += 1
                print(f"You are right! Current score: {SCORE}\n")

                OPTION_A = OPTION_B
                OPTION_B = random.choice(game_data)

                OPTION_B = is_the_same(OPTION_A, OPTION_B)

                print(f"\nCompare A: {OPTION_A['name']}, a {OPTION_A['description']}, from {OPTION_A['country']}\n")
                print("Vs.\n")
                print(f"Compare B: {OPTION_B['name']}, a {OPTION_B['description']}, from {OPTION_B['country']}\n")
        else:
            PLAYER_LIFE -= 1

play_game()
print(f"Sorry, your answer is wrong.\nTotal score: {SCORE}")
