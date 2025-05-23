import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_indexes(header_row):
    """Get indexes for TMIN and TMAX columns."""
    tmin_index = header_row.index('TMIN')
    tmax_index = header_row.index('TMAX')
    return tmin_index, tmax_index

def plot_temperatures(filename):
    """Plot high and low temperatures from the given CSV file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        
        # Get indexes for TMIN and TMAX columns.
        tmin_index, tmax_index = get_indexes(header_row)
        
        # Get station name.
        station_name = next(reader)[1]
        
        # Get dates, highs, and lows from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                high = int(row[tmax_index])
                low = int(row[tmin_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
                
        # Plot the high and low temperatures.
        plt.style.use('classic')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red', alpha=0.5, label='Highs')
        ax.plot(dates, lows, c='blue', alpha=0.5, label='Lows')
        ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
        
        # Set y-axis limit to 150.
        ax.set_ylim(bottom=None, top=150)
        
        # Format plot
        title = f"Daily High and Low Temperatures - {station_name}"
        ax.set_title(title, fontsize=20)
        ax.set_xlabel('Date', fontsize=16)
        ax.set_ylabel("Temperature (F)", fontsize=16)
        ax.tick_params(axis='both', which='major', labelsize=16)
        ax.legend()
        
        # Rotate x-axis labels to a diagonal position
        fig.autofmt_xdate(rotation=45)
        
        plt.show()

# Example usage
filename = 'python_work/data_visualization/Chapter_16/data/sitka_weather_2018_simple.csv'
plot_temperatures(filename)
