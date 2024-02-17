import matplotlib.pyplot as plt
from die import Die

# Create a die
die_1 = Die()

# Make some rolls
results = []
for roll_num in range(1000):
    result = die_1.roll()
    results.append(result)
    
# Analyze the rezults.
frequencies = []
for value in range (1, die_1.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
fig, ax = plt.subplots()
ax.plot(results, linewidth = 3)

# Set chart title and label axes.
ax.set_title("Die 1000 rolls", fontsize = 24)
ax.set_xlabel("Roll number",  fontsize = 14)
ax.set_ylabel("Die sides",  fontsize = 14)
plt.show()