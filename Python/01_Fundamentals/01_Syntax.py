"""
Topic: Syntax

Today I learned:

1. Indentation is important not only for readability but also to indicate a block of code
- (A block of code is a group of statements that are executed together as a single unit.)
For Example:
"""""

if 5 > 2:
    print("Five is greater than two.")
    # With this indentation, the system would recognise
    # it as a code block and execute the print statement
    # (The print statement is in the code block but not the if statement) 

if 5 > 2:
print("Five is greater than two.")
# However, without the indentation there would be an error



"""
2. Comments are useful for in-code documentation
- it is started by '#' and would not affect the execution of the code
For Example:
"""

# Comments can be placed at any line
if 5 > 2: # But it must be input after the statements
    print("Five is greater than two.") # Comment would not be printed
                # Comment can be input at any indentation level



"""
3. Statements are instructions that are executed by a computer
- There are many types of statements that bring about different outputs
For Example:
"""

print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")
# Stacking statements would allow the computer to print from the top to bottom



"""
4. Semicolons are useful to combine multiple statements into one line
For Example:
"""

print("Hello World!"); print("Have a good day."); print("Learning Python is fun!")
# Generally not recommended since it reduces readability and makes it look cramped
# And functions the same as multiple statement lines like the example above

