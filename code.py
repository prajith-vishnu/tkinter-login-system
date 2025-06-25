import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Login System")
root.geometry("500x300")

username_saved = ""
password_saved = ""

def create_account():
    global username_saved, password_saved
    username = create_u_entry.get()
    password = create_p_entry.get()

    if not username or not password:
        messagebox.showwarning("Error", "Enter both fields")
        return

    username_saved = username
    password_saved = password
    messagebox.showinfo("Done", "Account created")
    load_login()

def login():
    username = u_entry.get()
    password = p_entry.get()

    if username == username_saved and password == password_saved:
        messagebox.showinfo("Welcome", f"Hello {username}")
    else:
        messagebox.showerror("Error", "Wrong credentials")

def load_login():
    for w in root.winfo_children():
        w.destroy()

    header = ttk.Label(root, text="Login", font=("Arial", 16))
    header.place(relx=0.5, rely=0.1, anchor='center')

    ttk.Label(root, text="Username").place(relx=0.1, rely=0.3)
    global u_entry
    u_entry = ttk.Entry(root)
    u_entry.place(relx=0.4, rely=0.3, relwidth=0.5)

    ttk.Label(root, text="Password").place(relx=0.1, rely=0.45)
    global p_entry
    p_entry = ttk.Entry(root, show="*")
    p_entry.place(relx=0.4, rely=0.45, relwidth=0.5)

    ttk.Button(root, text="Login", command=login).place(relx=0.1, rely=0.65)

ttk.Label(root, text="Create Account", font=("Arial", 16)).place(relx=0.5, rely=0.1, anchor='center')

ttk.Label(root, text="New Username").place(relx=0.1, rely=0.3)
create_u_entry = ttk.Entry(root)
create_u_entry.place(relx=0.4, rely=0.3, relwidth=0.5)

ttk.Label(root, text="New Password").place(relx=0.1, rely=0.45)
create_p_entry = ttk.Entry(root, show="*")
create_p_entry.place(relx=0.4, rely=0.45, relwidth=0.5)

ttk.Button(root, text="Create Account", command=create_account).place(relx=0.1, rely=0.65)

root.mainloop()
