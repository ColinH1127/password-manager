from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    random_letters = [random.choice(letters) for letter in range(nr_letters)]
    random_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for number in range(nr_numbers)]


    password_list = random_letters + random_numbers + random_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    entry3.delete(0, "end")
    entry3.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Oops", message="All fields must be completed.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                      f"Email: {email}\n"
                                                      f"Password: {password}\n"
                                                      f"Is this ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                entry1.delete(0, "end")
                entry3.delete(0, "end")
            messagebox.showinfo(title=website, message=f"Login data for {website} saved")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)

logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
label1 = Label(text="Website:")
label1.grid(row=1, column=0)
entry1 = Entry(width=35)
entry1.grid(row=1, column=1, columnspan=2)
entry1.focus()
label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
entry2 = Entry(width=35)
entry2.grid(row=2, column=1, columnspan=2)
entry2.insert(0, "colinhussey82@gmail.com")
label3 = Label(text="Password:")
label3.grid(row=3, column=0)
entry3 = Entry(width=18)
entry3.grid(row=3, column=1)
button3 = Button(text="Generate Password", width=15, command=generate_password)
button3.grid(row=3, column=2)
button4 = Button(text="Add", width=35, command=add_password)
button4.grid(row=4, column=1, columnspan=2)


window.mainloop()