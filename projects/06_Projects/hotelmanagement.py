
"""
Hotel Management System
1. Functions needed:
    1a. Be able to check in or check out
    1b. recieve price
    1c. choose room
    1d. how many guests
5. Should use lists, tuples, dictionaries
6. All functionality in functions
""" 
from tkinter import messagebox, simpledialog, Tk 
window = Tk()     
window.withdraw()

db = {}

room_numbers = ("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")

def i():
    ask = simpledialog.askstring("Hotel management" , "What is your name?")
    check = simpledialog.askstring("Hotel management", "Would you like to check in or out?")
    if check == "check in" or check == "in":
        chosen_rooms = []
        room_number = simpledialog.askstring("Hotel management", room_numbers)
        guests = simpledialog.askinteger("Hotel management", "How many guests are you traveling with?")
        nights = simpledialog.askinteger("Hotel management", "How many nights are staying?")
        price = nights*90
    elif check == "check out" or check == "out":
        messagebox.showinfo("Hotel management", "Thank you for your time")
        messagebox.showinfo("Your cost is:", price)
    db =[] 