from tkinter import messagebox, simpledialog, Tk
import sys
import random


window = Tk()
window.withdraw()

# 1. Change this line to give you a random number between 1 - 100.
random_num = random.randint(1, 101)

# 2. Print out the random variable that you made in step #1
from tkinter import messagebox, simpledialog, Tk
# 3. Code a for loop to run steps 4-10, 10 times
for i in range(10):
    
    # 4. Ask the user for a guess using a pop-up window, and save their response
    guess = simpledialog.askinteger("Number guess pt.2", "Guess my number")
    # 5. If the guess is correct
        # 6. Win. Use 'sys.exit(0)' to end the program
    if guess == random_num:
        sys.exit(0)

    # 7. if the guess is high
        # 8. Tell them it's too high
    elif guess > random_num:
        messagebox.showinfo("Number guess pt.2", "Your guess is too high")
    # 9. Else if the guess is low
        # 10. Tell them it's too low
    else:
        messagebox.showinfo("Number guess pt.2", "Your guess is too low")
#11. Outside of the loop, tell the user they lost
messagebox.showinfo("Number guess pt.2", "you lost")
window.mainloop()
