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
print(create_box(3, 4, '*'))
print(create_box(2, 2, '@'))


# create_box(4, 3, '$')

"""
for h in range(4):  # 2
    for w in range(3):   # 0
        empty_box += '$'
    empty_box += '\n'
    
empty_box == '$$$\n$$$\n'
"""


"""
def create_box(height, width, character):
    character = ''
    for h in range(height):
        height += character
        for w in range(width):
            width += character
            return(width)

print(create_box(3, 4, '*'))

      


def create_box(height, width, character):
    empty_box = ''
    for h in range(height):
        return height += character + empty_box
        for w in range(width):
            return width += character + empty_box
create_box(height, width, character)
print(create_box(height, width, character))


for num1 in range(5):
    print("outer loop" + str(num1))
    for num2 in range(2):
      print("inner loop" + str(num2))
      
new_string = ""
for _ in range(5):
  new_string += "*"

print(new_string)

#  \n = new string.   Project today not printing, it's returning. Return in one string all at once.





def create_box(height, width, character):
    for:
        #insert code here
    for:
        #insert code here
    return #results    
    

if __name__ == '__main__':
    create_box(3, 4, '*')
    
    
    
def create_box(height, width, character):
  for x in str(height):
    if height > 0: 
      height = height * str(character)
      width = width * str(character)
      combo = "%s\n%s" % (height, width)
      return(combo) 
"""