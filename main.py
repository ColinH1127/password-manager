from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    if website == "" or email == "" or password == "":
        messagebox.showerror(title=website, message="All fields must be completed.")
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
            messagebox.showinfo(title=website, message=f"Login data for {website} saved.")


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
button3 = Button(text="Generate Password", width=15)
button3.grid(row=3, column=2)
button4 = Button(text="Add", width=35, command=add_password)
button4.grid(row=4, column=1, columnspan=2)


window.mainloop()