#print numbers 1 t0 n natural numbers
import tkinter as tk

# Function to update expression in the text entry
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

# Function to clear the entry
def clear():
    global expression
    expression = ""
    equation.set("")

# Main program
if __name__ == "__main__":
    # Create main window
    gui = tk.Tk()
    gui.configure(background="lightgray")
    gui.title("Simple Calculator")
    gui.geometry("300x400")

    expression = ""
    equation = tk.StringVar()

    # Entry field
    entry_field = tk.Entry(gui, textvariable=equation, font=('Arial', 40), bd=5, insertwidth=20, width=9, borderwidth=10)
    entry_field.grid(columnspan=80)

    # Buttons
    buttons = [
        '7', '8', '9', '+',
        '4', '5', '6', '-',
        '1', '2', '3', '*',
        '0', 'C', '=', '/'
    ]

    row_val = 1
    col_val = 0

    for button in buttons:
        if button == "C":
            b = tk.Button(gui, text=button, fg="black", bg="red",
                        command=clear, height=3, width=9)
        elif button == "=":
            b = tk.Button(gui, text=button, fg="black", bg="green",
                        command=equalpress, height=3, width=9)
        else:
            b = tk.Button(gui, text=button, fg="black", bg="lightblue",
                        command=lambda b=button: press(b), height=3, width=9)

        b.grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

    gui.mainloop()