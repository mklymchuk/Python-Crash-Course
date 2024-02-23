import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename_dv = 'python_work/data_visualization/Chapter_16/data/death_valley_2018_simple.csv'
filename_sfna = 'python_work/data_visualization/Chapter_16/data/san_francisco_national_airport.csv'

# Read data from Death Valley file
with open(filename_dv) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get high and low temperatures from this file.
    dv_highs, dv_lows = [], []
    for row in reader:
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for row: {row}")
        else:
            dv_highs.append(high)
            dv_lows.append(low)

# Read data from San Francisco National Airport file
with open(filename_sfna) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get high and low temperatures from this file.
    sfna_highs, sfna_lows = [], []
    for row in reader:
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for row: {row}")
        else:
            sfna_highs.append(high)
            sfna_lows.append(low)

# Plot the high and low temperatures for both locations
plt.style.use('classic')
fig, ax = plt.subplots()
dv_index = range(1, len(dv_highs) + 1)
sfna_index = range(1, len(sfna_highs) + 1)

ax.plot(dv_index, dv_highs, c='red', alpha=0.5, label='Death Valley Highs')
ax.plot(dv_index, dv_lows, c='blue', alpha=0.5, label='Death Valley Lows')
ax.fill_between(dv_index, dv_highs, dv_lows, facecolor='blue', alpha=0.1)

ax.plot(sfna_index, sfna_highs, c='orange', alpha=0.5, label='San Francisco NA Highs')
ax.plot(sfna_index, sfna_lows, c='green', alpha=0.5, label='San Francisco NA Lows')
ax.fill_between(sfna_index, sfna_highs, sfna_lows, facecolor='green', alpha=0.1)

# Set y-axis limit to 150.
ax.set_ylim(bottom=None, top=150)

# Set x-axis limit to 365.
ax.set_xlim(1, 365)

# Format plot
title = "Daily high and low temperatures - Death Valley, CA vs San Francisco National Airport, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('Data Point', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.legend()

plt.show()
