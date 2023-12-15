current_users = ['admin','Kokakola12','obama','piterpen','JoJo']
current_users = ['admin','kokakola12','obama','piterpen','jojo']
new_users = ['ADMIN','kokakola12','obama2008','piterpen10','Jojo']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Please enter new username")
    else:
        print("Username is available")