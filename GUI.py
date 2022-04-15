import tkinter as tk

import pandas as pd

import meal_tracker


# Gets user input and passes it to the search function
def search_button():
    search_input = user_input.get()

    search_results = tk.Text(root, height=20, width=70)
    search_results.insert(tk.END, meal_tracker.search(query=search_input))
    search_results.grid(row=1, column=4)


root = tk.Tk()
root.geometry("1500x700")
root.title("Meal Planner")

# Displays all data on right side of GUI
t = tk.Text(root, height=30, width=70)
t.insert(tk.END, meal_tracker.get_data())

label_text = tk.StringVar()
label_text.set("All Meal Data")
l = tk.Label(root, textvariable=label_text, height=2)

# Search bar + label
user_input = tk.StringVar()

search_label = tk.Label(root, text='Search Dataframe\nUse column, value(s)', font=('calibre', 10, 'bold'))

search_bar = tk.Entry(root, textvariable=user_input)

search_btn = tk.Button(root, text='Search', command=search_button)

t.grid(row=1, column=0, pady=5, padx=20)
l.grid(row=0, column=0, pady=5)
search_label.grid(row=0, column=4)
search_bar.grid(row=0, column=5)
search_btn.grid(row=0, column=6)

tk.mainloop()
