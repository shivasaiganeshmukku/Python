'''
🔹 Beginner Level
- Write a program that asks the user to input a number.
- Handle the case where the user enters a non-numeric value using try-except.
- Divide two numbers entered by the user.
- Handle division by zero.
- Create a list and try to access an index that doesn’t exist.
- Catch the IndexError.


🔹 Intermediate Level
- Write a program to open a file and read its contents.
- Handle the case where the file does not exist (FileNotFoundError).
- Create a dictionary and try to access a key that doesn’t exist.
- Handle the KeyError.
- Implement a calculator program.
- Handle invalid operations (like dividing by zero or entering wrong operator).
- Write a program that converts a string to an integer.
- Handle ValueError if the string is not numeric.

🔹 Advanced Level
- Build a program that simulates an ATM machine:
- Handle exceptions like insufficient balance, invalid PIN, or invalid input.
- Write a program that connects to a database (or simulate with a dictionary).
- Handle exceptions for connection failure or invalid queries.
- Create a program that processes a list of numbers from a file.
- Handle multiple exceptions: file not found, invalid data format, division by zero.
- Implement a custom exception class NegativeNumberError.
- Raise it when the user enters a negative number where only positive is allowed.
- Build a program that demonstrates finally block:
- Example: Always close a file or release a resource, even if an exception occurs.

🎯 Simple Way to Understand Exception Handling
Think of it like a seatbelt in a car:
- You hope you never need it, but if something goes wrong, it protects you.
- try → attempt the risky action.
- except → catch the error if it happens.
- finally → clean up (like closing files or releasing resources).
'''
# - Write a program that asks the user to input a number.
# - Handle the case where the user enters a non-numeric value using try-except.
'''try:
    n = int(input("Enter a Number: "))
    print("You entered:", n)
except ValueError:
    print("Error: Please enter a numeric value.")
finally:
    print("Execution complete")'''

#  Divide two numbers entered by the user.
# - Handle division by zero.

'''try:
    n = float(input("Enter a  value: "))
    m = float(input("enter a value: "))
    s= n/m
    print("result: ", s )
except ZeroDivisionError:
    print("Error: Zero Division Error . You can not divide with zero")
except ValueError:
    print("Error: Enter a numeric values")
finally:
    print("Execution completed")'''

#  Create a list and try to access an index that doesn’t exist.
# - Catch the IndexError.
'''try:
    ss = [10, "twenty",30, 40, "fifty"]
    print("Index value: ", ss[6])
except IndexError as e:
    print("Error: index out of bound ")
finally:
    print("code execution completed")'''

# 🔹 Intermediate Level
# - Write a program to open a file and read its contents.
# - Handle the case where the file does not exist (FileNotFoundError).
'''try:
    with open('example.txt',"r") as file:
        contents = file.read()
        print("file contents:\n", contents)
except FileNotFoundError:
    print("Error: The file does not exist")
finally:
    print("file is not there")'''


# - Create a dictionary and try to access a key that doesn’t exist.
# - Handle the KeyError.
'''try:
    my_dict = {"name": "shiva", "age":"21"," city":"Hyderabad"}

    print("value:",my_dict["country"])
except KeyError:
    print("Error: The key does not exist in the dictionary")
finally:
    print("Execution Complete")'''

# - Implement a calculator program.
# - Handle invalid operations (like dividing by zero or entering wrong operator).
'''try:
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform calculation based on operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Handle division by zero
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2
    else:
        # Handle invalid operator
        raise ValueError("Invalid operator")

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError as e:
    print("Error:", e)

finally:
    print("Execution complete")'''

#  Write a program that converts a string to an integer.
# - Handle ValueError if the string is not numeric.
'''try :
    user_input = input("Enter a number")
    number  = int(user_input)
    print("Converted Integer:" , number)
except ValueError:
    print("Error: the value is not valid integer")
finally:
    print("execution complete")'''

