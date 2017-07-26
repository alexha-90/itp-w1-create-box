"""This is the entry point of the program."""
""" Alex Ha and James Curbow """

def create_box(height, width, character):
    if height <= 0 or width <= 0:
        return 'invalid parameters'
    empty_box = ''
    for h in range(height):
        for w in range(width):
            empty_box += character 
        empty_box += '\n'
    return empty_box
print(create_box(3, 4, '*'))
print(create_box(2, 2, '@'))


