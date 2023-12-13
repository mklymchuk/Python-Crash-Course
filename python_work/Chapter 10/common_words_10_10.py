"""Program read files, and counts 'the ' """

def read_file(filename):
    """Read file and count 'the ' """
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"The appears {contents.lower().count('the ')}")

filenames = ['txt/I_bring_fresh_flowers.txt', 'txt/star_chamber.txt', 'txt/utopia?_never!.txt']

for filename in filenames:
    read_file(filename)