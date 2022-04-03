from tkinter import Tk, Label, Button, Entry, Listbox, Radiobutton, Checkbutton
from tkinter import *
# Start Point
window = Tk()
window.title("Tkinter")
window.minsize(width=500, height=300)
# -----------------------------------lable----------------------------------------
my_label = Label(text="My first Label", font=("Arial", 24, "bold"))  # create label
my_label.grid()
my_label.config(padx=20,pady=20)
# or
# my_label["text"] = "Hello"
# or
# my_label.config(text="Hello")

# -----------------Button-------------------------
# def button_click():
#     my_label["text"] = "I Got Clicked"
#     my_label.pack()

# my_button = Button(text="click", command=button_click)
# my_button.pack()

# -------------------Input--------------------------------
input = Entry(width=10)
input.grid(column=1, row=1)

def click_btn_lable_change():
    my_label["text"] = input.get()
    my_label.grid(column=2, row=2)

newBtn = Button(text="click", command=click_btn_lable_change)
newBtn.grid(column=3, row=4)
new2Btn = Button(text="submit", command=click_btn_lable_change)
new2Btn.grid(column=3, row=0)

# cant use pack and grid together

# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for fruit in fruits:
#     listbox.insert(fruits.index(fruit), fruit)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop()
# End Point
