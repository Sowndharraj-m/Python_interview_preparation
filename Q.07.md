Difference between is and == ?
The difference between "is" and "==" in Python is as follows:
- "==" checks for value equality. It checks whether the values of the objects being compared are equal. For example:
```
a = [1, 2, 3]
b = [1, 2, 3]   
print(a == b)  # Output: True
```
In this case, "a" and "b" have the same values, so "a == b" returns True.
- "is" checks for identity. It checks whether the two operands refer to the same object in memory. For example:
```
print(a is b)  # Output: False
``` 
In this case, "a" and "b" are two different objects in memory, even though they have the same values. Therefore, "a is b" returns False.    
