#Select Difficulty Component

response = ''
difficulties = ["easy","medium","hard"]
def select_difficulty(user_difficulty):
    while True:
        global response
        response = input("What Difficulty would you like to play?\n")
        if response in difficulties:
            return response
        else:
            print("That response is invalid. Please try again")
while True:
    response = select_difficulty(response)
    print(f"You chose {response}")