from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 die.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store result in a list
results = []
for roll_num in range(1_000_000):
    # Multiplication instead of sum
    result = die_1.roll() * die_2.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
# Max result will be a result of two sides multiplication 
max_result = die_1.num_sides * die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title = 'Result of rolling and multiplication of two D6 dice, 1000000 times',
                   xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'd6_d6_mult.html')