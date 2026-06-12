import tkinter as tk
from tkinter import messagebox

PASSWORD = "ALIB TAMPAN"

def unlock():
    if password_entry.get() == PASSWORD:
        root.destroy()
    else:
        messagebox.showerror("Error", "Password salah!")
        password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Screen Lock")
root.attributes("-fullscreen", True)
root.configure(bg="black")

root.protocol("WM_DELETE_WINDOW", lambda: None)

title = tk.Label(
    root,
    text="SCREEN LOCK",
    font=("Arial", 30, "bold"),
    fg="white",
    bg="black"
)
title.pack(pady=50)

password_entry = tk.Entry(
    root,
    show="*",
    font=("Arial", 20),
    justify="center"
)
password_entry.pack(pady=20)

button = tk.Button(
    root,
    text="UNLOCK",
    font=("Arial", 18),
    command=unlock
)
button.pack(pady=20)

root.bind("<Return>", lambda event: unlock())

root.mainloop()