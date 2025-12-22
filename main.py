from data import game_data
import random

# compare two data
# make the user choose which one is bigger
# if wrong, game over
# if right, the correct answer stays and will be against a new data

# art here

# fix issue where what if option a and b are the same
option_a = random.choice(game_data)
option_b = random.choice(game_data)

print(f"\nCompare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}\n")
print("Vs.\n")
print(f"Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}\n")

print(f"option_a: {option_a['follower_count']}")
print(f"option_b: {option_b['follower_count']}")

def check_higher(a, b):
    return "a" if a['follower_count'] > b['follower_count'] else "b"

player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

answer = check_higher(option_a, option_b)

if player_choice == answer:
    print("correct")
else:
    print("wrong")

    # {
    #     'name': 'Instagram',
    #     'follower_count': 346,
    #     'description': 'Social media platform',
    #     'country': 'United States'
    # },