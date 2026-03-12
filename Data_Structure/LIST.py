''' Basic Level
- Create a list of 10 numbers and:
- Print the first, last, and middle element.
- Reverse the list without using reverse() or slicing.
- Write a program to find the sum and average of elements in a list.
- Count how many times a specific element appears in a list.
- Remove duplicates from a list without using set().
- Find the maximum and minimum element in a list manually (without max() or min()).'''


'''Intermediate Level
- Given a list of integers, separate them into even and odd lists.
- Rotate a list by k positions (e.g., [1,2,3,4,5] rotated by 2 → [4,5,1,2,3]).
- Write a program to flatten a nested list (e.g., [[1,2],[3,4],[5]] → [1,2,3,4,5]).
- Find the second largest and second smallest number in a list.
- Implement a program to check if a list is palindromic (same forwards and backwards).'''

'''🔹 Advanced Level
- Implement your own version of list comprehension using loops.
- Write a program to generate all possible subsets of a list.
- Given a list of numbers, find all pairs that sum to a target value.
- Implement a program to merge two sorted lists into one sorted list (without using sorted()).
- Solve the Josephus Problem using lists (elimination game where every k-th person is removed until one remains).
- Write a function to chunk a list into sub lists of size n.
'''
# Create a list of 10 numbers and :
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Print the first, last, and middle element.
print(lst)

# Print the first, last, and middle element.
print("First Element ", lst[0])
print("Last Element" , lst[-1])
print("Middle Element", lst[len(lst)//2])
# Reverse the list without using reverse() or slicing.
reversed_lst = []
for i in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[i])
print("Reversed List:", reversed_lst)

#Write a program to find the sum and average of elements in a list.
for i in lst:
    sum = 0
    sum +=  i
    average = sum/len(lst)

print("Sum of elements in the list:", sum)
print("Average of elements in the list:", average)

# Count how many times a specific element appears in a list.
specific_element = 5
count = lst.count(specific_element)
print(f"The element {specific_element} appears {count} times in the list.")

# Remove duplicates from a list without using set().
#using dictionary from keys()
lst= list(dict.fromkeys(lst))
print(f"using dictionary fromkeys {lst}")

#using set()
print(f"Using the set{set(lst)} ")
#using a loop
res = []
for x in lst:
    if x not in res:
        res.append(x)
print(f"Using a loop {res}")

res=[]
[res.append(x) for x in lst if x not in res]
print(f"using the list comprehension{res}")


# Find the maximum and minimum element in a list manually (without max() or min()).
max_element = lst[0]
min_element = lst[0]
for num in lst:
    if num > max_element:
        max_element = num
    if num < min_element:
        min_element = num
print("Maximum element in the list:", max_element)
print("Minimum element in the list:", min_element)

# Given a list of integers, separate them into even and odd lists.
# for x in lst:
#     if x % 2 ==0:
#         print(f"even = {x}")
#     else:
#         print(f"Odd = {x}")
even_lst =[]
odd_lst =[]
for x in lst:
    if x % 2 == 0:
        even_lst.append(x)
    else:
        odd_lst.append(x)
print(f"Even List: {even_lst}")
print(f"Odd List: {odd_lst}")

# Rotate a list by k positions (e.g., [1,2,3,4,5] rotated by 2 → [4,5,1,2,3]).
def rotate_list(lst, k):
    k = k % len(lst) # Handle cases where k is greater than the list length
    return lst[-k:] + lst[:-k]
original_list = [1, 2, 3, 4, 5]
k = 2
rotated_list = rotate_list(original_list, k)
print(f"Original List: {original_list}")
print(f"Rotated List by {k} positions: {rotated_list}")

# Write a program to flatten a nested list (e.g., [[1,2],[3,4],[5]] → [1,2,3,4,5]).
def flatten_list(nested_list):
    flat = []
    for sublist in nested_list:
        for item in sublist:
            flat.append(item)
    return flat
nested_list = [[1, 2], [3, 4], [5]]
flattened_list = flatten_list(nested_list)
print(f"Nested List: {nested_list}")
print(f"Flattened List: {flattened_list}")

#  Find the second largest and second smallest number in a list.
def second_largest_smallest(lst):
    if len(lst) < 2:
        return None, None
    first_largest = second_largest = float('-inf')
    first_smallest = second_smallest = float('inf')
    for num in lst:
        if num > first_largest:
            second_largest = first_largest
            first_largest = num
        elif first_largest > num > second_largest:
            second_largest = num
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif first_smallest < num < second_smallest:
            second_smallest = num
    return second_largest, second_smallest
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
second_largest, second_smallest = second_largest_smallest(numbers)
print(f"Second Largest: {second_largest}")
print(f"Second Smallest: {second_smallest}")

# Implement a program to check if a list is palindromic (same forwards and backwards).
def is_palindrome(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return lst == reversed_lst

test_list = [1, 2, 3, 2, 1]
if is_palindrome(test_list):
    print("The list is palindromic.")
else:
    print("The list is not palindromic.")

# Implement your own version of list comprehension using loops.
original_list = [1, 2, 3, 4, 5]
squared_list = []
for x in original_list:
    squared_list.append(x ** 2)
print(f"Original List: {original_list}")
print(f"Squared List using loops: {squared_list}")

#  Write a program to generate all possible subsets of a list.
def generate_subsets(lst):
    subsets = [[]]
    for element in lst:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [element])
        subsets.extend(new_subsets)
    return subsets

original_list = [1, 2, 3]
all_subsets = generate_subsets(original_list)
print(f"All Subsets of {original_list}: {all_subsets}")

# Given a list of numbers, find all pairs that sum to a target value.
def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs
numbers = [1, 2, 3, 4, 5]
target_sum = 5
pairs = find_pairs(numbers, target_sum)
print(f"Pairs that sum to {target_sum}: {pairs}")

# Implement a program to merge two sorted lists into one sorted list (without using sorted()).
def merge_sorted_lists(lst1, lst2):
    merged = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    while i < len(lst1):
        merged.append(lst1[i])
        i += 1
    while j < len(lst2):
        merged.append(lst2[j])
        j += 1
    return merged
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = merge_sorted_lists(list1, list2)
print(f"Merged Sorted List: {merged_list}")

# Solve the Josephus Problem using lists (elimination game where every k-th person is removed until one remains).
def josephus(n, k):
    people = list(range(1, n + 1))
    index = 0
    while len(people) > 1:
        index = (index + k - 1) % len(people)
        people.pop(index)
    return people[0]
n = 7  # Number of people
k = 3  # Step count
survivor = josephus(n, k)
print(f"The survivor is person number {survivor}.")

# Write a function to chunk a list into sub lists of size n.
def chunk_list(lst, n):
    chunks = []
    for i in range(0, len(lst), n):
        chunks.append(lst[i:i + n])
    return chunks
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
chunked_list = chunk_list(original_list, chunk_size)
print(f"Original List: {original_list}")
print(f"Chunked List (size {chunk_size}): {chunked_list}")