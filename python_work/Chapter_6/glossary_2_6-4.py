glossary = {'concatenation':'the action of linking things together in a series',
            'integer':'a whole number (not a fractional number) that can be positive, negative, or zero',
            'float':'a positive or negative whole number with a decimal point',
            'list':'lists are used to store multiple items in a single variable',
            'if-elif-else':'the if...else statement is used to execute a block of code among two alternatives',
            'argument':'A value passed to a function (or method) when calling the function. ',
            'asynchronous context manager':'An object which controls the environment seen in an async with statement by defining __aenter__() and __aexit__() methods. Introduced by PEP 492.',
            'attribute':'A value associated with an object which is usually referenced by name using dotted expressions.',
            'awaitable':'An object that can be used in an await expression. ',
            'BDFL':'Benevolent Dictator For Life, a.k.a. Guido van Rossum, Python’s creator.'
            }

for word,meaning in glossary.items():
    print(f"\n{word.title()} - \n {meaning}")