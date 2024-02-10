import matplotlib.pyplot as plt

x_values = range(1, 5000)
y_values = [x ** 3 for x in x_values]

plt.style.use('_classic_test_patch')
fig, ax = plt.subplots()

ax.plot(x_values, y_values, linewidth = 3)

# Set chart title and lable axes.
ax.set_title("Cubic numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

# Set size of tick labels
ax.tick_params(axis = 'both', labelsize = 14)

plt.show()