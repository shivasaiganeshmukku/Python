'''🔹 Basic Level
- Create a dictionary with student names as keys and their marks as values.
- Print all keys, all values, and all key-value pairs.
- Write a program to check if a given key exists in a dictionary.
- Count the frequency of characters in a string using a dictionary.
- Merge two dictionaries into one.
- Find the maximum and minimum value in a dictionary (e.g., highest and lowest marks).
'''

'''🔹 Intermediate Level
- Given a dictionary of employees and their salaries, find the employee with the highest salary.
- Write a program to invert a dictionary (swap keys and values).
- Sort a dictionary by keys and by values.
- Create a dictionary from two lists: one of keys and one of values.
- Write a program to remove a key from a dictionary without using pop() or del.
'''

'''🔹 Advanced Level
- Implement a program to count word frequencies in a paragraph using a dictionary.
- Write a program to group a list of tuples into a dictionary.
- Example: [("a",1),("b",2),("a",3)] → {"a":[1,3],"b":[2]}
- Create a nested dictionary to store student details (name, age, marks).
- Write queries to access and update specific fields.
- Implement a program to find the intersection of two dictionaries (common keys with same values).
- Write a function to convert a dictionary into a list of tuples and back.
- Build a program that uses a dictionary to simulate a phone book with add, search, update, and delete operations.
'''
# Create a dictionary with student names as keys and their marks as values.
stu = {'shiva':90 , "sai":97 , "ganesh":98}
print(stu)

# Print all keys, all values, and all key-value pairs.
print(stu.keys())
print(stu.values())
print(stu.items())

# Write a program to check if a given key exists in a dictionary.
key = "sai"
if key in stu:
    print(f"{key} exists in the dictionary.")
else:    print(f"{key} does not exist in the dictionary.")

# Count the frequency of characters in a string using a dictionary.
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char]+= 1
        else:
            frequency[char] =1
    return frequency
s = "hello world"
print(char_frequency(s))

# Merge two dictionaries into one.
dict1 = {"a":1,"b":2}
dict2 ={"c":3,"d":4}
print(dict1|dict2)
# merge two dictionaries into one.
dict1 = {"a":1,"b":2}
dict2 ={"c":3,"d":4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# Find the maximum and minimum value in a dictionary (e.g., highest and lowest marks).
marks = {"shiva":90 , "sai":97, "ganesh":98}
max_marks = max(marks.values())
min_marks = min(marks.values())
print(f"highest marks:{max_marks}")
print(f"lowest marks:{min_marks}")

# Given a dictionary of employees and their salaries, find the employee with the highest salary.
salaries = {"Alice": 70000, "Bob": 85000, "Charlie": 60000}
highest_salary_employee = max(salaries, key=salaries.get)
print(f"Employee with the highest salary: {highest_salary_employee} with salary {salaries[highest_salary_employee]}")

# Write a program to invert a dictionary (swap keys and values).
original_dict = {"a": 1, "b": 2, "c":3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(inverted_dict)

# Sort a dictionary by keys and by values.
unsorted_dict = {"b": 2, "a": 1,"c":3}
sorted_by_keys = dict(sorted(unsorted_dict.items()))
sorted_by_values = dict(sorted(unsorted_dict.items()))
print("Sorted by keys:" , sorted_by_keys)
print("Sorted by values:" , sorted_by_values)

# Create a dictionary from two lists: one of keys and one of values.
keys = ["a","b","c"]
values = [1,2,3]
new_dict = dict(zip(keys, values))
print(new_dict)

# Write a program to remove a key from a dictionary without using pop() or del.
my_dict ={'a':1,'b':2,'c':3}
key_to_remove = 'b'
if key_to_remove in my_dict:
    my_dict[key_to_remove] = None
print(my_dict)

# Implement a program to count word frequencies in a paragraph using a dictionary.
def word_frequencies(paragraph):
    frequency = {}
    for word in paragraph.split():
        if word in frequency:
            frequency[word] += 1
        else:            frequency[word] = 1
    return frequency
paragraph = "hello world hello"
print(word_frequencies(paragraph))

# Write a program to group a list of tuples into a dictionary.
def group_tuples(tuples):
    grouped_dict = {}
    for key, value in tuples:
        if key in grouped_dict:
            grouped_dict[key].append(value)
        else:
            grouped_dict[key] = [value]
    return grouped_dict
tuples = [("a",1),("b",2),("a",3)]
print(group_tuples(tuples))

# Create a nested dictionary to store student details (name, age, marks).
students = {
    "student1": {"name": "Alice", "age": 20, "marks": 85 ,},
    "student2": {"name": "Bob", "age": 22, "marks": 90},
    "student3": {"name": "Charlie", "age": 21, "marks": 88}
}
print(students)

# Write queries to access and update specific fields.
print(students["student1"]["name"])  # Access name of student1
students["student2"]["marks"] = 95  # Update marks of student2
print(students)

# Implement a program to find the intersection of two dictionaries (common keys with same values).
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 4, "d": 5}
intersection = {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}
print(intersection)

# Write a function to convert a dictionary into a list of tuples and back.
def dict_to_tuples(d):
    return list(d.items())
def tuples_to_dict(tuples):
    return dict(tuples)
my_dict = {"a": 1, "b": 2, "c": 3}
tuples = dict_to_tuples(my_dict)
print(tuples)
converted_dict = tuples_to_dict(tuples)
print(converted_dict)

# Build a program that uses a dictionary to simulate a phone book with add, search, update, and delete operations.
phone_book = {}
def add_contact(name, number):
    phone_book[name] = number
def search_contact(name):
    return phone_book.get(name, "Contact not found")
def update_contact(name, number):
    if name in phone_book:
        phone_book[name] = number
    else:
        print("Contact not found")
def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
    else:
        print("Contact not found")
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
print(search_contact("Alice"))
update_contact("Alice", "111-222-3333")
print(search_contact("Alice"))
delete_contact("Bob")
print(search_contact("Bob"))

