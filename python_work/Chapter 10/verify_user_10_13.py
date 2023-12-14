import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.

filename = 'username.json'

def get_stored_username():
    """Get stored username if available."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
        """Greet the user by name."""
        username = get_stored_username()
        answer = input(f"Is it a correct {username}, type 'y' if username correct, and 'n' if not")
        if answer == 'y':
            if username:
                print(f"Welcome back, {username}!")
            else:
                username = get_new_username()
                print(f"We'll remember you when you come back, {username}!")
        else:
            get_new_username()

greet_user()