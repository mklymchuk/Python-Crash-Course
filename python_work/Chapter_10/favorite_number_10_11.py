import json

"""Ask user for their favorite number"""

def ask_user_favorite_number():
    """Asking users favorite number"""
    filename = 'user_favorite_number.json'
    try:
        usernumber = input('What is your favorite number?')
        with open(filename, 'w') as f:
            json.dump(int(usernumber), f)
    except ValueError:
        print("Please enter a number next time")

ask_user_favorite_number()