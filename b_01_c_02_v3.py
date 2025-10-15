#Integer Checker for Number of Questions

response = 0
def int_checker(x):
    global response
    while True:
        response = input("How many questions do you want?\n").lower()
        try:
            response = float(response)
            if 0 < response < 200:
                return response
            else:
                print("Please enter a number between 1-200")

        except ValueError:
            print("Please enter a valid number between 1-200")
while True:
    number = int_checker(response)
    print(f"You chose {int(number)} questions")