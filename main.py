import random
from tkinter import *
import tkinter as tk

# function to read a list of words from a text file
def read_word_list(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

# read lists of prefixes and suffixes from text files
prefixes = read_word_list('prefixes.txt')
weaponType = read_word_list('weaponType.txt')
suffixes = read_word_list('suffixes.txt')

# function to generate weapon names
def generate_weapon_name():
    # choose a random prefix and suffix
    prefix = random.choice(prefixes)
    weapon = random.choice(weaponType)
    suffix = random.choice(suffixes)
    # combine the two and return the result
    return prefix + ' ' + weapon + ' ' + suffix

# generate and print some weapon names
##for i in range(1):
##    print(generate_weapon_name())





### Some GUI Shit Now Baby!!! ###

# function to be called when the button is clicked
def button_clicked():
    weaponName = generate_weapon_name()
    label.config(text=weaponName)

# create a new window
window = tk.Tk()

# set the window title
window.title("My GUI")

# create a label widget to display text
label = tk.Label(window, text="Placeholder", font=("Helvetica", 24))

# create a button widget and associate it with the button_clicked function
img = PhotoImage(file="buttonGraphic.png")
button = tk.Button(window, image=img, command=button_clicked)

# pack the label and button widgets in the window
label.pack()
button.pack()

# start the main event loop
window.mainloop()