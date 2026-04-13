🔹 Basic Python Concepts
What are the key features of Python?
What is the difference between list, tuple, and set?
What are mutable and immutable data types?
Explain Python’s dynamic typing.
What is indentation in Python and why is it important?
What are Python keywords?
What is the difference between is and ==?
What is the difference between shallow copy and deep copy?
What are *args and **kwargs?
What is the difference between a function and a method?



what are the key features of Python?
   
1. Easy to Learn and Use: Python has a simple syntax that is easy to read and write, making it an excellent choice for beginners.
2. Interpreted Language: Python is an interpreted language, which means that code can be executed line by line, making debugging easier.
3. Dynamically Typed: Python does not require explicit declaration of variable types, allowing for more flexibility in coding.
4. Extensive Standard Library: Python has a large standard library that provides modules and functions for various tasks, such as file handling, regular expressions, and web development.
5. Cross-Platform Compatibility: Python can run on various operating systems, including Windows, macOS, and Linux, without requiring any modifications to the code.
6. Object-Oriented Programming: Python supports object-oriented programming (OOP) paradigms, allowing developers to create reusable and modular code.
7. High-Level Language: Python abstracts away many low-level details, making it easier for developers to focus on problem-solving rather than managing memory or other system-level tasks.
8. Large Community and Ecosystem: Python has a vast and active community that contributes to a wide range of libraries and frameworks, making it suitable for various applications, including web development, data analysis, machine learning, and more.

What is the difference between list, tuple, and set?
1. List: A list is an ordered collection of items that can be modified (mutable). It allows duplicate elements and is defined using square brackets [].
Example: 
```pythonmy_list = [1, 2, 3, 4, 5]
``` 
2. Tuple: A tuple is an ordered collection of items that cannot be modified (immutable). It allows duplicate elements and is defined using parentheses ().
Example:
```pythonmy_tuple = (1, 2, 3, 4, 5)
```
3. Set: A set is an unordered collection of unique elements. It does not allow duplicate elements and is defined using curly braces {}.
Example:
```pythonmy_set = {1, 2, 3, 4, 5}               
```     
What are mutable and immutable data types?
Mutable data types are those that can be modified after they have been created. Examples of mutable data types in Python include lists, dictionaries, and sets. You can change the contents of a mutable object without creating a new object.
Example of mutable data type:
```python       
my_list = [1, 2, 3]
my_list.append(4)  # Modifying the list by adding an element    
print(my_list)  # Output: [1, 2, 3, 4]
```
Immutable data types, on the other hand, cannot be modified after they have been created. Examples of immutable data types in Python include strings, tuples, and frozensets. If you want to change the contents of an immutable object, you need to create a new object.
Example of immutable data type:
```python   
my_string = "Hello"
new_string = my_string + " World"  # Creating a new string by concatenating
print(new_string)  # Output: "Hello World"
``` 
Explain Python’s dynamic typing.
Python's dynamic typing means that the type of a variable is determined at runtime, rather than being explicitly declared by the programmer. This allows for greater flexibility in coding, as you can assign different types of values to the same variable without causing errors. For example, you can assign an integer to a variable and later assign a string to the same variable without any issues.
Example of dynamic typing:
```python           
x = 5  # x is an integer
print(type(x))  # Output: <class 'int'>

x = "Hello"  # x is now a string
print(type(x))  # Output: <class 'str'>
```     
What is indentation in Python and why is it important?
Indentation in Python refers to the use of whitespace (spaces or tabs) at the beginning of a line of code to indicate the level of nesting or hierarchy in the code structure. It is important because it defines the scope of loops, functions, and other code blocks. Proper indentation is crucial for the correct execution of Python code, as it helps to visually organize the code and indicates which statements belong to which blocks. Incorrect indentation can lead to syntax errors or logical errors in the program.
Example of indentation:
```python
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")
greet("Alice")  # Output: Hello, Alice
greet("")  # Output: Hello, World!
```
What are Python keywords?
Python keywords are reserved words that have special meaning in the Python programming language. They cannot be used as identifiers (variable names, function names, etc.) because they are part of the syntax of the language. Python has a set of keywords that are used to define the structure and flow of the code. Some common Python keywords include:
- `if`: Used for conditional statements.
- `else`: Used for alternative execution paths in conditional statements.
- `elif`: Used for additional conditional checks in conditional statements.
- `for`: Used for creating loops that iterate over a sequence of items.
- `while`: Used for creating loops that continue until a condition is no longer true.
- `def`: Used for defining functions.
- `return`: Used for returning values from functions.
- `class`: Used for defining classes.
- `import`: Used for importing modules into the current namespace.
- `from`: Used in conjunction with `import` to specify which components to import from a module.    

What is the difference between is and ==?The `is` operator in Python checks for identity, meaning it checks whether two variables refer to the same object in memory. The `==` operator, on the other hand, checks for equality, meaning it checks whether the values of the objects being compared are equal, regardless of whether they are the same object in memory.
Example of `is` and `==`:
```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x == y)  # Output: True (x and y have the same values)
print(x is y)  # Output: True (x and y refer to the same object in memory)
print(x == z)  # Output: True (x and z have the same values)