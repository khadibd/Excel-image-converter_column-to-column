import tkinter as tk
from tkinter import messagebox
from app import process

def run():
    try:
        process()
        messagebox.showinfo("Success", "Conversion finished successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Image Converter")

btn = tk.Button(root, text="Run Conversion", command=run, width=25, height=2)
btn.pack(padx=20, pady=20)

root.mainloop()
