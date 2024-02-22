import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename_dv = 'python_work/data_visualization/Chapter_16/data/death_valley_2018_simple.csv'
filename_sfna = 'python_work/data_visualization/Chapter_16/data/san_francisco_national_airport.csv'

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
            
# Read data from San - Francisco National Airoport.
with open(filename_sfna) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, and high and low temperatures from this file.
    sfna_dates, sfna_highs, sfna_lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            sfna_dates.append(current_date)
            sfna_highs.append(high)
            sfna_lows.append(low)
            
# Plot the high and low temperatures for Death Valley.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dv_dates, dv_highs, c='red', alpha=0.5, label='Death Valley Highs')
ax.plot(dv_dates, dv_lows, c='blue', alpha=0.5, label='Death Valley Lows')
ax.fill_between(dv_dates, dv_highs, dv_lows, facecolor='blue', alpha=0.1)

# Plot the high and low temperatures for San - Francisco National Airoport.
ax.plot(
    sfna_dates, sfna_highs, c='orange', alpha=0.5,
    label='San-Francisco NA Highs'
    )
ax.plot(
    sfna_dates, sfna_lows, c='green', alpha=0.5,
    label='San-Francisco NA Lows'
    )
ax.fill_between(sfna_dates, sfna_highs, sfna_lows, facecolor='green', alpha=0.1)

# Set y-axis limit to 150.
ax.set_ylim(bottom=None, top=150)

# Format plot.
title = ("Daily high and low temperatures - 2018 \n"
"Death Valley, CA vs 2023 San-Francisco National Airoport, CA")
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.legend()

plt.show()