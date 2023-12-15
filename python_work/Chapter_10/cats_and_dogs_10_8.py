"""Program open .txt files"""

def open_file(filename):
    """Open .txt file, and if file not presented - throw exception"""
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File is not found {filename}")
    else:
        print(contents)

filenames = ['txt/cats.txt', 'txt/dogs.txt']

for filename in filenames:
    open_file(filename)