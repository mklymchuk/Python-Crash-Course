import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename_dv = 'python_work/data_visualization/Chapter_16/data/death_valley_2018_simple.csv'
filename_s = 'python_work/data_visualization/Chapter_16/data/sitka_weather_2018_simple.csv'

# Read data from Death Valley file
with open(filename_dv) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dv_dates, dv_highs, dv_lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dv_dates.append(current_date)
            dv_highs.append(high)
            dv_lows.append(low)
            
# Read data from Sitka file.
with open(filename_s) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, and high and low temperatures from this file.
    s_dates, s_highs, s_lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            s_dates.append(current_date)
            s_highs.append(high)
            s_lows.append(low)

# Plot the high and low temperatures for Death Valley.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dv_dates, dv_highs, c='red', alpha=0.5, label='Death Valley Highs')
ax.plot(dv_dates, dv_lows, c='blue', alpha=0.5, label='Death Valley Lows')
ax.fill_between(dv_dates, dv_highs, dv_lows, facecolor='blue', alpha=0.1)

# Plot the high and low temperatures for Sitka
ax.plot(s_dates, s_highs, c='orange', alpha=0.5, label='Sitka Highs')
ax.plot(s_dates, s_lows, c='green', alpha=0.5, label='Sitka Lows')
ax.fill_between(s_dates, s_highs, s_lows, facecolor='green', alpha=0.1)

# Set y-axis limit to 150.
ax.set_ylim(bottom=None, top=150)

# Format plot.
title = "Daily high and low temperatures - 2018 \nDeath Valley, CA vs Sitka, AK"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.legend()

plt.show()
