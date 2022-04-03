from tkinter import *

window = Tk()
window.title("Miles to Km converter")
window.config(padx=100, pady=100)
window.minsize(600, 400)

# inupt
enterMiles = Entry()
enterMiles.grid(column=1, row=0)
# Input lable
entryLable = Label(text="Miles", font=("itallic", 14, "bold"))
entryLable.grid(column=2, row=0)
entryLable.config(padx=10)

# lable is equal to

isEqualLable = Label(text="is equal to", font=("itallic", 14, "bold"))
isEqualLable.grid(column=0, row=1)
entryLable.config(padx=10)

ans = Label(text="0", font=("itallic", 14, "bold"))
ans.grid(column=1, row=1)
entryLable.config(padx=20)

km = Label(text="Km", font=("itallic", 14, "bold"))
km.grid(column=2, row=1)
entryLable.config(padx=10)


# buttons

def calculate_km():
    value = int(enterMiles.get())
    miles = (value * 1.6)
    ans.config(text=(miles))


calculate = Button(text="calculate", command=calculate_km)
calculate.grid(column=1, row=2)

window.mainloop()
