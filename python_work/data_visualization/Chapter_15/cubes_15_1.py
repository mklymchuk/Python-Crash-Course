import matplotlib.pyplot as plt

x_values = range(1, 5000)
y_values = [x ** 3 for x in x_values]

plt.style.use('_classic_test_patch')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10) #type: ignore

# Set chart title and lable axes.
ax.set_title("Cubic numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

# Set size of tick labels.
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()