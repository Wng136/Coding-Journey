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
Moving onto variable naming
The x, y, and z shown above are examples of names assigned to the variables, which allows the computer to find and retrieve the assigned data
Another way of understanding it is that x is the label given to the storage compartment containing the number 1

Not only that, but there are also rules in naming these variables
Good Examples:
"""

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""
The naming rules strictly follow these:
- Must start with a letter or the underscore character
- Cannot start with a number
- Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Case-sensitive (age, Age, and AGE are three different variables)
- Cannot be any of the Python keywords

Any variable naming without following these rules produces errors
Bad Examples:
"""

#2myvar = "John" # Cannot start with numbers
#my-var = "John" # Cannot contain dash "-"
#my var = "John" # Cannot contain space " "


"""
Now that is the theoretical understanding of variables, but the practical wisdom in naming variables also holds great importance
For Example: 
"""

UserName = user_name = userName = "Paul" 
# There are many naming patterns (follow rules), but best to maintain a consistent naming pattern for cleanliness
UserAge = "60"

"""
It is recommended that the naming holds significance in showing the intent and functions of the variable
This is especially important in large programs with many variables 
so that other people and yourself working on the program would understand the program faster
Best to train to be accustomed to a familiar naming pattern
"""


"""
These theories and knowledge are fundamentals in handling variables in Python
From the above, it can be concluded that a name is assigned to a variable that contains data
as well as the rules and methods in utilising variables
"""





"""
Two additional functions for variables are casting and getting the data type of the variable

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

print(type(x)) # <class 'str'>
print(type(y)) # <class 'int'>
print(type(z)) # <class 'float'>
