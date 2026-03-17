'''🟢 Basic Level
- Write a program to create a text file and write a few lines into it.
- Read the contents of a file and print them line by line.
- Count the number of words, characters, and lines in a file.
- Copy the contents of one file into another.
- Append new text to an existing file without overwriting.

🟡 Intermediate Level
- Write a program to reverse the contents of a file (line order or character order).
- Find and replace a given word in a file.
- Merge two files into a single file.
- Read a CSV file and display it in a formatted table.
- Write a program to store student records (name, roll number, marks) in a file and retrieve them.

🔵 Advanced Level
- Implement a log file system that records every action with timestamps.
- Create a program that reads a large file and splits it into smaller chunks.
- Implement a program to serialize and deserialize objects (e.g., using JSON or pickle in Python).
- Build a program to index words in a file (like a mini search engine).
- Handle binary files: store and retrieve images or other non-text data.
- Implement a program that tracks file changes (modified, deleted, added) in a directory.
- Create a program that compresses and decompresses files using algorithms (e.g., Huffman coding).
'''

#  Write a program to create a text file and write a few lines into it.
'''def create_file(filename):
    try:
        with open(filename,"w") as f:
            f.write("This is python file.\n")
            f.write("File Handling in python. \n")
            f.write("In Python using the exception and file handling.\n")
            print(f"File{filename} created and written successfully.")
    except Exception as e:
        print("Error creating file: ",e)
create_file("file.txt")'''
#  Read the contents of a file and print them line by line.
'''def read_file(filename):
    try:
        with open(filename, "r") as f:
            print("Reading file contents:")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("Error: File not found.")
read_file("file.txt")'''

# Count the number of words, characters, and lines in a file.
'''def count_file_stats(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
        print(f"Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}")
    except FileNotFoundError:
        print("Error: File not found.")

count_file_stats("file.txt")'''

# Copy the contents of one file into another.
'''def copy_file(source, destination):
    try:
        with open(source,"r") as src, open(destination ,"w") as dest:
            dest.write(src.read())
            print(f"contents copied from {source} to destination {destination}.")
    except FileNotFoundError:
        print("Error : file not found")
copy_file("file.txt","folder.txt")'''


# Append new text to an existing file without overwriting.
'''def append_to_file(filename, text):
    try:
        with open(filename, "a") as f:
            f.write("\n" + text)
        print(f"Text appended to '{filename}'.")
    except Exception as e:
        print("Error appending to file:", e)
append_to_file("file.txt", "This  is newly added text.")'''

# 🟡 Intermediate Level
# - Write a program to reverse the contents of a file (line order or character order).
'''try:
    # Step 1: Open the input file in read mode
    with open("input.txt", "r") as infile:
        # Step 2: Read all lines into a list
        lines = infile.readlines()

    # Step 3: Reverse the list of lines
    reversed_lines = lines[::-1]

    # Step 4: Open the output file in write mode
    with open("output.txt", "w") as outfile:
        # Step 5: Write the reversed lines into the new file
        outfile.writelines(reversed_lines)

except FileNotFoundError:
    # Step 6: Handle case where file does not exist
    print("Error: The file was not found.")

except Exception as e:
    # Step 7: Handle any other unexpected errors
    print("Error:", e)

finally:
    # Step 8: Always runs, whether successful or not
    print("Execution complete")'''

# - Find and replace a given word in a file.
'''try:
    with open("file.txt", "r") as file:
            content = file.read()
            #Ask user for the word to find and replace the word
            oldword = input("Enter the word to find:")
            newword = input("Enter the word to replace: ")
            # perfrom the replacement
            updated_contents = content.replace(oldword , newword)
            #open the file in write mode
            with open ("file.txt", "w") as f:
                f.write(updated_contents)
                print("Word replaced successfully.")
except FileNotFoundError :
        print("Error: file not found")
except Exception as e:
        print("Error: ",e)
finally:
        print("Executed successfully.")'''

# Merge two files into a single file.
'''try:
    # Step 1: Open the first file in read mode
    with open("file.txt", "r") as f1:
        contents1 = f1.read()

    # Step 2: Open the second file in read mode
    with open("folder.txt", "r") as f2:
        contents2 = f2.read()

    # Step 3: Open the output file in write mode
    with open("merged.txt", "w") as fout:
        # Step 4: Write contents of both files into the new file
        fout.write(contents1 + "\n" + contents2)

    print("Files merged successfully into 'merged.txt'.")

except FileNotFoundError as e:
    print("Error: One of the files was not found.", e)

except Exception as e:
    print("Error:", e)

finally:
    print("Execution complete")'''

