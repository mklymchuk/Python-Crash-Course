import json

# Explore the structure of the data.
filename = 'python_work/data_visualization/Chapter_16/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    readable_file = 'python_work/data_visualization/Chapter_16/data/readable_eq_data.json'
    with open(readable_file, 'w') as f:
        json.dump(all_eq_data, f, indent=4)
    