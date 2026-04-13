What is indentation in Python and why is it important?

Indentation is the space/tab used to define code blocks in Python.

It replaces {} used in other languages
It is mandatory
Incorrect indentation → IndentationError
Example:
if True:
    print("This is indented correctly.")
    if False:
        print("This will not be printed.")
else:
    print("This is not indented correctly.")  # This will cause an IndentationError