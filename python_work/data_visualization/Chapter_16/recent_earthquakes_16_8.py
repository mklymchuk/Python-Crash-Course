import json

from plotly.graph_objs import Scatter, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'python_work/data_visualization/Chapter_16/data/eq_data_26_01_2024_26_02_2024.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    readable_file = 'python_work/data_visualization/Chapter_16/data/readable_eq_data_26_01_2024_26_02_2024.json'
    with open(readable_file, 'w') as f:
        json.dump(all_eq_data, f , indent=4)
        
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hower_text = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hower_text.append(eq_dict['properties']['title'])
    
# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hower_text,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Reds',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]

file_title = all_eq_data['metadata']['title']
my_layout = Layout(title=file_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_26_01_2024_26_02_2024.html')