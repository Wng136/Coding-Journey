"""
Topic: Variables

Today I learned:

Variables are like storage compartments that store specific kind of data
It can store numbers and texts

For example:
"""

x = 1
y = "Good Wednesday!"

"""
From the example, assigning data can be done by (variable name) = (Data), 
where x is a name assigned for the variable whereas 1 is the data assigned to the variable
This method is the most common and direct
"""

x, y, z = "Monday", "Tuesday", "Friday"

"""
This method allows data to be assigned to its respective variable
It produces the same thing as x = "Monday", y =  "Tuesday", z = "Wednesday" 
"""

x = y = z = "Unity"

"""
All variables can also be assigned the same data, "Unity"
"""

"""
Moving onto the variable naming
The x, y, and x shown above are exmaples of names assigned to the variables, which allows the computer to find and retrieve the assigned data
Another way of understanding it, is that x is the label given to the storage compartment consisting the number 1

Not only that, there are also rules in naming these variables
Good Examples:
"""

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""
The naming rules strictly follows these:
- Must start with a letter or the underscore character
- Cannot start with a number
- Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Case-sensitive (age, Age and AGE are three different variables)
- Cannot be any of the Python keywords

Any variable namings without following these rules produces errors
Bad Examples:
"""

#2myvar = "John" # Cannot start with numbers
#my-var = "John" # Cannot contain dash "-"
#my var = "John" # Cannot contain space " "


"""
Now that is the theoretical understanding of variables, but the practical wisdom in naming variable also holds great importance
For Example: 
"""

UserName = user_name = userName = "Paul" 
# There are many naming pattern (follows rules) but best to maintain consistant naming pattern for cleanliness
UserAge = "60"

"""
It is recommended that the naming holds significance in showing the intent, and functions of the variable
This is escpecially important in large programs with many variables 
so that other people and yourself working on the program would understand the program faster
Best to train to be accustom to a familiar naming pattern
"""


"""
These theory and knowledge are fundamentals in handling variables in Python
from the above it can be concluded, that a name is assigned to a variable that contains data
as well as the rules and method in utilising variables
"""





"""
Another two aditional function for variables are casting and getting the data type of the variable

Casting is used to specify the data type of the variable
For Example:
"""

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

a = int("Hello") # but of course text cannot be specified as int() and float() unlike numbers itself

"""
Another function is printing out the data type of the variable
For Example:
"""

print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>
print(type(z)) # <class 'float'>
