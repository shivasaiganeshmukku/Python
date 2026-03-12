'''s="hello world"
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])'''

'''str = "coding is fun!"
print(str.upper())
print(len(str))
print(str.lower())
print(str.strip())
print(str.replace('o','y'))
print(str.isalnum())
print(str.isalpha())
print(str.isdigit())
print(str.isupper())
print(str.isspace())
print(str.capitalize())
print(str.title())'''



#vowels count
'''s = "shiva sai ganesh"
a = (s.count("a"))
e = (s.count("e"))
i = (s.count("i"))
u = (s.count("u"))
o = (s.count("o"))
print(f"number of vowels:{a,e,i,o,u}")'''

#grade calculator
''''
m = int(input("marks in maths: "))
e = int(input("marks in english: "))
s = int(input("marks in science: "))

total_marks = m+e+s
average = total_marks/3
percentage = total_marks/3
grade=" "
if percentage >90:
    grade="A"

elif percentage>80 :
    grade="B"
elif percentage>70 :
    grade="c"

else:
    grade= "f"
print(f"total_marks:{total_marks}\n average:{average}\n grade: {grade}")'''

#Palindrome
'''''
's = input("Enter: ")
r = s[::-1]
if r ==s :
    print("It is a palindrome. ")

else :
    print("It is not a palindrome.") '''
#largest three numbers
'''
a = input()
x,y,z = a.split(",")
num1 = int(x)
num2 = int(y)
num3 = int(z)
great =""
if num1>num2:
    if num1>num3:
        great=num1
    else:
        great=num3
elif num2>num1:
    if num2>num3:
        great = num2
    else :
        great=num3
        
elif num3>num1:
        if num3>num2:
            great=num3
        else:
            great=num2
print(great)
'''
#leapyear checker
'''year = int(input("Enter year: "))
leap = False
if year % 100 == 0 and year % 400 != 0:
    leap = False
elif year % 4 == 0:
    leap = True
else:
    leap = False
print(leap)
'''

"""Beginner Level
- Reverse a string without using built-in functions.
- Check if a string is a palindrome.
- Count vowels and consonants in a string.
- Find the frequency of each character in a string.
- Remove all duplicate characters from a string.
Intermediate Level
- Find the longest word in a sentence.
- Write a function to check if two strings are anagrams.
- Convert a string to title case (capitalize first letter of each word).
- Find the first non-repeating character in a string.
- Implement substring search (without using in or built-in methods).
Advanced Level- Implement the KMP algorithm for pattern matching.
- Find the longest palindromic substring in a given string.
- Compress a string using run-length encoding (e.g., "aaabbc" → "a3b2c1").
- Generate all permutations of a string.
- Implement a function to check if a string can be segmented into valid dictionary words (Word Break Problem).
"""

# Reverse a string without using built-in functions.
def reverse_string(s):
    reversed_str = ""
    for i in range(len(s)-1, -1, -1):
        reversed_str += s[i]
    return reversed_str
input_str = "hello"
print(reverse_string(input_str))

# Check if a string is a palindrome.
def str_palindrome(s):
    r = s[::-1]
    if r == s:
        return "it is a palindrome"
    else:
        return "not a palindrome"
    return r
r = "madam"
print(str_palindrome(r))

# Count vowels and consonants in a string.
def count_vowels_and_consonants(s):
    vowels = 0
    consonants = 0
    vowel_list = "aeiouAEIOU"
    for char in s:
        if char in vowel_list:
            vowels += 1
        elif char.isalpha():
            consonants += 1
    print(f"count of vowels {vowels}")
    print(f"count of consonants {consonants}")
s = "mom"
print(count_vowels_and_consonants(s))

# Find the frequency of each character in a string.
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    for char, count in frequency.items():
        print(f"{char}: {count}")
    return frequency
input_str = "hello world"
print(char_frequency(input_str))

# Remove all duplicate characters from a string.
def remove_duplicates(s):
    unique_chars = ""
    for chr in s:
        if chr not in unique_chars:
            unique_chars += chr
    return unique_chars
input_str = "Shivasaiganesh"
print(remove_duplicates(input_str))

# Find the longest word in a sentence.
def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
input_str = "i am a student."
print(longest_word(input_str))

# Write a function to check if two strings are anagrams.

def is_anagram( s1 , s2):
    if len(s1) != len(s2):
        return False
    dict1 = {}
    dict2 = {}
    for char in dict1:
        if char in dict1:
            dict1[char] =+ 1
        else:
            dict2[char] = 1
    for char in dict2:
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1
    return dict1 == dict2
s1 = "mumma"
s2 = "mamum"
print(f"is anagram: {is_anagram(s1,s2)}")

# Convert a string to title case (capitalize first letter of each word).
def to_title_case(s):
    words = s.split()
    print(words)
    title_cased = ""
    for word in words:
        new_word = word[0].upper() + word[1:].lower()
        title_cased += new_word + " "
    return title_cased.strip()
input_str = "i am learning python."
print(to_title_case(input_str))

# Find the first non-repeating character in a string.
def first_non_repeating(string):
    char_frequency = {}
    for char in string:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    for char in string:
        if char_frequency[char] == 1:
            return char
input_str = "swiss"
print(first_non_repeating(input_str))

# Implement substring search (without using in or built-in methods).
def substring_search(string, substring):
    len_string = len(string)
    len_substring = len(substring)
    if len_substring > len_string:
        return False
    for i in range(len_string - len_substring + 1):
        match = True
        for j in range(len_substring):
            if string[i + j] != substring[j]:
                match = False
                break
        if match:
            return True
    return False
string = "hello world"
substring = "world"
print(substring_search(string, substring))


# Compress a string using run-length encoding (e.g., "aaabbc" → "a3b2c1").
def run_length_encoding(s):
    if not s:
        return ""
    encoded = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += s[i - 1] + str(count)
            count = 1
    encoded += s[-1] + str(count)
    return encoded
input_str = "aaabbc"
print(run_length_encoding(input_str))

