#Integer Checker for Number of Questions

response = 0
def int_checker(x):
    global response
    while True:
        response = input("How many questions do you want?").lower()
        try:
            response = float(response)
            if response > 0:
                return response
            else:
                print("Please enter a number greater than 0")

        except ValueError:
            print("Please enter a valid number.")
while True:
    number = int_checker(response)
    print(f"You chose {number}")