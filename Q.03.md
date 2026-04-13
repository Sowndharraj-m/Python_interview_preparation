What are mutable and immutable data types?
1. Mutable Data Types: Mutable data types are those that can be modified after they have been created. Examples of mutable data types in Python include lists, dictionaries, and sets. You can change the contents of a mutable object without creating a new object.
Example:
my_list = [1, 2, 3]
my_list.append(4)   
print(my_list)  # Output: [1, 2, 3, 4]
2. Immutable Data Types: Immutable data types are those that cannot be modified after they have been created. Examples of immutable data types in Python include strings, tuples, and frozensets. If you want to change the contents of an immutable object, you need to create a new object.
Example:
my_string = "Hello"
new_string = my_string + " World"
print(new_string)  # Output: "Hello World"
print(my_string)  # Output: "Hello"