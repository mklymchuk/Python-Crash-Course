glossary = {'concatenation':'the action of linking things together in a series',
            'integer':'a whole number (not a fractional number) that can be positive, negative, or zero',
            'float':'a positive or negative whole number with a decimal point',
            'list':'lists are used to store multiple items in a single variable',
            'if-elif-else':'the if...else statement is used to execute a block of code among two alternatives',}

for glossary_value in glossary:
    print(f"\n{glossary_value.title()} - \n {glossary[glossary_value]}")