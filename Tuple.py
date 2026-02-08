'''🔹 Basic Level
- Create a tuple with 5 elements and:
- Print the first, last, and middle element.
- Try modifying one element — what happens?
- Convert a tuple into a list, modify it, and convert it back into a tuple.
- Write a program to find the length of a tuple without using len().
- Count how many times a specific element appears in a tuple.
- Find the index of an element in a tuple manually (without using index()).'''

'''🔹 Intermediate Level
- Given a tuple of numbers, find the sum and average.
- Write a program to reverse a tuple without using slicing.
- Concatenate two tuples and sort the result.
- Given a tuple of strings, find the longest and shortest string.
- Check if a tuple is palindromic (same forwards and backwards).'''

'''🔹 Advanced Level
- Write a program to flatten a nested tuple (e.g., ((1,2),(3,4),(5,)) → (1,2,3,4,5)).
- Implement a function to generate all possible subsets of a tuple.
- Given a tuple of numbers, find all pairs that sum to a target value.
- Write a program to zip two tuples together into a tuple of pairs.
- Implement a program to chunk a tuple into sub-tuples of size n.
- Solve the tuple unpacking challenge: Given a tuple (1, (2,3), (4,(5,6))),
extract all numbers into a flat tuple (1,2,3,4,5,6).
'''

#🔹 Basic Level
#- Create a tuple with 5 elements and:
#- Print the first, last, and middle element.
my_tuple = (10, 20, 30, 40, 50)
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])
print("Middle element:", my_tuple[len(my_tuple)//2])

# Try modifying one element — what happens?
try:
    my_tuple[0] = 100
except TypeError as e:
    print("Error:", e)

# Convert a tuple into a list, modify it, and convert it back into a tuple.
my_list = list(my_tuple)
my_list[0] = 100
my_tuple = tuple(my_list)
print("Modified tuple:", my_tuple)

# Write a program to find the length of a tuple without using len().
# def tuple_length(t):
#     count = 0
#     for _ in t:
#         count +=  1
#     return count
# print("Length of tuple:", tuple_length(my_tuple))

# Count how many times a specific element appears in a tuple.
def count_element(t, element):
    count = 0
    for item in t:
        if item == element:
            count += 1
    return count
print("Count of 30 in tuple:", count_element(my_tuple, 30))

# Find the index of an element in a tuple manually (without using index()).
def find_index(t, element):
    for i in range(len(t)):
        if t[i] == element:
            return i
    return -1
print("Index of 30 in tuple:", find_index(my_tuple, 30))

# 🔹 Intermediate Level
# Given a tuple of numbers, find the sum and average.

total_sum = sum(my_list)
average = total_sum / len(my_list)
print("Sum:", total_sum)
print("Average:", average)

# Write a program to reverse a tuple without using slicing.
def reverse_tuple(t):
    reversed_t = ()
    for item in t:
        reversed_t = (item,) + reversed_t
    return reversed_t
print("Reversed tuple:", reverse_tuple(my_tuple))

# Concatenate two tuples and sort the result.
tuple1 = (3, 1, 4)
tuple2 = (2, 5, 0)
concatenated = tuple1 + tuple2
sorted_tuple = tuple(sorted(concatenated))
print("Concatenated tuple:", concatenated)
print("Sorted concatenated tuple:", sorted_tuple)

# Given a tuple of strings, find the longest and shortest string.
string_tuple = ("apple", "banana", "kiwi", "cherry", "blueberry")
longest = max(string_tuple, key=len)
shortest = min(string_tuple, key=len)
print("Longest string:", longest)
print("Shortest string:", shortest)

# Check if a tuple is palindromic (same forwards and backwards).
def is_palindromic(t):
    return t == reverse_tuple(t)
palindrome_tuple = (1, 2, 3, 2, 1)
print("Is palindromic:", is_palindromic(palindrome_tuple))

# 🔹 Advanced Level
# Write a program to flatten a nested tuple (e.g., ((1,2),(3,4),(5,)) → (1,2,3,4,5)).
def flatten(nested_t):
    flat_t = ()
    for item in nested_t:
        if isinstance(item, tuple):
            flat_t += flatten(item)
        else:
            flat_t += (item,)
    return flat_t
nested_tuple = ((1,2),(3,4),(5,))
print("Flattened tuple:", flatten(nested_tuple))

# Implement a function to generate all possible subsets of a tuple.
def subsets(t):
    result = [()]
    for item in t:
        result += [subset + (item,) for subset in result]
    return result
print("Subsets of tuple:", subsets(my_tuple))

# Given a tuple of numbers, find all pairs that sum to a target value.
def find_pairs(t, target):
    pairs = []
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] + t[j] == target:
                pairs.append((t[i], t[j]))
    return pairs
print("Pairs that sum to 50:", find_pairs(my_tuple, 50))

# Write a program to zip two tuples together into a tuple of pairs.
def zip_tuples(t1, t2):
    return tuple(zip(t1, t2))
tuple_a = (1, 2, 3)
tuple_b = ('a', 'b', 'c')
print("Zipped tuples:", zip_tuples(tuple_a, tuple_b))

# Implement a program to chunk a tuple into sub-tuples of size n.
def chunk_tuple(t, n):
    return tuple(t[i:i + n] for i in range(0, len(t), n))
print("Chunked tuple:", chunk_tuple(my_tuple, 2))

# Solve the tuple unpacking challenge: Given a tuple (1, (2,3), (4,(5,6))),extract all numbers into a flat tuple (1,2,3,4,5,6).
def unpack_tuple(t):
    flat_t = ()
    for item in t:
        if isinstance(item, tuple):
            flat_t += unpack_tuple(item)
        else:
            flat_t += (item,)
    return flat_t
nested_tuple = (1, (2,3), (4,(5,6)))
print("Unpacked tuple:", unpack_tuple(nested_tuple))


