What is the difference between list, tuple, and set?
1. List: A list is a mutable, ordered collection of items. It allows duplicate elements and can contain elements of different data types. Lists are defined using square brackets [].
Example:    
my_list = [1, 2, 3, 'hello', 3]
print(my_list)  # Output: [1, 2, 3, 'hello', 3]
2. Tuple: A tuple is an immutable, ordered collection of items. Like lists, tuples can contain duplicate elements and can hold different data types. Tuples are defined using parentheses ().
Example:    
my_tuple = (1, 2, 3, 'hello', 3)
print(my_tuple)  # Output: (1, 2, 3, 'hello)
3. Set: A set is a mutable, unordered collection of unique items. Sets do not allow duplicate elements and can contain elements of different data types. Sets are defined using curly braces {}.
Example:
my_set = {1, 2, 3, 'hello', 3}
print(my_set)  # Output: {1, 2, 3, 'hello'}
In summary, the main differences between lists, tuples, and sets are:
- Mutability: Lists and sets are mutable, while tuples are immutable.   
- Order: Lists and tuples maintain the order of elements, while sets do not.
- Duplicates: Lists and tuples can contain duplicate elements, while sets cannot.
- Syntax: Lists use square brackets [], tuples use parentheses (), and sets use curly braces {}.
