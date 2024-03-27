import tkinter as tk
from tkinter import ttk

def change_button_color(color, button):
    button.configure(background=color)

def main():
    root = tk.Tk()
    root.grid_anchor('center')
    root.geometry('400x450')

    style = ttk.Style()
    style.theme_use('clam')

    # Define button styles
    style.map("design1.TButton", background=[("pressed", "red"), ("active", "blue"), ("!disabled", "skyblue")],
              foreground=[("pressed", "white"), ("active", "yellow")],
              font=[("pressed", "Arial 14 bold"), ("active", "Georgia 12 bold")])
    style.map("design2.TButton", background=[("pressed", "green"), ("active", "red"), ("!disabled", "lightyellow")],
              foreground=[("pressed", "yellow"), ("active", "white")],
              font=[("pressed", "times 14 bold"), ("active", "Georgia 16 bold")])

    # Create buttons
    button1 = ttk.Button(root, text="Button", style="design1.TButton", padding=20, width=30)
    button1.grid(row=0, column=0, padx=5, pady=5)

    button2 = ttk.Button(root, text="Button", style="design2.TButton", padding=20, width=30)
    button2.grid(row=1, column=0, padx=5, pady=5)

    # List of colors
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

    # Create Listbox to select colors
    color_listbox = tk.Listbox(root, selectmode=tk.SINGLE, exportselection=0)
    for color in colors:
        color_listbox.insert(tk.END, color)
    color_listbox.grid(row=2, column=0, padx=5, pady=5)

    # Bind Listbox selection to change button color
    color_listbox.bind('<<ListboxSelect>>', lambda event: change_button_color(colors[color_listbox.curselection()[0]], button1))

    root.mainloop()

if __name__ == "__main__":
    main()