"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules7
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups7

# Hide the window, hint: use the withdraw method
window.withdraw
# Ask the user for the first number   
a1=simpledialog.askinteger("your first number", "insert number here")
# Ask the user for the second number
a2=simpledialog.askinteger("your second number", "insert number here")
# Display the sum of the two numbers 
a=a1+a2
messagebox.showinfo("your answer", a)

# Keep the window open

7
