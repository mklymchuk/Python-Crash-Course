import json

"""Read user favorite number"""

def read_user_favorite_number():
    """Read user favorite number"""
    filename = 'user_favorite_number.json'
    with open(filename) as f:
        usernumber = json.load(f)
        print(f"I know your favorite number! It's {usernumber}")

read_user_favorite_number()