#Integer Checker for Number of Questions

response = 0
def int_checker(x):
    global response
    while True:
        response = input("How many questions do you want?")
        if response == int(response):
            return response
        else:
            pass

while True:
    number = int_checker(response)
    print(f"You chose {int}")