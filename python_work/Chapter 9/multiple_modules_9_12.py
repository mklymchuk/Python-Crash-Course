import privileges_9_8

new_admin = privileges_9_8.Admin('Mykola', 'Klymvhuk', 28, 'male')
new_admin.describe_user()
new_admin.greet_user()
new_admin.privileges.show_privileges()