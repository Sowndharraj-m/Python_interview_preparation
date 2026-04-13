if True:
     print("This is indented correctly.")
     if False:
       print("This will not be printed.")
else:
    print("This is not indented correctly.")  # This will cause an IndentationError