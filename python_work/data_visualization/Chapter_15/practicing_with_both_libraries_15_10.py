import matplotlib.pyplot as plt
import plotly.express as px
from die import Die

# Create a die
die_1 = Die()
die_2 = Die()

# Make some rolls
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
die_max_value = die_1.num_sides + die_2.num_sides
for value in range(2, die_max_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Plot the frequencies
fig, ax = plt.subplots()
ax.bar(
    range(2, die_max_value + 1), frequencies, edgecolor='white',
    linewidth=0.7
    )

# Set chart title and label axes.
ax.set_title("Die 1000 rolls", fontsize=24)
ax.set_xlabel("Die sides", fontsize=14)
ax.set_ylabel("Frequency", fontsize=14)

plt.show()