# 🔹 Advanced Level
# - Build a program that simulates an ATM machine:
# - Handle exceptions like insufficient balance, invalid PIN, or invalid input.
'''class InvalidPINError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

def atm_machine():
    # Predefined PIN and balance
    correct_pin = "1234"
    balance = 5000.0

    try:
        # Ask for PIN
        pin = input("Enter your PIN: ")
        if pin != correct_pin:
            raise InvalidPINError("Invalid PIN entered.")

        print("\nWelcome to the ATM!")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    raise InsufficientBalanceError("Insufficient balance.")
                balance -= amount
                print("Withdrawal successful. Remaining balance:", balance)
            except ValueError:
                print("Error: Please enter a valid numeric amount.")

        elif choice == "3":
            try:
                amount = float(input("Enter amount to deposit: "))
                balance += amount
                print("Deposit successful. New balance:", balance)
            except ValueError:
                print("Error: Please enter a valid numeric amount.")

        else:
            raise ValueError("Invalid operation selected.")

    except InvalidPINError as e:
        print("Error:", e)

    except InsufficientBalanceError as e:
        print("Error:", e)

    except ValueError as e:
        print("Error:", e)

    finally:
        print("Thank you for using the ATM.")

# Run the ATM simulation
atm_machine()'''

# - Write a program that connects to a database (or simulate with a dictionary).
# - Handle exceptions for connection failure or invalid queries.
'''class ConnectionError(Exception):
    pass
class InvalidQueryError(Exception):
    pass
def connect_to_database(simulate_failure = False):
    if simulate_failure:
        raise ConnectionError("Failed to connect the database")
    return{
        "101":{"name ": 'Shiva',"balance": 5000},
        "102":{"name": "sai","balance":6000},
        "103":{"name":"ganesh","balance":7000}
    }
def query_database(db, key):
    if key  not in db:
        raise InvalidQueryError(f"Record with id{key} not found")
    return db[key]
try:
    database = connect_to_database(simulate_failure=False)
    print("connected to database successful.")

    record_id = input("Enter record id to fetch: ")
    record = query_database(database,record_id)
    print("Record found: ",record)
except ConnectionError as e:
    print("Error: ", e)
except InvalidQueryError as e:
    print("Error: ",e)
finally:
    print("Execution complete")'''

# - Create a program that processes a list of numbers from a file.
# - Handle multiple exceptions: file not found, invalid data format, division by zero.
'''class InvalidDataError(Exception):
    pass
def process_file(filename):
    try:
        with open(filename, "r") as  file:
            numbers =file.readlines()

            int_numbers = []
            for num in numbers:
                num = num.strip()
                if not num.isdigit():
                    raise InvalidDataError(f"Invalid data format: '{num}'")
                int_numbers.append(int(num))
            try:
                result = int_numbers[0]/int_numbers[1]
                print("Division Result: ",result)
            except ZeroDivisionError:
                print("Error: Division by is not allowed.")
    except FileNotFoundError:
        print("File not found")
    except InvalidDataError as e:
        print("Error: ", e)

    finally:
        print("Execution complete.")
filename = input("Enter file name: ")
process_file(filename)'''

# Implement a custom exception class NegativeNumberError.
# - Raise it when the user enters a negative number where only positive is allowed.
'''class NegativeNumberError(Exception):
    pass
def positive_input(n):
    if n < 0 :
        raise NegativeNumberError("Negative numbers are not allowed.")
    return n
try :
    num = positive_input(-5)
    print("Number Entered ",num)
except NegativeNumberError as e:
    print("Error: ", e)'''

# Build a program that demonstrates finally block:
# - Example: Always close a file or release a resource, even if an exception occurs.
try:
    f = open("sample.txt","w")
    f.write("Hello world")
    raise Exception("Simulated error")
except Exception as e:
    print("Caught exception: ", e)

finally :
    f.close()
    print("File closed successfully(finally block executed).")
    