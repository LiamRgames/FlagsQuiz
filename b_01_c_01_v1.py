#Select Difficulty Component

response = ''

def select_difficulty(user_difficulty):
    global response
    response = input("What Difficulty would you like to play?")
    if response == "easy":
        user_difficulty = "easy"
    elif response == "medium":
        user_difficulty = "medium"
    else:
        user_difficulty = "hard"
    return user_difficulty
while True:
    response = select_difficulty(response)
    print(f"You chose {response}")