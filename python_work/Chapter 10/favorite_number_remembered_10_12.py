import json

def ask_user_favorite_number():
    """Asking users favorite number"""
    filename = 'user_favorite_number.json'
    try:
        usernumber = input('What is your favorite number?')
        with open(filename, 'w') as f:
            json.dump(int(usernumber), f)
    except ValueError:
        print("Please enter a number next time")

def read_user_favorite_number():
    """Read user favorite number"""
    filename = 'user_favorite_number.json'
    with open(filename) as f:
        usernumber = json.load(f)
        print(f"I know your favorite number! It's {usernumber}")

ask_user_favorite_number()
read_user_favorite_number()