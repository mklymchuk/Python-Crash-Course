import csv 

from plotly.graph_objs import Scatter, Layout
from plotly import offline

filename = 'python_work/data_visualization/Chapter_16/data/world_fires_1_day.csv'

# Read data from file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get longtitude, latitude and the brightness of each fire.
    lats, longs, brights = [], [], []
    for row in reader:
        try:
            lat = float(row[0])
            long = float(row[1])
            bright = float(row[2])
        except ValueError:
            print(f"Missing Value: {row}")
        else:
            lats.append(lat)
            longs.append(long)
            brights.append(bright)
            
# Map the world fires.
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'marker': {
        'size': [bright/50 for bright in brights],
        'color': brights,
        'colorscale': 'Reds',
        'reversescale': True,
        'colorbar': {'title': 'Brightness of fire'}
    }
}]

file_title = 'Brightness of fires'
my_layout = Layout(title=file_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')