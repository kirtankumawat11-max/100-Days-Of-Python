from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbol

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    # It will copy the password in clipbord with ourselves
    pyperclip.copy(password)

# ------------------------FIND PASSWORD -------------------------- #

def find_password():
    website = website_entry.get()
    try :
        with open("data.json","r") as file :
            data = json.load(file)
    except FileNotFoundError :
        messagebox.showinfo(title="Error",message="No data found.")
    else:
        if website in data :
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email : {email} \n Password : {password}")
        else :
            messagebox.showinfo(title="Error",message=f"No result for {website},This is not exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
    else:
        # json.dump(new_data , data_file , indent=4) -- to write some data , mode= w
        # data = json.load(data_file)  -- It's takes data and puts into list
        # print(data)
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except (FileNotFoundError,json.JSONDecodeError):
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)

        else :
            # Updating old data with new date
            data.update(new_data)
            with open("data.json","w") as data_file:
                # Saving the updated data
                json.dump(data, data_file,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.config(padx=5, pady=5)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_label.config(padx=5, pady=5)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(padx=5, pady=5)

# Entry

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()  # It will focus the cursor in website entry line
email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "kirtan@gmail.com")  # It will show in email entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button

generate_password_button = Button(text="Generate password",width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search",width=15,command=find_password)
search_button.grid(column=2,row=1)

window.mainloop()