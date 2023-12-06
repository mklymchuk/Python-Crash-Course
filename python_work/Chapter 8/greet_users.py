def greeat_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greeat_users(usernames)