import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'python_work/data_visualization/Chapter_16/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates, and amount of rainfall.
    dates, rainfalls = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rainfalls.append(rain)
            
# Plot rainfalls.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, c = 'blue', alpha = 0.5)

# Format plot.
title = "Daily rainfall amounts - 2018 \nSitka Alaska"
ax.set_title(title, fontsize = 20)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfalls mm", fontsize = 16)
ax.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()