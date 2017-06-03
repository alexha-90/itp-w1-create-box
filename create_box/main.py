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

""" 
For an extra challenge, make it so only the outer border of the box shows and it is not filled in. Make this a separate function and add unit tests for it.

Oh, also-- Remember that when you have a for loop like `for w in range(5)` that `w` will take on the value of each number when your loop is going through, for example:
for w in range(5):
    print('W is: {}'.format(w))  # <-- Just formating the string here, plugging in the `w` variable to the {}'s inside the string

'W is: 0'
'W is: 1'
'W is: 2'
'W is: 3'
'W is: 4'

create_empty_box(5, 5, '*')
*****
*   *
*   *
*   *
*****
"""


