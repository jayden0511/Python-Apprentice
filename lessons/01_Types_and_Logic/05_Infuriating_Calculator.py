"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
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
# Ask the user for the math operation
a3=simpledialog.askstring("would you like to do 1=addition 2=subtraction 3=multiplication 4=division")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if a3 == 1:
    a=a1+a2
elif a3 == 2:
    a=a1-a2
elif a3 == 3:
    a=a1*a2   
elif a3 == 4:
    a=a1/a2
else:
    messagebox.showinfo("Error6")
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()

# Keep the window open
