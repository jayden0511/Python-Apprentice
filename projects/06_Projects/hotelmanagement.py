
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

guest = {}

db = {} 

level_floors = ("1 2 3 4 5 6 7 8")
room_numbers = ("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20")

def i(db):
    while True:
        print(db)
        ask = simpledialog.askstring("Hotel management" , "What is your name?")
        check = simpledialog.askstring("Hotel management", "Would you like to check in, out or quit?")
        if check == "check in" or check == "in":
            chosen_rooms = []
            level_floor = simpledialog.askinteger("Hotel management", level_floors)
            if level_floor >8:
                print("Error")
                return
                room_func(room_numbers)
            guests = simpledialog.askinteger("Hotel management", "How many guests are you traveling with?")
            nights = simpledialog.askinteger("Hotel management", "How many nights are staying?")
            price = nights*200
            messagebox.showinfo("Your cost is:", price)
            db[ask] = chosen_rooms
        elif check == "check out" or check == "out":
            messagebox.showinfo("Hotel management", "Thank you for your time")
            messagebox.showinfo("Your cost is:", price)
            db.pop[ask]
        elif check == "quit" or check == "quit":
            break
def room_func(room_numbers, chosen_rooms):
    room_number = simpledialog.askinteger("Hotel management", room_numbers)
    chosen_rooms.append(room_number)
    if room_number in room_numbers:
        room_numbers.remove(room_number)
        if room_number >20 or room_number in chosen_rooms:
                messagebox.showerror("Error")
                return
        
    return room_number
i(db)
