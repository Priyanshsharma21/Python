# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letter = random.randint(8, 10)
nr_number = random.randint(2, 4)
nr_symbols = random.randint(2, 4)



letter_pass = [random.choice(letters) for i in range(nr_letter)]
number_pass = [random.choice(numbers) for i in range(nr_number)]
symb_pass = [random.choice(symbols) for i in range(nr_symbols)]

password_list = letter_pass + number_pass + symb_pass
random.shuffle(password_list)

password = "".join(password_list)

# ----------------------search-----------------------------
def search():
    website = website_ip.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# try to use if else ,  if dont solve then use try catch
# ---------------------------- SAVE PASSWORD ------------------------------- #

def savePassword():
    websiteName = website_ip.get()
    userName = email_ip.get()
    password = pass_ip.get()

    newData = {
        websiteName : {
            "email" : userName,
            "password": password
        }
    }

    if len(websiteName) == 0 or len(userName) == 0 or len(password) == 0:
        empty()

    else:
        try:
            with open("file.json", mode='r') as data:
                # json.dump(newData, file, indent=4) # use to write into json format
                data_file = json.load(data) # reading old data
        except FileNotFoundError :
            with open("file.json", mode='w') as data:
                json.dump(newData, data, indent=4)
        else:
            data_file.update(newData)  # updating old data

            with open("file.json", mode='w') as data:
                json.dump(data_file, data, indent=4) # saving new data
        finally:
            website_ip.delete(0, END)
            pass_ip.delete(0, END)

# -----------------------------------------------------------------------------------
# def show_confirmation():
#     return messagebox.askokcancel(f"{website_ip.get()}",
#                                   f"Do you wanna submit it \n Email : {email_ip.get()}\n Password: {pass_ip.get()}\n click ok for confirm")


def empty():
    messagebox.showinfo(f"{website_ip.get()}", "Hey! you left some field empty....")

#-------------------------------Generate password--------------------------#

def gen_pass():
    pass_ip.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import messagebox
from tkinter import *

# Logo setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
bg = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=bg)
canvas.grid(column=1, row=0)

# ------------------- lable and button setup-------------------------#

website = Label(text="Website: ", font=("Arial", 10, "bold"))
website.grid(column=0, row=1)

website = Label(text="Email/Username: ", font=("Arial", 10, "bold"))
website.grid(column=0, row=2)

website = Label(text="Password: ", font=("Arial", 10, "bold"))
website.grid(column=0, row=3)

# --------------------Entry-------------------------------#

website_ip = Entry(width=21)
website_ip.focus()
website_ip.grid(column=1, row=1, columnspan=2)

email_ip = Entry(width=35)
email_ip.insert(END, "piyuindia4@gmail.com")
email_ip.grid(column=1, row=2, columnspan=2)

pass_ip = Entry(width=17)
pass_ip.grid(column=1, row=3)

# -------------------Button-------------------#
search = Button(text="Search", command=search)
search.grid(row=1, column=2)
add = Button(text="Add", width=36, command=savePassword)
add.grid(column=1, row=4, columnspan=2)
gen_pass = Button(text="Generate Password", command=gen_pass)
gen_pass.grid(column=2, row=3)

window.mainloop()