#  Read a CSV file and display it in a formatted table.
'''import csv

try:
    # Step 1: Open the CSV file
    with open("students.csv", "r") as file:
        reader = csv.reader(file)

        # Step 2: Read all rows into a list
        rows = list(reader)

        # Step 3: Print header
        header = rows[0]
        print(f"{header[0]:<10} {header[1]:<5} {header[2]:<15}")

        # Step 4: Print each row in formatted style
        for row in rows[1:]:
            print(f"{row[0]:<10} {row[1]:<5} {row[2]:<15}")

except FileNotFoundError:
    print("Error: The CSV file was not found.")

except Exception as e:
    print("Error:", e)

finally:
    print("Execution complete")'''

# Write a program to store student records (name, roll number, marks) in a file and retrieve them.
'''try:
    # Step 1: Store student records in a file
    with open("students.txt", "w") as file:
        # Writing multiple records
        file.write("Sai,101,85\n")
        file.write("Ravi,102,90\n")
        file.write("Anita,103,95\n")

    print("Student records stored successfully!")

    # Step 2: Retrieve student records from the file
    with open("students.txt", "r") as file:
        records = file.readlines()

    print("\nRetrieved Student Records:")
    print(f"{'Name':<10} {'Roll':<10} {'Marks':<10}")
    for record in records:
        name, roll, marks = record.strip().split(",")
        print(f"{name:<10} {roll:<10} {marks:<10}")

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Error:", e)

finally:
    print("Execution complete")'''

# 🔵 Advanced Level
# - Implement a log file system that records every action with timestamps.
'''import datetime

def log_action(action):
    try:
        # Step 1: Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Step 2: Open log file in append mode
        with open("system_log.txt", "a") as logfile:
            # Step 3: Write action with timestamp
            logfile.write(f"[{timestamp}] {action}\n")

    except Exception as e:
        print("Error writing to log file:", e)

    finally:
        print("Log action complete")


# Example usage
log_action("System started")
log_action("User logged in")
log_action("File uploaded")
log_action("Error: Invalid input detected")'''

#  Create a program that reads a large file and splits it into smaller chunks.
'''def split_file(filename, chunk_size):
    try:
        # Step 1: Open the large file in read mode
        with open(filename, "r") as infile:
            data = infile.read()

        # Step 2: Split the data into chunks
        for i in range(0, len(data), chunk_size):
            # Step 3: Create chunk file names
            chunk_filename = f"chunk_{i//chunk_size + 1}.txt"

            # Step 4: Write each chunk into a separate file
            with open(chunk_filename, "w") as chunk_file:
                chunk_file.write(data[i:i+chunk_size])

        print("File split successfully into smaller chunks.")

    except FileNotFoundError:
        print("Error: The file was not found.")

    except Exception as e:
        print("Error:", e)

    finally:
        print("Execution complete")


# Example usage
split_file("largefile.txt", 1000)  # Splits into chunks of 1000 characters'''

# Implement a program to serialize and deserialize objects (e.g., using JSON or pickle in Python).
import json
import pickle

# Define a sample student object (dictionary)
student = {
    "name": "Sai",
    "roll_number": 101,
    "marks": 85
}

# ---------------- JSON Serialization ----------------
try:
    # Serialize (convert object to JSON string and save to file)
    with open("student.json", "w") as json_file:
        json.dump(student, json_file)
    print("Student object serialized to JSON.")

    # Deserialize (read JSON string back into Python object)
    with open("student.json", "r") as json_file:
        student_from_json = json.load(json_file)
    print("Deserialized from JSON:", student_from_json)

except Exception as e:
    print("JSON Error:", e)


# ---------------- Pickle Serialization ----------------
try:
    # Serialize (convert object to binary and save to file)
    with open("student.pkl", "wb") as pickle_file:
        pickle.dump(student, pickle_file)
    print("Student object serialized with pickle.")

    # Deserialize (read binary back into Python object)
    with open("student.pkl", "rb") as pickle_file:
        student_from_pickle = pickle.load(pickle_file)
    print("Deserialized from pickle:", student_from_pickle)

except Exception as e:
    print("Pickle Error:", e)

finally:
    print("Execution complete")