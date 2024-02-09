import matplotlib.pyplot as plt
x_values = range(1, 1000)
y_values = [x ** 2 for x in x_values]

plt.style.use('_classic_test_patch')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = 'red', s = 10)

# Set chart title and lable axes.
ax.set_title("Square numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set size of tick lables
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])
plt.show()
